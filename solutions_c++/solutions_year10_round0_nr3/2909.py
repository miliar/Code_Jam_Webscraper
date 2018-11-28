/*
 * thempark.cc
 *
 *  Created on: May 7, 2010
 *      Author: sainath
 */

#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

class grp{
public:
	int uniqid;
	int memb;


	grp(int uniqid, int memb){
		//printf("%ld %ld\n", memb, uniqid);
		this->memb = memb;
		this->uniqid = uniqid;
	}

};

int main(int argc, char *argv[]){
/*
	if(argc<2){
		prlong longf("No filename\n");
		return -1;
	}
*/
/*
	ofstream fout("llarge.in", ios::out);
	long long wr_t = 1;
	fout<<wr_t<<endl;
	for(long long i=0; i<wr_t; i++){
		long long wr_r, wr_n, wr_k;

		wr_r = ((float)rand()/RAND_MAX)*pow(10,7);
		wr_n = ((float)rand()/RAND_MAX)*pow(10,3);
		wr_k = ((float)rand()/RAND_MAX)*pow(10,8);

		fout<<wr_r<<" "<<wr_k<<" "<<wr_n<<endl;

		for(long long j=0; j<wr_n; j++){
			long long gij = ((float)rand()/RAND_MAX)*pow(10,6);
			fout<<gij<<" ";
		}
		fout<<endl;

	}
	fout.close();

	prlong longf("Write complete\n");
*/
	ifstream fp("C-large (1).in", ios::in);

	long long T;
	fp >> T;

	long long count = 1;

	while(T > 0){

		int R, k, N;
		fp >> R >> k >> N;

		queue<grp> grps;

		int grp_count = N;
		while(grp_count>0){
			int mem;
			fp >> mem;

			int uniqid = N-grp_count;

			//printf("Creating: %d %d\n", uniqid, mem);

			grp gr(uniqid, mem);
			grps.push(gr);

			grp_count--;
		}
		//prlong longf("grp vector created\n");
		//for(long long i=0; i<grps.size(); i++)
		//	printf("%ld %ld\n", grps.at(i).uniqid, grps.at(i).memb);

		vector<long long> tours;
		vector<int> ids;

		int period = 0;

		int check_period = 0;

		int rem_rides = R;
		long long flag_done = 0;
		while(!flag_done){

			long long sum = 0;
			long long curr_grp_cnt = N;

			while(sum<k){
				if(sum+grps.front().memb>k || curr_grp_cnt<=0)
					break;
				curr_grp_cnt--;
				grp grf = grps.front();
				sum += grf.memb;
				grps.pop();
				grps.push(grf);
			}

			rem_rides--;

			//printf("R: %d || %d || %ld\n",
			//		rem_rides,  grps.front().uniqid, sum);

			vector<int>::iterator vit = find(ids.begin(), ids.end(), grps.front().uniqid);
			if(vit != ids.end() || rem_rides<=0){
				flag_done = 1;
			}

			tours.push_back(sum);
			ids.push_back(grps.front().uniqid);

			//prlong longf("period: %ld\n", period);
		}

		//printf("Searching for %d\n", *(ids.end()-1));
		int header = 0;
		vector<int>::iterator vit = find(ids.begin(), ids.end()-1, *(ids.end()-1));
		if(vit != ids.end()-1){
			header = (int) (vit - ids.begin() + 1);
			period = (int) (ids.end()-1 - vit);
		}
		else{
			period = -1;
		}

		//printf("R: %d, header: %d, period: %d\n", R, header, period);

		long long tot_sum = 0;

		if(period<0){
			for(int i=0; i<tours.size(); i++)
				tot_sum += tours.at(i);
		}
		else{

			long long curr_sum = 0;
			for(int i=header; i<header+period; i++)
				curr_sum += tours.at(i);

			//printf("curr_sum: %ld\n",  curr_sum);

			for(int i=0; i<header; i++)
				tot_sum += tours.at(i);

			R = R-header;

			//printf("Rides rem: %d, Initial sum: %ld\n",R,tot_sum);

			if(R>0 && period>0){
				tot_sum += (R/period)*curr_sum;
				int tail = R%period;
				for(int i=header; i<header+tail; i++)
					tot_sum += tours.at(i);
			}
		}

		cout<<"Case #"<<count<<": "<<tot_sum<<endl;

		count++;
		T--;
	}

	return 0;

}
