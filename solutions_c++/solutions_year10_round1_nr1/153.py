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
template<class T> void D(T A[],int n) {for(int i=0;i<n;i++) cout<<A[i]<<" ";cout<<endl;}
template<class T> void D(vector<T> A,int n=-1) {if (n==-1) n=A.size();for(int i=0;i<n;i++) cout<<A[i]<<" ";cout<<endl;}
char mp[101][101];
char nmp[101][101];
int N,K;
void rotate()
{
	fir(i,0,N) fir(j,0,N) nmp[j][(N-1)-i]=mp[i][j];
	memcpy(mp,nmp,sizeof(mp));
}
void gravity()
{
	firre(i,N-1,0) fir(j,0,N)
	{
		int ci=i;
		while(ci>=0 && mp[ci][j]=='.') ci--;
		if (ci>=0) swap(mp[i][j],mp[ci][j]);
	}
}
int di[]={1,0,1,1};
int dj[]={0,1,1,-1};
bool check(int ci,int cj,int k,char ch)
{
	int cnt=0;
	while(ci>=0 && cj>=0 && ci<N && cj<N)
	{
		if (mp[ci][cj]==ch) cnt++;
		else break;
		ci+=di[k];
		cj+=dj[k];
	}
	if (cnt>=K) return true;
	return false;
}
int main() {
	int tc;
	scanf("%d",&tc);int kase=0;
	while(tc--) {
		++kase;
		scanf("%d%d\n",&N,&K);
		fir(i,0,N) {
			gets(mp[i]);
		}
		rotate();
		//fir(i,0,N) puts(mp[i]);
		gravity();
		bool R=0,B=0;
		fir(i,0,N) fir(j,0,N) {
			fir(k,0,4) {
				if (!R)
				R|=check(i,j,k,'R');
				if (!B)
				B|=check(i,j,k,'B');
			}
		}
		printf("Case #%d: ",kase);
		if (!R && !B) puts("Neither");
		if (R && B) puts("Both");
		if (R && !B) puts("Red");
		if (!R && B) puts("Blue");
	}
    return 0;
}