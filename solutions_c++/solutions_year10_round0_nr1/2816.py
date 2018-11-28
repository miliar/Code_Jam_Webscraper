#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <cstdlib>
#include <stdlib.h>
#include <stack>
#include <cstdio>
#include <map>
#include <cmath>
#include <time.h>
using namespace std;

#define MAX(a,b) ((a>=b)?a:b)
#define MIN(a,b) ((a<=b)?a:b)
#define ABS(a) ((a<0)?-(a):a)

int main()
{
	//freopen("in.txt","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,n,k;
	scanf("%d",&T);
	for(int t=0;t<T;++t)
	{
		scanf("%d %d",&n,&k);
		k&=((1<<n)-1);
		if(k==((1<<n)-1))printf("Case #%d: ON\n",t+1); else printf("Case #%d: OFF\n",t+1);
	}
	return 0;
}