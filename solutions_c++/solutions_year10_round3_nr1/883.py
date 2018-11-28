#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <cctype>
#include <fstream>
#include <numeric>
#include <map>
#include <iterator>
#include <cstdlib>
#include <cstdio>
using namespace std;

#define INF 99999999
#define EPS 1e-7
#define MIN(a,b) ((a)<(b))?(a):(b)
#define MAX(a,b) ((a)>(b))?(a):(b)
#define REP(i,n) for(i=0; i<(n); i++)
#define FOR(i,a,b) for(i=(a); i<=(b); i++)
#define SET(t,v) memset((t), (v), sizeof(t))
#define sz size()
#define pb push_back
#define i64 long long
#define ALL(x) x.begin(), x.end()


#define SIZE 1000+10

#define IO freopen("A-large.in","r",stdin); freopen("A-large.out","w",stdout);


int T,N;

class building{
public:		
	int a,b;
	building(){
		a=0;
		b=0;
	};
	building(int x,int y){
		a = x;
		b = y;
	}
}H[SIZE];

bool comp(building a, building b)
{
	return (a.a > b.a);
}

int main()
{
	IO
	int tc,i,j,k,cnt;
	scanf("%d",&T);
	for(tc=1;tc<=T;tc++)
	{
		scanf("%d",&N);
		for(i=0;i<N;i++)
		{
			H[i] = building();
			scanf("%d %d",&H[i].a,&H[i].b);
		}
		sort(H,H+N, comp);
		cnt=0;
		for(i=0;i<N;i++)
		{
			for(j=i+1;j<N;j++)
			{
				if(H[j].b > H[i].b)
					cnt++;
			}
		}
		printf("Case #%d: %d\n",tc,cnt);
	}
	return 0;
}

