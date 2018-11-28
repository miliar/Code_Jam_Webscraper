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

string itoa(int n)
{
	char buf[20];
	sprintf(buf,"%d",n);
	return buf;
}

int f(int n, int b)
{
	string s = itoa(n);
	set<int> ans;
	fori(i,sz(s)-1)
	{
		s = s.substr(1) + s[0];
		int test = atoi(s.c_str());
		if(s[0] != '0' && test > n && test <= b)
			ans.insert(test);
	}
	return sz(ans);
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif
	int testCount;
	cin >> testCount;
	for(int testNo = 1; testNo <= testCount; testNo++)
	{
		int a, b;
		cin >> a >> b;
		int ans = 0;
		for(int n = a; n < b; n++)
			ans += f(n,b);
		cout << "Case #" << testNo << ": " << ans << endl;
		cerr << testNo << endl;
	}
}