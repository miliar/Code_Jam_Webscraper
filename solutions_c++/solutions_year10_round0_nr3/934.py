#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define max(a, b) (((a)>(b))?(a):(b))
#define min(a, b) (((a)<(b))?(a):(b))
using namespace std;

long long r, m;
int n;
long long a[2048];
long long b[2048];
int v[2048];
long long vtot[2048];
int nxt[2048];
long long tot;
long long ans;

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int i, j, k;
	int t, tc;
	long long psum, clen, ctot;
	int cst;
	fscanf(fp, "%d", &tc);
	for(t=1;t<=tc;t++)
	{
		fscanf(fp, "%lld%lld%d", &r, &m, &n);
		tot=0;
		for(i=1;i<=n;i++){fscanf(fp, "%lld", &a[i]); a[n+i]=a[i]; tot+=a[i];}
		fprintf(ofp, "Case #%d: ", t);
		if(tot<=m){fprintf(ofp, "%lld\n", tot*r); continue;}
		for(i=j=1, psum=0;i<=n;i++)
		{
			for(;psum+a[j]<=m;j++) psum+=a[j];
			nxt[i]=j; b[i]=psum;
			if(nxt[i]>n) nxt[i]-=n;
			psum-=a[i];
		}
		memset(v, 0, sizeof(v));
		ans=0; clen=1; ctot=0;
		for(k=1, i=1, tot=0;r;k++)
		{
			tot+=b[i];
			if(v[i]){clen=k-v[i]; ctot=tot-vtot[i]; cst=i; break;}
			v[i]=k; vtot[i]=tot; ans+=b[i]; r--; i=nxt[i];
		}
		ans+=(long long)(r/clen)*ctot;
		r%=clen;
		for(i=cst;r--;){ans+=b[i]; i=nxt[i];}
		fprintf(ofp, "%lld\n", ans);
	}
	
	fclose(fp);
	fclose(ofp);
	char cmd[128];
	strcpy(cmd, "type ");
	strcat(cmd, outfile);
	system(cmd);
	return 0;
}
