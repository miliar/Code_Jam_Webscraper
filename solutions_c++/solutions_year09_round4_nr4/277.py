#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#define INF 1e8
#define max(a, b) (((a)>(b))?(a):(b))
#define min(a, b) (((a)<(b))?(a):(b))
struct circle
{
	double x, y, r;
};
int n;
circle a[8];
double ans;
int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	
	int i, j;
	int tc, t;
	double d;
	fscanf(fp, "%d", &tc);
	for(t=1;t<=tc;t++)
	{
		fscanf(fp, "%d", &n);
		for(i=1;i<=n;i++) fscanf(fp, "%lf%lf%lf", &a[i].x, &a[i].y, &a[i].r);
		fprintf(ofp, "Case #%d: ", t);
		if(n==1) ans=a[1].r;
		else if(n==2) ans=max(a[1].r, a[2].r);
		else
		{
			ans=INF;
			for(i=1;i<=n;i++)
			{
				for(j=i+1;j<=n;j++)
				{
					d=hypot(a[i].x-a[j].x, a[i].y-a[j].y)+a[i].r+a[j].r;
					d/=2.0;
					ans=min(ans, max(d, a[6-i-j].r));
				}
			}
		}
		fprintf(ofp, "%.8lf\n", ans);
	}

	fclose(fp);
	fclose(ofp);
	char cmd[128];
	strcpy(cmd, "type ");
	strcat(cmd, outfile);
	system(cmd);
	return 0;
}
