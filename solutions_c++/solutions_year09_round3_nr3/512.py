#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <string>
#include <vector>
#include <math.h>
#include <queue>
#include <stack>
#include <map>

#define abs(a) (a>=0)?a:(-a)

using namespace std;
int P,Q,N,mark[200];
int rec(int x)
{
	int cnt,i;
	cnt=0;
	mark[x]=0;
	for (i=x+1; i<P; i+=1)
	{
		if (mark[i]==0) break;
		else cnt++;
	}
	for (i=x-1; i>=0; i-=1)
	{
		if (mark[i]==0) break;
		else cnt++;
	}
	return cnt;
}
int main()
{
	int ans,cnt,a[200],i,j,k;
	FILE * pf = fopen("C-small.in","r");
	FILE * rf = fopen("cans.in","w");
	fscanf (pf,"%d",&N);
	for (i=0; i<N; i+=1)
	{
		fscanf (pf,"%d",&P);
		fscanf (pf,"%d",&Q);
		for (j=0; j<Q; j+=1)
		{
			fscanf (pf,"%d",&a[j]);
		}
		j=0;
		ans=10000000;
		do
		{
			cnt=0;
			for (k=0; k<P; k+=1)
			{
				mark[k]=1;
			}
			for (k=0; k<Q; k+=1)
			{
				cnt+=rec(a[k]-1);
			}
			if (cnt<ans) ans=cnt;
			
		}while (next_permutation(a,a+Q));
		fprintf(rf,"Case #%d: %d\n",i+1,ans);
	}
	return 0;
}
