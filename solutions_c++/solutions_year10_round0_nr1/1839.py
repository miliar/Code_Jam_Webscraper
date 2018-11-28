#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <set>
#include <list>
#include <queue>
#include <memory.h>
#include <stdio.h>
#include <time.h>
 
using namespace std;
 
#define ABS(a) ((a>0)?a:-(a))
#define MIN(a,b) ((a<b)?(a):(b))
#define MAX(a,b) ((a<b)?(b):(a))
#define FOR(i,a,n) for (int i=(a);i<(n);++i)
#define FI(i,n) for (int i=0; i<(n); ++i)
#define pnt pair <int, int>
#define mp make_pair
#define PI 3.14159265358979
#define MEMS(a,b) memset(a,b,sizeof(a))
#define LL long long
#define U unsigned
int a[35];
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.txt","w",stdout);
	a[1]=1;
	FOR(i,2,31)
		a[i]=a[i-1]*2+1;
	int t;
	scanf("%d",&t);
	FOR(it,0,t)
	{
		int n,k;
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",it+1);
		if (k%(a[n]+1)==a[n])
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}