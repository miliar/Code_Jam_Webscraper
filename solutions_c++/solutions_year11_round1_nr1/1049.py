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
bool poss(int y, int k1, int x, int k2, long long N)
{
	y -= k1;
	x -= k2;
	if (x == 0 && y == 0) return true;
	if (k1 == 0 && k2 == 0) return true;
	if (k1 == 0) return false;
	if (y == 0) return false;
	return true;
}

int main() {
	int T;
	cin>>T;
	fir(kase, 0, T)
	{
		long long N;int Pg, Pd;
		cin>>N>>Pd>>Pg;
		int den = 100;
		for(int i = 2; i <= 100; i++)
		{
			while(den % i == 0 && Pd % i == 0)
			{
				den /= i;
				Pd /= i;
			}
		}
		int den2 = 100;
		for(int i = 2; i <= 100; i++)
		{
			while(den2 % i == 0 && Pg % i == 0)
			{
				den2 /= i;
				Pg /= i;
			}
		}
		swap(den, den2);
		printf("Case #%d: ", kase + 1);
		if (poss(den, Pg, den2, Pd, N) && den2 <= N)
			printf("Possible\n");
		else printf("Broken\n");
	}
    return 0;
}