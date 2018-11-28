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
string sheet[512];
int main() {
	int T;
	cin>>T;
	int kase = 0;
	while(T--)
	{
		kase++;
		int R, C, D;
		cin>>R>>C>>D;
		fir(i, 0, R)
		{
			cin>>sheet[i];
		}
		int mxsize = min(R, C);
		int ans = -1;
		for(int k = 3; k <= mxsize; k ++) fir(i1, 0, R) fir(j1, 0, C)
		{
			int i2 = i1 + k - 1;
			int j2 = j1 + k - 1;
			if (i2 >= R || j2 >= C) continue;
			int ci = (i1 + i2);
			int cj = (j1 + j2);
			int x = 0, y = 0;
			fire(i, i1, i2) fire(j, j1, j2)
			{
				if (i == i1 && j == j1) continue;
				if (i == i1 && j == j2) continue;
				if (i == i2 && j == j1) continue;
				if (i == i2 && j == j2) continue;
				x += (2 * i - ci) * (sheet[i][j] - '0' + D);
				y += (2 * j - cj) * (sheet[i][j] - '0' + D);
			}
			if (x == 0 && y == 0) ans = max(ans, k);
		}
		printf("Case #%d: ", kase);
		if (ans == -1)
			puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}
    return 0;
}