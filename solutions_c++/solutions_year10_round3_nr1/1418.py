#include <stdio.h>



int main(int argc, char* argv[])
{
	FILE* is = freopen(argv[1], "r", stdin);
	FILE* os = freopen(argv[2], "w", stdout);

	int t;

	scanf("%d", &t);
	
	int ai[10000];
	int bi[10000];
	
	for (int i = 1; i<=t; i++)
	{
		int n;
		
		scanf("%d",&n);
		

		for (int j = 0; j<n; j++)
		{
			scanf("%d", &ai[j]);
			scanf("%d", &bi[j]);			
		}
		
		__int64 s = 0;
		
		for (int m = 0; m<n; m++)
			for (int p = m+1; p<n; p++)
			{
				if ( ((ai[m]<ai[p])&&(bi[m]>bi[p])) || ((ai[m]>ai[p])&&(bi[m]<bi[p])) )   s++;
			}

		printf("Case #%d: %I64d\n", i, s);
	}

	
	fclose(is);
	fclose(os);
	return 0;
}