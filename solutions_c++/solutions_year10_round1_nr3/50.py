#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <complex>

#define mp make_pair
#define pb push_back
#define sqr(x) ((x)*(x))
#define foreach(it,c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;
typedef long long LL;
typedef complex<double> Point;

template<typename T> inline int size(const T &a) { return a.size(); }
template<typename T> inline bool operator<(const int &a,const vector<T> &b) { return a<b.size(); }

int bord[1000005];

bool check(int a,int b)
{
	if(a>b) swap(a,b);
	return b>bord[a];
}

void precalc(void)
{
	bord[1] = 1;
	for(int i=2;i<=1000000;i++)
	{
		for(int s = max(i,bord[i-1]);;s++)
		{
			bord[i] = s;
			for(int tmp = s-i; tmp >= 0; tmp -= i)
			{
				if(check(i,tmp) == false)
				{
					bord[i] = s-1;
					break;
				}
			}
			if(bord[i] != s) break;
		}
	}
}

bool process(void)
{
	int a1,a2,b1,b2;
	LL ret = 0;
	scanf("%d %d %d %d",&a1,&a2,&b1,&b2);
	for(int i=a1;i<=a2;i++)
	{
		int lo = max(bord[i],b1-1);
		if(lo > b2) break;
		ret += (b2 - lo);
	}
	for(int i=b1;i<=b2;i++)
	{
		int lo = max(bord[i],a1-1);
		if(lo > a2) break;
		ret += (a2 - lo);
	}
	cout << ret << endl;
	return true;
}

int main(void)
{
	precalc();
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		process();
	}
	return 0;
}

