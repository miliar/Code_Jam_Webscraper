#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<memory.h>
int n, m;
int a[32][32];
bool w[32][32];
int v[32];
int ans;
void f1(int x);
void f2(int x, int cur)
{
	v[cur]=x;
	int i;
	bool flag=false;
	for(i=cur+1;i<=n;i++)
	{
		if(v[i] || w[cur][i]) continue;
		flag=true;
		f2(x, i);
	}
	if(!flag) f1(x+1);
	v[cur]=false;
}
void f1(int x)
{
	if(ans<=x-1) return;
	int i;
	for(i=1;i<=n && v[i];i++);
	if(i>n){ans=x-1; return;}
	f2(x, i);
}
int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int i, j, k;
	int tmp;
	int tc, t;
	bool flag1, flag2, flag3;
	fscanf(fp, "%d", &tc);
	for(t=1;t<=tc;t++)
	{
		fscanf(fp, "%d%d", &n, &m);
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=m;j++) fscanf(fp, "%d", &a[i][j]);
		}
		for(i=1;i<=n;i++)
		{
			for(j=i+1;j<=n;j++)
			{
				if(a[i][1]>a[j][1])
				{
					for(k=1;k<=m;k++)
					{
						tmp=a[i][k]; a[i][k]=a[j][k]; a[j][k]=tmp;
					}
				}
			}
		}
		memset(w, false, sizeof(w));
		for(i=1;i<=n;i++)
		{
			for(j=i+1;j<=n;j++)
			{
				flag1=flag2=flag3=false;
				for(k=1;k<=m;k++)
				{
					if(a[i][k]>a[j][k]) flag1=true;
					if(a[i][k]<a[j][k]) flag2=true;
					if(a[i][k]==a[j][k]) flag3=true;
				}
				if((flag1 && flag2) || flag3) w[i][j]=w[j][i]=true;
			}
		}
		memset(v, 0, sizeof(v));
		ans=n;
		f1(1);
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
