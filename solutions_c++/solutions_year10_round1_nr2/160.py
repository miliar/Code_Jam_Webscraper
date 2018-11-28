/*
	Author: Imran Khan
*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <cstring>
#include <fstream>
#include <cassert>
using namespace std;
#define all(x) (x).begin(),(x).end()

#define vs vector <string>
#define vi vector <int>
#define p(X) push_back((X))

#define fir(i,j,n) for(int (i)=(j);(i)<(n);(i)++)
#define fire(i,j,n) for(int (i)=(j);(i)<=(n);(i)++)
#define firr(i,j,n) for(int (i)=(j);(i)>(n);(i)--)
#define firre(i,j,n) for(int (i)=(j);(i)>=(n);(i)--)
#define tr(v,it) for(typeof(v.begin()) it=v.begin();it!=v.end();it++)

#define srt(v) sort((v).begin(),(v).end())
#define srtc(v) sort(v.begin(),v.end(),cmp)

#define _bc(i) __builtin_popcount(i)

string lower(string s) {for(int i=0;i<s.size();i++) s[i]=tolower(s[i]);return s;}
vector<string> sep(string s,char c) { string temp;vector<string> res;for(int i=0;i<s.size();i++) { if (s[i]==c) {if (temp!="") res.push_back(temp);temp="";continue;}temp=temp+s[i];}if (temp!="") res.push_back(temp);return res;}
template<class T> T toint(string s)
{
	stringstream ss(s);
	T ret;
	ss>>ret;
	return ret;
}
template<class T> string tostr(T inp)
{
	string ret;
	stringstream ss;ss<<inp;
	ss>>ret;
	return ret;
}
int arr[101];
int dp[101][301][4];
int D,I,M,N;
bool valid(int pval,int nval)
{
	if (pval==-1) return true;
	if (abs(pval-nval)>M) return false;
	return true;
}
int solve(int ind,int pval,int increasing)
{
	if (ind==N) return 0;
	if (dp[ind][pval+1][increasing+1]!=-1) return dp[ind][pval+1][increasing+1];
	int ret=D+solve(ind+1,pval,-1);
	fire(i,0,255) if (valid(pval,i)) {
		if (increasing==1 && i<=pval) continue;
		if (increasing==0 && i>=pval) continue;
		if (increasing==-1)
		{
			if (pval==-1 || i>=pval)
			ret=min(ret,I+solve(ind,i,1));
			if (pval==-1 || i<=pval)
			ret=min(ret,I+solve(ind,i,0));
		} else
		ret=min(ret,I+solve(ind,i,increasing));
	}
	fire(i,0,255) if (valid(pval,i)) ret=min(ret,(abs(i-arr[ind]))+solve(ind+1,i,-1));
	return dp[ind][pval+1][increasing+1]=ret;
}
int main() {
	int tc;
	scanf("%d",&tc);int kase=0;
	while(tc--) {
		++kase;
		cerr<<kase<<endl;
		scanf("%d%d%d%d",&D,&I,&M,&N);
		fir(i,0,N) scanf("%d",&arr[i]);
		memset(dp,-1,sizeof(dp));
		printf("Case #%d: ",kase);
		cout<<solve(0,-1,-1)<<endl;
	}
    return 0;
}