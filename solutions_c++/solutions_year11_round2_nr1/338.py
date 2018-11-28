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
string graph[101];
pair<int, int> wp[101];
double owp[101];
double oowp[101];
int main() {
	int T;
	cin>>T;
	int kase = 0;
	while(T--)
	{
		kase++;
		int N;
		cin>>N;
		fir(i, 0, N) cin>>graph[i];
		memset(wp, 0, sizeof(wp));
		memset(owp, 0, sizeof(owp));
		memset(oowp, 0, sizeof(oowp));
		fir(i, 0, N)
		{
			int tot = 0;
			int win = 0;
			fir(j, 0, N) {
				if (i == j) continue;
				if (graph[i][j] == '.') continue;
				tot++;
				if (graph[i][j] == '1') win++;
			}
			wp[i] = make_pair(win, tot);
		}
		fir(i, 0, N)
		{
			int tot = 0;
			owp[i] = 0;
			fir(j, 0, N)
			{
				if (i == j) continue;
				if (graph[i][j] == '.') continue;
				int ttot = wp[j].second;
				int twin = wp[j].first;
				ttot--;
				if (graph[j][i] == '1')
				twin--;
				owp[i] += (double)twin/(double)ttot;
				tot ++;
			}
			owp[i] /= (double)tot;
		}
		fir(i, 0, N)
		{
			int tot = 0;
			oowp[i] = 0;
			fir(j, 0, N)
			{
				if (i == j || graph[i][j] == '.') continue;
				oowp[i] += owp[j];
				tot++;
			}
			oowp[i] /= tot;
		}
		printf("Case #%d:\n", kase);
		fir(i, 0, N)
		{
			double tval = 0.25*((double)wp[i].first/(double)wp[i].second) + 0.50*owp[i] + 0.25*oowp[i];
			printf("%.6lf\n",tval);
		}
	}
    return 0;
}