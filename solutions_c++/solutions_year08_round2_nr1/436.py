#include <fstream>
#include <iostream>
#include <string>
#include <stdio.h>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

int main(){
	ifstream fin("A-small.in");
	ofstream fout ("output.txt");
	int N;
	fin >> N;
	long long n, A, B, C, D, x0, y0 ,M;
	
	for(int i=0;i<N;i++){
		map <pair <long long ,long long> ,int> mp;
		vector <pair<long long, long long> > vp;
		for(long long k=0;k<3;k++){
			for(long long j=0;j<3;j++){
				mp[make_pair(k,j)]=0;
				vp.push_back(make_pair(k,j));
			}
		}
		fin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		mp[make_pair(x0%3,y0%3)]=1;
		for (int j = 1;j<n;j++){
		  x0 = (A * x0 + B) % M;
		  y0 = (C * y0 + D) % M;
		  mp[make_pair(x0%3,y0%3)]++;
		  
		}
		long long sum=0,temp1,temp2,temp3;
		for(int k=0;k<vp.size();k++){
			temp1 = mp[vp[k]];
			sum+= temp1 * (temp1-1) * (temp1-2)/6;
			for(int j=k+1;j<vp.size();j++){
				temp2 = mp[vp[j]];
				if (((2*vp[k].first+vp[j].first)%3==0)&&((2*vp[k].second+vp[j].second)%3==0))
					sum+=temp1*(temp1-1)*temp2/2;
				if (((2*vp[j].first+vp[k].first)%3==0)&&((2*vp[j].second+vp[k].second)%3==0))
					sum+= temp2*(temp2-1)*temp1/2;
				for(int l=j+1;l<vp.size();l++){
					long long aa = vp[k].first+vp[j].first+vp[l].first;
					long long bb = vp[k].second+vp[j].second+vp[l].second;
					if((aa%3==0)&&(bb%3==0)){
						temp3 = mp[vp[l]];
						sum+= temp1*temp2*temp3;
					}
				}
			}
		}
		fout << "Case #"<<i+1 << ": " << sum << endl;
	}
	return 0;
};