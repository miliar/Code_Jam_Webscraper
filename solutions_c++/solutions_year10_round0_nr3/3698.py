/*
 * thempark.cc
 *
 *  Created on: May 7, 2010
 *      Author: sainath
 */

#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

class grp{
public:
	long uniqid;
	long memb;

	grp(long memb){
		this->memb = memb;
		this->uniqid = 0;
	}

	grp(long uniqid, long memb){
		this->memb = memb;
		this->uniqid = uniqid;
	}

};

int main(int argc, char *argv[]){
/*
	if(argc<2){
		printf("No filename\n");
		return -1;
	}
*/
/*
	ofstream fout("llarge.in", ios::out);
	int wr_t = 1;
	fout<<wr_t<<endl;
	for(int i=0; i<wr_t; i++){
		long wr_r, wr_n, wr_k;

		wr_r = ((float)rand()/RAND_MAX)*pow(10,7);
		wr_n = ((float)rand()/RAND_MAX)*pow(10,3);
		wr_k = ((float)rand()/RAND_MAX)*pow(10,8);

		fout<<wr_r<<" "<<wr_k<<" "<<wr_n<<endl;

		for(int j=0; j<wr_n; j++){
			int gij = ((float)rand()/RAND_MAX)*pow(10,6);
			fout<<gij<<" ";
		}
		fout<<endl;

	}
	fout.close();

	printf("Write complete\n");
*/
	ifstream fp("C-small-attempt0 (1).in", ios::in);

	long T;
	fp >> T;

	int count = 1;

	while(T > 0){

		long R, k, N;
		fp >> R >> k >> N;

		vector<grp> grps;

		int grp_count = N;
		while(grp_count>0){
			long mem;
			fp >> mem;
			if(grp_count==N){
				grp gr(1, mem);
				grps.push_back(gr);
			}
			else{
				grp gr(mem);
				grps.push_back(gr);
			}
			grp_count--;
		}
		//printf("grp vector created\n");

		vector<long> tours;
		long period = 0;

		int flag_done = 0;
		while(!flag_done){

			long sum = 0;
			long curr_grp_cnt = N;

			while(sum<k){
				if(sum+grps.at(0).memb>k || curr_grp_cnt<=0)
					break;
				curr_grp_cnt--;
				sum += grps.at(0).memb;
				grp grf = grps.front();
				grps.erase(grps.begin());
				grps.push_back(grf);
			}

			//printf("sum: %ld\n", sum);
			//for(int i=0; i<grps.size(); i++)
			//	printf("%ld %ld\n", grps.at(i).uniqid, grps.at(i).memb);

			tours.push_back(sum);

			//printf("R: %d\n", R);

			R--;
			if(R<=0 || grps.at(0).uniqid==1)
				flag_done = 1;

			//printf("R: %d || %d\n", R, grps.at(0).uniqid);

			period++;
			//printf("period: %ld\n", period);
		}

		//printf("R: %d, period: %d\n", R, period);

		R += period;

		long curr_sum = 0;
		for(int i=0; i<tours.size(); i++)
			curr_sum += tours.at(i);

		//printf("curr_sum %ld, tours pushed: %d\n", curr_sum, tours.size());

		if(R>0){
			curr_sum = (R/period)*curr_sum;
			int left_out = R%period - 1;
			if(left_out >= 0){
				while(left_out>=0)
					curr_sum += tours.at(left_out--);
			}
		}

		cout<<"Case #"<<count<<": "<<curr_sum<<endl;

		count++;
		T--;
	}

	return 0;

}
