#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <utility>
#include <set>
#include <sstream>
#include <map>
#include <ctime>
#include <cstdlib>
#include <queue>
#define fr(a,b,c) for (a=b;a<=c;a++)
#define frr(a,b,c) for (a=b;a>=c;a--)
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define F first
#define S second
#define oo 1000111222
using namespace std;
typedef long long ll;
const int dx[]={-1,0,1,0,-1,1,1,-1};
      int dy[]={0,1,0,-1,1,1,-1,-1};

int n,re;
vector <int> a;
priority_queue <int> b[10100];

int main()
{
	freopen("blarge.in","r",stdin); freopen("blarge.out","w",stdout);
	int test,it,i,x;
	cin >> test;
	fr(it,1,test)
	{
		cout << "Case #" << it << ": ";
		cin >> n; re=1;
		if (!n)
		{
			cout << 0 << endl;
			continue;
		}
		a.clear();
		fr(i,1,n) scanf("%d",&x), a.pb(x);
		sort(a.begin(),a.end());
		fr(i,0,n-1)
			if (b[a[i]-1].empty()) b[a[i]].push(-1);
			else
			{
				int u=b[a[i]-1].top();
				b[a[i]-1].pop();
				b[a[i]].push(u-1);
			}
		int s=n;
		fr(i,1,10000)
			while (!b[i].empty())
			{
				s=min(s,-b[i].top());
				b[i].pop();
			}
		re=max(re,s);
		cout << re << endl;
	}
   return 0;
}
