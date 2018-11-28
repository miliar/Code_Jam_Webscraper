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

int d, n;
vector<ii> a;
vector<int> x, h;
vector<int> len;

bool ok;

int main() 
{ 
#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
	int testCnt;
	cin >> testCnt;
	for(int testNo = 1; testNo <= testCnt; testNo++)
	{
		cin >> n;
		a.resize(n);
		fori(i,n)
		{
			cin >> a[i].first >> a[i].second;
		}
		ok = false;
		sort(all(a));
		x.resize(n);
		h.resize(n);
		fori(i,n)
		{
			x[i] = a[i].first;
			h[i] = a[i].second;
		}
		cin >> d;
		len.assign(n,0);
		cout << "Case #" << testNo << ": ";

		len[0] = x[0];

		fori(i,n)
		{
			if(x[i]+len[i] >= d)
				ok = true;
			for(int j = i+1; j < n; j++)
			{
				if(x[i]+len[i] >= x[j])
				{
					int nlen;
					if(h[j] >= x[j]-x[i])
						nlen = x[j]-x[i];
					else
						nlen = h[j];
					len[j] = max(len[j],nlen);
				}
				else
					break;
			}
		}

		if(ok)
			cout << "YES";
		else
			cout << "NO";
		cout << endl;
	}
}