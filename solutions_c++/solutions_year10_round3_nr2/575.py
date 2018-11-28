#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <cmath>

using namespace std;

map < pair <int, int >, int > mp;

int f2(int L,int P, int z){

	if(L>=P) return 0;
	if(L*z>=P) return 0;
	//if(mp.count(make_pair(L,P)) > 0) return mp[make_pair(L,P)];
	int a = floor(sqrt(double(L)*double(P)));
	int b = max( f2(L,a,z) , f2(a,P,z)) + 1;
	int q = 100000; //max( f(L,a-1,z),f(a-1,P,z)) + 1;
	int d = 100000;//max(f(L,a+1,z), f(a+1,P,z)) + 1;
	int e = min(min(b,q),d);
	//mp[make_pair(L,P)] = e;
	return e;	
}



int f(int L,int P,int z){
	if(L>=P) return 0;
	if(L*z>=P) return 0;
	if(mp.count(make_pair(L,P)) > 0) return mp[make_pair(L,P)];
	int a = floor(sqrt(double(L)*double(P)));
	int b=10000;
	if (a!=L) b = max( f(L,a,z) , f(a,P,z)) + 1;
	int q=100000;
	if(a-1>L) q = max( f(L,a-1,z),f(a-1,P,z)) + 1;
	int d = 100000;
	if(a+1<P)  d = max(f(L,a+1,z), f(a+1,P,z)) + 1;
	int e = min(min(b,q),d);
	mp[make_pair(L,P)] = e;
	return e;	
}
int dp[2000][2000];
void initialize(int n){
	for(int i=0;i<n;i++)
		for(int j=0;j<n;j++) dp[i][j]=-1;

}
int f3(int L,int P,int z){
	
	if(L*z>=P) return 0;
	if(dp[L][P] != -1) return dp[L][P];
	int mn = 100000;
	int a = floor(sqrt(double(L)*double(P)));
	int tt = max(L+1,a-5);
	int rr = min(P-1,a +5);
	for(int i=tt;i<=rr;i++){

		int x = max(f3(L,i,z),f3(i,P,z))+1;
		mn = min(mn,x);
	}
	dp[L][P] = mn;
	return dp[L][P];	
}
int main(){
	ifstream fin;
	fin.open("B-small-attempt2.in");
	ofstream fout;
	fout.open("b.out");
	int nCases;
	fin >> nCases;
	for(int testCase = 0;testCase < nCases; testCase++){
		int L,P,C;
		fin >> L >> P >> C;
		initialize(P+5);
		int ans = f3(L,P,C);
		fout  <<"Case #" << testCase+1 << ": " << ans << endl;
	}

	return 0;
}