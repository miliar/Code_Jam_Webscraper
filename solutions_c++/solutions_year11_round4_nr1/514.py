/*
ID: imranka1
PROG: test
LANG: C++
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
//#define cin fin
//#define cout fout
int main() {
	int T;
	cin>>T;
	int kase = 0;
	while(T--)
	{
		kase++;
		int X, S, R, t, N;
		cin>>X>>S>>R>>t>>N;
		double tleft = t;
		vector<pair<int, pair<int, int> > > speeder;
		fir(i, 0, N)
		{
			int b, e, s;
			cin>>b>>e>>s;
			speeder.p(make_pair(s, make_pair(b, e)));
			X -= (e - b);
		}
		srt(speeder);
		double ans = 0;
		double ttim = (X/((double)R));
		ttim = min(ttim, tleft);
		ans += ttim;
		ans += ((double)X - (double)R*ttim)/(double)S;
		tleft -= ttim;
		fir(i, 0, speeder.size())
		{
			double ttim = ((double)speeder[i].second.second - speeder[i].second.first)/((double)R + speeder[i].first);
			ttim = min(ttim, tleft);
			tleft -= ttim;
			ans += ttim;
			double rdist = ((double)speeder[i].second.second - speeder[i].second.first) - (ttim * (R + speeder[i].first));
			ans += (rdist/((double)S + speeder[i].first));
		}
		printf("Case #%d: ", kase);
		printf("%.7lf\n", ans);
	}
    return 0;
}