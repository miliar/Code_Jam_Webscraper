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
map<int, int> pfact[1001];
vector<pair<int, int> > sum;
int main() {
	int T;
	cin>>T;
	int kase = 0;
	pfact[1][1] = 1;
	fir(i, 2, 1001) {
		int ci = i;
		int tsum = 0;
		fir(j, 2, i)
		{
			while(ci % j == 0) {pfact[i][j]++; ci /= j;tsum++;}
		}
		if (ci > 1) {pfact[i][ci] = 1;tsum++;}
		sum.p(make_pair(tsum, i));
	}
	srt(sum);
	reverse(all(sum));
	//fir(i, 0, sum.size()) cout<<sum[i].first<<" "<<sum[i].second<<endl;
	while(T--)
	{
		kase++;
		int N;
		cin>>N;
		int ans = 1;
		map<int, int> hav;
		fire(i, 2, N)
		{
			bool tneed = 0;
			tr(pfact[i], it)
			{
				if (it->second > hav[it->first])
				{
					tneed = 1;
					hav[it->first] = it->second;
				}
			}
			if (tneed) ans++;
		}
		hav.clear();
		fire(i, 2, N)
		{
			bool prm = true;
			fir(j, 2, i) if (i % j == 0) prm = false;
			if (prm) ans--;
		}
		if (N == 1)
			printf("Case #%d: %d\n", kase, 0);
		else
			printf("Case #%d: %d\n", kase, abs(ans));
	}
    return 0;
}