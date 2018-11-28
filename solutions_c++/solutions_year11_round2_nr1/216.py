#include <map>
#include <set>
#include <cmath>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;
#define li		long long
#define rep(i,to)	for(li i=0;i<((li)to);i++)
#define pb		push_back
#define sz(v)		((li)v.size())

int main(){
	ifstream ifs("input.txt");
	ofstream ofs("output.txt");
	
	li t,n;
	ifs>>t;
	rep(i,t){
		ifs>>n;
		vector<string> mp;
		rep(j,n){
			string str;
			ifs>>str;
			mp.pb(str);
		}
		double wp[105],owp[105],oowp[105];
		double cnt0[105],cnt1[105],cnt2[105];
		rep(j,105) wp[j]=owp[j]=oowp[j]=0;
		rep(j,105) cnt0[j]=cnt1[j]=cnt2[j]=0;
		rep(j,n)rep(k,n)if(mp[j][k]!='.'){
			if(mp[j][k]=='1') wp[j]+=1;
			cnt0[j]+=1;
		}
		rep(j,n)rep(k,n)if(mp[j][k]!='.'){
			if(mp[j][k]=='1') owp[j]+=wp[k]/(cnt0[k]-1.0);
			else owp[j]+=(wp[k]-1.0)/(cnt0[k]-1.0);
			cnt1[j]+=1;
		}
		rep(j,n)rep(k,n)if(mp[j][k]!='.'){
			oowp[j]+=owp[k]/cnt1[k];
			cnt2[j]++;
		}
		ofs<<"Case #"<<i+1<<":"<<endl;
		rep(j,n) ofs<<wp[j]/cnt0[j]*0.25+0.5*owp[j]/cnt1[j]+0.25*oowp[j]/cnt2[j]<<endl;
	}
}
