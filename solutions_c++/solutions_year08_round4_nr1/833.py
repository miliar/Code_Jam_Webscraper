#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <set>
#include <cmath>
#include <string>
using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");

int t,T;


int main() {
	fin>>T;
	int m,v;
	vector<int> vec;
	vector<int> a;
	vector<int> c;
	vector<int> dp;
	int i,x,y,tmp;
	for(t=1;t<=T;t++) {
		//cout<<t<<endl;
		fin>>m>>v;
		vec.resize(m+1);
		a.resize(m+1);
		c.resize(m+1);
		vec.resize(m+1);
		dp.resize(m+1);
		//cout<<'g'<<endl;
		for(i=1;i<=m;i++) {
			if(i<=m/2) {
				//cout<<"-- "<<i<<endl;
				fin>>a[i]>>c[i];
			}
			else {fin>>vec[i];}
		}
		//cout<<'g'<<endl;
		for(i=m/2;i>=1;i--) {
			if(a[i]==1) {
				if(vec[i*2]==1 && vec[i*2 + 1]==1)vec[i]=1;
				else vec[i]=0;
			}
			else {
				if(vec[i*2]==1 || vec[i*2 + 1]==1)vec[i]=1;
				else vec[i]=0;
			}
		}
		if(vec[1]==v) {
			fout<<"Case #"<<t<<": 0"<<endl;
			continue;
		}
		for(i=1;i<=m;i++)dp[i]=-1;
		//cout<<"h"<<endl;
		for(i=m/2;i>=1;i--) {
			dp[i]=-1;
			if(vec[i]==0) {
				if(a[i]==1) {
					/*tmp=-1;
					if(vec[i*2]==1)tmp=0;
					if(vec[i*2]==0 && dp[i*2]!=-1)tmp=dp[i*2];
					if(vec[i*2+1]==1)if(tmp==-1)tmp=0;
					if(vec[i*2+1]==- && dp[i*2+1]!=-1)if(tmp==-1 || tmp<dp[i*2+1])tmp=dp[i*2+1];
					if(vec[i*2]==0 && dp[])*/
					x=-1;y=-1;
					if(vec[2*i]==1)x=0;
					if(vec[2*i+1]==1)y=0;
					if(vec[2*i]==0 && dp[2*i]!=-1)x=dp[2*i];
					if(vec[2*i+1]==0 && dp[2*i+1]!=-1)y=dp[2*i+1];
					if(x==-1 || y==-1)tmp=-1;
					else tmp = x+y;
					if(tmp!=-1){if(dp[i]==-1 || dp[i]>tmp)dp[i]=tmp;}
				}
				if(a[i]==0) {
					x=-1;y=-1;
					if(vec[2*i]==1)x=0;
					if(vec[2*i+1]==1)y=0;
					if(vec[2*i]==0 && dp[2*i]!=-1)x=dp[2*i];
					if(vec[2*i+1]==0 && dp[2*i+1]!=-1)y=dp[2*i+1];
					//if(x==-1 || y==-1)tmp=-1;
					//else tmp = max(x,y);
					if(x==-1)tmp=y;
					else if(y==-1)tmp=x;
					else {
						tmp = x;if(tmp>y)tmp=y;
					}
					if(tmp!=-1){if(dp[i]==-1 || dp[i]>tmp)dp[i]=tmp;}
				}
				if(a[i]==1 && c[i]==1) {
					x=-1;y=-1;
					if(vec[2*i]==1)x=0;
					if(vec[2*i+1]==1)y=0;
					if(vec[2*i]==0 && dp[2*i]!=-1)x=dp[2*i];
					if(vec[2*i+1]==0 && dp[2*i+1]!=-1)y=dp[2*i+1];
					//if(x==-1 || y==-1)tmp=-1;
					//else tmp = max(x,y);
					if(x==-1)tmp=y;
					else if(y==-1)tmp=x;
					else {
						tmp = x;if(tmp>y)tmp=y;
					}
					if(tmp!=-1)tmp++;
					if(tmp!=-1){if(dp[i]==-1 || dp[i]>tmp)dp[i]=tmp;}
				}
			}
			else {
				if(a[i]==1) {
					x=-1;y=-1;
					if(vec[2*i]==0)x=0;
					if(vec[2*i+1]==0)y=0;
					if(vec[2*i]==1 && dp[2*i]!=-1)x=dp[2*i];
					if(vec[2*i+1]==1 && dp[2*i+1]!=-1)y=dp[2*i+1];
					//if(x==-1 || y==-1)tmp=-1;
					//else tmp = max(x,y);
					if(x==-1)tmp=y;
					else if(y==-1)tmp=x;
					else {
						tmp = x;if(tmp>y)tmp=y;
					}
					if(tmp!=-1){if(dp[i]==-1 || dp[i]>tmp)dp[i]=tmp;}
				}
				if(a[i]==0) {
					x=-1;y=-1;
					if(vec[2*i]==0)x=0;
					if(vec[2*i+1]==0)y=0;
					if(vec[2*i]==1 && dp[2*i]!=-1)x=dp[2*i];
					if(vec[2*i+1]==1 && dp[2*i+1]!=-1)y=dp[2*i+1];
					if(x==-1 || y==-1)tmp=-1;
					else tmp = x+y;
					if(tmp!=-1){if(dp[i]==-1 || dp[i]>tmp)dp[i]=tmp;}
				}
				if(a[i]==0 && c[i]==1) {
					x=-1;y=-1;
					if(vec[2*i]==0)x=0;
					if(vec[2*i+1]==0)y=0;
					if(vec[2*i]==1 && dp[2*i]!=-1)x=dp[2*i];
					if(vec[2*i+1]==1 && dp[2*i+1]!=-1)y=dp[2*i+1];
					//if(x==-1 || y==-1)tmp=-1;
					//else tmp = max(x,y);
					if(x==-1)tmp=y;
					else if(y==-1)tmp=x;
					else {
						tmp = x;if(tmp>y)tmp=y;
					}
					if(tmp!=-1)tmp++;
					if(tmp!=-1){if(dp[i]==-1 || dp[i]>tmp)dp[i]=tmp;}
				}
			}
		}
		fout<<"Case #"<<t<<": ";
		if(dp[1]==-1) {
			fout<<"IMPOSSIBLE"<<endl;
		}
		else fout<<dp[1]<<endl;
	}
	return 0;
}