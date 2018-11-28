/*
ID: mythic_1
PROG: c
LANG: C++
*/

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <complex>
#include <cctype>
#include <algorithm>
#include <functional>
#include <cmath>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <valarray>
#include <set>
#ifdef _MSC_VER
#include <hash_set>
#include <hash_map>
using namespace stdext;
#else
#if __GNUC__ > 2
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
#else
#include <hash_set>
#include <hash_map>
#endif
#endif

template<class key>
struct hashtemp
{

	enum
	{
		bucket_size = 4, min_buckets = 8
	};
	virtual size_t operator()(const key &p) const=0;

};
using namespace std;

#define fo(i,n) for(i=0;i<(n);++i)

typedef vector<int> vi ;
typedef vector<string> vs ;
typedef vector<double> vd ;
#define sz(x) ((int)(x).size())
#define all(x) x.begin(),x.end()
#define pb(x) push_back(x)
typedef long long ll;
#define SMALL
//#define LARGE
int ar[500][500];
int ar2[500][500];
bool update() {
	memset(ar2,0,sizeof ar2);
	bool a = 0;
	for(int i = 1 ; i < 500; i++)
	{

		for(int j = 1 ; j < 500 ; j++)
		{

			if(ar[i][j-1]==1&&ar[i-1][j]==1)
				a=1,ar2[i][j]=1;
			if(ar[i][j]==1&&(ar[i][j-1]==1||ar[i-1][j]==1))
				a=1,ar2[i][j]=1;
		}
	}
	memcpy(ar,ar2,sizeof ar);
	return a;
}
int main()
{
#ifdef SMALL
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("C-large.in","rt",stdin);
	freopen("C-large.out","wt",stdout);
#endif
	int r,tt,t=0 ;
	scanf("%d",&tt);
	int x1,x2,y1,y2;

	while(tt--)
	{
		scanf("%d",&r);
		memset(ar,0,sizeof ar);
		for(int i = 0 ; i < r ; i++)
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for(int x = x1 ; x<=x2 ; x++)
				for(int y = y1 ; y<=y2 ; y++)
					ar[x][y]=1;
		}
		int c = 0;
		while(update())c++;

		printf("Case #%d: %d\n",++t,c+1);

	}



	return 0;
}
