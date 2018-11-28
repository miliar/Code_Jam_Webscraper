#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

struct P {
	int a,b;
} p[1002];

bool compare(P x,P y)
{
	if( x.a!=y.a )
		return (x.a<y.a);
	return (x.b<y.b);
}

int main()
{
//	freopen("A.in","r",stdin);//freopen("A_output.txt","w",stdout);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);

	int _kase,kase=0,i,j,k,l,n;
	scanf("%d",&_kase);
	while( _kase-- )
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf(" %d %d",&p[i].a,&p[i].b);
		}
		sort(&p[0],&p[n],compare);

		k=0;
		for(i=0;i<n;i++)
		{
			for(j=i+1;j<n;j++)
			{
				if( p[i].b >= p[j].b )
					k++;
			}
		}

		printf("Case #%d: %d\n",++kase,k);
	}
	return 0;
}