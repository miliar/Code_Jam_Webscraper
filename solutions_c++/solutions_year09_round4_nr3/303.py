#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <algorithm>
#include <vector>
#define MAX 101
using namespace std;

int T,N,K;

struct MM
{
	int x[25];
}mm[100];

int Bipartite(bool vc [][MAX],int nv1,int nv2) {
    int i, j, x, n;
    int q[MAX], prev[MAX], qs, qe;
    int vm1[MAX], vm2[MAX];

    n = 0;
    for( i = 0; i < nv1; i++ ) vm1[i] = -1;
    for( i = 0; i < nv2; i++ ) vm2[i] = -1;
    for( i = 0; i < nv1; i++ ) {
        for( j = 0; j < nv2; j++ ) prev[j] = -2;
        qs = qe = 0;
        for( j = 0; j < nv2; j++ ) if( vc[i][j] ) {
            prev[j] = -1;
            q[qe++] = j;
        }
        while( qs < qe ) {
            x = q[qs];
            if( vm2[x] == -1 ) break;
            qs++;
            for( j = 0; j < nv2; j++ ) if( prev[j] == -2 && vc[vm2[x]][j] ) {
                prev[j] = x;
                q[qe++] = j;
            }
        }
        if( qs == qe ) continue;
        while( prev[x] > -1 ) {
            vm1[vm2[prev[x]]] = x;
            vm2[x] = vm2[prev[x]];
            x = prev[x];
        }
        vm2[x] = i;
        vm1[i] = x;
        n++;
    }
    return n;
}



bool cmp(MM a,MM b)
{
	int i;
	for(i = 0;i < K;i++)
	{
		if(a.x[i] < b.x[i])
			return true;
		if(a.x[i] > b.x[i])
			return false;
	}
	return false;
}

bool ok(MM a,MM b)
{
	int i;
	for(i = 0;i < K;i++)
	{
		if(a.x[i] >= b.x[i])
			return false;
	}
	return true;
}

int main()
{
	int i,j,k,t;
	bool vc[MAX][MAX];
	freopen("C-large.in","r",stdin);
	freopen("C.txt","w",stdout);
	scanf("%d",&T);
	for(t = 1;t <= T;t++)
	{
		scanf("%d%d",&N,&K);
		for(i = 0;i < N;i++)
			for(j = 0;j < K;j++)
				scanf("%d",&mm[i].x[j]);
		sort(mm,mm + N,cmp);
		memset(vc,false,sizeof(vc));
		for(i = 0;i < N;i++)
			for(j = i + 1;j < N;j++)
			{
				if(ok(mm[i],mm[j]))
					vc[i][j] = true;
			}
		int ans = N - Bipartite(vc,N,N);
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
		
					
			
		
		
