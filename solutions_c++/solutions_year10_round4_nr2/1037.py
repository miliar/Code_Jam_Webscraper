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
//int miss[(1<<11)+100];
bool cost[(1<<11)+100];
int getnn(int nc) {
	int tm=1,nn=1;
	while(tm*2<nc) {tm*=2;nn+=tm;}
	return nn;
}
int main() {
	int tc;
	scanf("%d",&tc);int kase=0;
	while(tc--) {
		++kase;
		int P;scanf("%d",&P);
		int ub=1<<P;
		int nc=getnn(ub);
		memset(cost,0,sizeof(cost));
		fir(i,0,ub) {
			int th;scanf("%d",&th);
			int tind=nc+i+1;
			tind/=2;
			while(tind>=1) {
				if (th<=0) cost[tind]=1;
				else th--;
				tind/=2;
			}
		}
		int tmp;
		ub--;
		fir(i,0,ub) scanf("%d",&tmp);
		int ans=0;
		fir(i,0,nc+100) if (cost[i]) ans++;
		cout<<"Case #"<<kase<<": "<<ans<<endl;
	}
    return 0;
}