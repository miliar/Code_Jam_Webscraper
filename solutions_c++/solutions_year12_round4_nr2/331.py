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

inline bool inters (int a, int b, int c, int d) {
	if (a > b)  swap (a, b);
	if (c > d)  swap (c, d);
	return max(a,c) < min(b,d);
}

struct human
{
	int r, index;
	bool operator < (const human &h)const
	{
		return r < h.r;
	}
};

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
		cout << "Case #" << testNo << ": ";

		int n, w, l;
		cin >> n >> w >> l;
		vector<human> h(n);
		vector<ii> ans(n,ii(-1,-1));
		fori(i,n)
		{
			cin >> h[i].r;
			h[i].index = i;
		}
		stable_sort(h.rbegin(),h.rend());
		int prev = -1;
		int x;
		fori(i,n)
		{
			if(prev == -1)
				x = 0;
			else
				x = prev+h[i].r;
			if(x > w)
			{
				i--;
				prev = -1;
				continue;
			}/**/
			prev = x+h[i].r;
			if(prev >= w)
				prev = -1;
			int ma = -1;
			fori(j,n)
				if(ans[h[j].index].first != -1)
					if(inters(x-h[i].r,x+h[i].r,ans[h[j].index].first-h[j].r,ans[h[j].index].first+h[j].r))
						ma = max(ma,ans[h[j].index].second+h[j].r);
			int y;
			if(ma == -1)
				y = 0;
			else
				y = ma+h[i].r;
			ans[h[i].index] = ii(x,y);
		}
		fori(i,n)
			cout << ans[i].first << ' ' << ans[i].second << ' ';
		cout << endl;
	}
}