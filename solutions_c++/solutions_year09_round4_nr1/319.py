#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int n;
int a[64];
int ans;
int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	
	int i, j, k;
	int tc, t;
	char buf[64];
	int tmp;
	fscanf(fp, "%d", &tc);
	for(t=1;t<=tc;t++)
	{
		fscanf(fp, "%d", &n);
		for(i=1;i<=n;i++)
		{
			fscanf(fp, "%s", &buf[1]);
			a[i]=0;
			for(j=1;j<=n;j++)
			{
				if(buf[j]=='1') a[i]=j;
			}
		}
		ans=0;
		for(i=1;i<=n;i++)
		{
			for(j=i;j<=n;j++)
			{
				if(a[j]<=i) break;
			}
			ans+=j-i;
			tmp=a[j];
			for(k=j;k>i;k--) a[k]=a[k-1];
			a[i]=tmp;
		}
		fprintf(ofp, "Case #%d: %d\n", t, ans);
	}

	fclose(fp);
	fclose(ofp);
	char cmd[128];
	strcpy(cmd, "type ");
	strcat(cmd, outfile);
	system(cmd);
	return 0;
}
