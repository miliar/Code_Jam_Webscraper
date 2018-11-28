#include <iostream>
#include <cstdio>

using namespace std;

int intersect(int x1, int y1, int x2, int y2)
{
	if(x1>x2 && y1<y2) return 1;
	if(x1<x2 && y1>y2) return 1;
	return 0;
}

int main()
{
	//freopen("test_a.txt","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int cas, maxcas;
	int i, j, n, sol;
	int x[1010], y[1010];
	
	scanf("%d\n",&maxcas);

	for(cas = 1; cas <= maxcas; cas++) {
		scanf("%d\n",&n);
		for(i=0; i<n; i++) scanf("%d %d\n",&x[i],&y[i]);
		sol = 0;

		for(i=0; i<n-1; i++) 
			for(j=i+1; j<n; j++) 
				sol += intersect(x[i],y[i],x[j],y[j]);
			

		printf("Case #%d: %d\n",cas,sol);

	}

	return 0;
}