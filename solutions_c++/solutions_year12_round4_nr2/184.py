#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}//NOTES:checkmin(
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}//NOTES:checkmax(
#define SIZE(x) ((int)(x).size())
#define for0(i,n) for(int i=0;i<(n);i++)
#define for1(i,n) for(int i=1;i<=(n);i++)
#define for0r(i,n) for(int i=(n)-1;i>=0;i--)
#define for1r(i,n) for(int i=(n);i>=1;i--)
typedef long long ll;

int r[1010];
typedef pair<int,int> PII;
PII c[1010];
int x[1010];
int y[1010];

void solve()
{
	int N,W,L;
	scanf("%d %d %d",&N,&W,&L);
	for0(i,N)
	{
		scanf("%d",&r[i]);
		c[i]=make_pair(r[i],i);
	}
	sort(c,c+N);
	reverse(c,c+N);
	//if(W<L)swap(W,L);
	int w=0,l=0;
	int p=0;
	while(p<N)
	{
		int wt=c[p].first+w;
		l=0;
		x[c[p].second]=w;
		y[c[p].second]=l;
		p++;
		while(p<N && l+c[p-1].first+c[p].first<=L)
		{
			l+=c[p-1].first+c[p].first;
			x[c[p].second]=w;
			y[c[p].second]=l;
			p++;
		}
		if(p<N)
		{
			w=wt+c[p].first;
		}
	}
	for0(i,N)
	{
		printf(" %d %d",x[i],y[i]);
	}
	putchar('\n');
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,Tc=0;
	scanf("%d",&T);
	while(++Tc<=T)
	{
		printf("Case #%d:",Tc);
		solve();
	}
	return 0;
}