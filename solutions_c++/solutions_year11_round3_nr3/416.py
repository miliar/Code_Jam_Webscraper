#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

#define MAX 10010

int v[MAX];

int main()
{
	int cas, casos;
	int i, j, achei;
	int n, h, l;
	
	scanf("%d", &casos);
	
	for (cas = 1; cas <= casos; cas++)
	{
		printf("Case #%d: ", cas);
	
		scanf("%d %d %d", &n, &l, &h);
		
		for (i=0; i<n; i++)
			scanf("%d", &v[i]);
		
		achei = 0;
		for (i=l; i<=h; i++)
		{
			for (j=0; j<n; j++)
			{
				if (v[j]%i!=0 && i%v[j]!=0)
					break;
			}
			if (j==n)
			{
				achei = 1;
				break;
			}
		}
		if (achei)
			printf("%d\n", i);
		else
			printf("NO\n");
		
	
	}
	
	return 0;
}
