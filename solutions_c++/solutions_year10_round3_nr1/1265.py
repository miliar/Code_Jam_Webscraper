#include<stdio.h>
#include<map>
#include<string>

using namespace std;
int flag[10005][10005];

int main()
{
	FILE *fin = fopen("INP.IN","r");
	FILE *fout = fopen("OUT.out","w");
	int t;
	fscanf(fin,"%d",&t);
	for(int x = 1; x <= t;x++)
	{
		int counter = 0;
		int n;
		fscanf(fin,"%d",&n);
		int b1[10005];
		int b2[10005];
		for(int i = 0; i < n;i++)
			fscanf(fin,"%d %d",&b1[i],&b2[i]);
		memset(flag,0,sizeof(flag));
		for(int i = 0; i < n; i ++)
		{
			int start = b1[i];
			int end = b2[i];
			for(int j = 0; j < n;j ++)
			{
				if (flag[i][j] == 1)
					continue;
				if (b1[j] > start && b2[j] < end)
				{
					counter ++;
					flag[i][j] = 1;
				}
			}
		}
		fprintf(fout,"Case #%d: %d\n",x,counter);
	}
}