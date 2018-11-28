#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

bool used[1001];
int tc, ntc;
int n;
int ar[1000];

int main()
{
	FILE* fi = fopen("D-large.in", "r");
	FILE* fo = fopen("D-large.out", "w");
	
	fscanf(fi, "%d", &ntc);
	for (tc=1; tc<=ntc; tc++)
	{
		fscanf(fi, "%d", &n);
		int i;
		for (i=0; i<n; i++) 
		{
			fscanf(fi, "%d", &ar[i]);
			ar[i]--;
		}
		
		double res = 0;
		memset(used, 0, sizeof(used));
		for (i=0; i<n; i++) if (!used[i])
		{
			int cnt = 0;
			int x = i;
			while (!used[x])
			{
				used[x] = true;
				cnt++;
				x = ar[x];
			}
			
			if (cnt == 1);
			else res += cnt;
		}
		
		printf("Case #%d: %lf\n", tc, res);
		fprintf(fo, "Case #%d: %lf\n", tc, res);
	}
	
	fclose(fi); fclose(fo);
}