#pragma comment(linker,"/STACK:300000000")
#define _CRT_SECURE_NO_WARNINGS
#pragma warning(disable:4800)

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
#include <iomanip>
#include <memory.h>
#include <cstdio>
#include <sstream>
#include <deque>
#include <bitset>
#include <numeric>
#include <ctime>
#include <queue>

using namespace std;

#define show(x) cout << #x << " = " << (x) << endl;
#define fori(i,n) for(int i = 0; i < (n); i++)
#define forab(i,a,b) for(int i = (a); i <= (b); i++)
#define sz(v) int((v).size())
#define all(v) (v).begin(),(v).end()
const double pi = 3.1415926535897932384626433832795;
template<class T> T abs(const T &a) { return a >= 0 ? a : -a; };
template<class T> T sqr(const T &x) { return x * x; }
typedef pair<int,int> ii;
typedef long long ll;
///////////////////////////////////////

char ma[256];

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif
   string s1, s2, x;
   while(cin >> x, x != "#")
	   s1 += x;
   while(cin >> x, x != "#")
	   s2 += x;
   fori(i,sz(s1))
	   ma[s1[i]] = s2[i];
   ma['z'] = 'q';
   ma['q'] = 'z';
   int n;
   cin >> n;
   string s;
   getline(cin,s);
   fori(test,n)
   {	   
	   getline(cin,s);
	   fori(i,sz(s))
		   if(s[i] != ' ')
			   s[i] = ma[s[i]];
	   cout << "Case #" << test+1 << ": " << s << endl;
   }
}