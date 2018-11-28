/*
 * C.cpp
 *
 *  Created on: Sep 3, 2009
 *      Author: Yasser
 */


#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<sstream>
#include<cstdio>
#include<cmath>
#include<stack>
#include<complex>

using namespace std;

string str = "welcome to code jam";
string s = "";

int dp[550][20];

int fun(int ind,int i){
	if(i == str.size())return 1;
	if(ind == s.size())return 0;

	if(dp[ind][i]!= -1)return dp[ind][i];
	int r=0;
	if(i<str.size() && s[ind] == str[i])
		r = (fun(ind+1,i+1))%10000;
	r += fun(ind+1,i);
	return dp[ind][i] = r%10000;
}


int main(){
	freopen("in.in","rt",stdin);
	freopen("in.txt","wt",stdout);
	int n;
	cin>>n;
	getline(cin,s);
	for(int i=0;i<n;i++){
		getline(cin,s);
		memset(dp,-1,sizeof dp);
		int sol = fun(0,0);
		printf("Case #%d: %04d\n",i+1,sol);
	}


	return 0;
}
