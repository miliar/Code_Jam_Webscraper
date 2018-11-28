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
#define abs(x) (((x)<0)?(-(x)):(x))
using namespace std;

typedef __int64 stt;

struct qdat
{
	stt s;
	int d, h;
	friend bool operator < (qdat d1, qdat d2)
	{
		return d1.h>d2.h;
	}
};

int n, m, r, sz;
char a[16][16];
priority_queue<qdat> q;
set<stt> chk;
stt goal;
int dx[5]={0, -1, 0, 0, 1};
int dy[5]={0, 0, -1, 1, 0};
int gx[6], gy[6];
int ans;

int h(stt s)
{
	int i, j;
	int x, y;
	int tmp;
	int ret=0;
	for(i=r;i>=1;i--)
	{
		tmp=s%sz; s/=sz;
		x=tmp/m; y=tmp%m;
		tmp=99999;
		for(j=1;j<=r;j++) tmp=min(tmp, abs(x-gx[j])+abs(y-gy[j]));
		ret+=tmp;
	}
	return ret;
}
bool f_conflict(int *x, int *y, int k)
{
	int i;
	for(i=1;i<=r;i++)
	{
		if(i==k) continue;
		if(x[i]==x[k] && y[i]==y[k]) return true;
	}
	return false;
}
bool f_connected(int *x, int *y)
{
	int i, j, k;
	bool v[6]={false, };
	v[1]=true;
	bool flag;
	while(true)
	{
		flag=false;
		for(i=1;i<=r;i++)
		{
			if(!v[i]) continue;
			for(j=1;j<=r;j++)
			{
				if(v[j]) continue;
				for(k=1;k<=4;k++)
				{
					if(x[j]==x[i]+dx[k] && y[j]==y[i]+dy[k]){v[j]=flag=true; break;}
				}
			}
		}
		if(!flag) break;
	}
	for(i=1;i<=r && v[i];i++);
	return i>r;
}
void f_insert(int *x, int *y, int dat)
{
	int i;
	int is[6];
	stt s=0;
	for(i=1;i<=r;i++) is[i]=x[i]*m+y[i];
	sort(&is[1], &is[r+1]);
	for(i=1;i<=r;i++) s=s*sz+is[i];
	set<stt>::iterator it=chk.find(s);
	if(it!=chk.end()) return;
	qdat nq;
	nq.s=s; nq.d=dat; nq.h=dat+h(nq.s);
	q.push(nq);
}

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int t, tc;
	int i, j;
	stt cur, nxt;
	qdat cq, nq;
	int x[6], y[6];
	int tmp;
	int d1, d2;
	int nx1, ny1, nx2, ny2;
	int tx1, ty1, tx2, ty2;
	int bx1, by1, bx2, by2;
	fscanf(fp, "%d", &tc);
	for(t=1;t<=tc;t++)
	{
		if(t==5)
			t=t;
		nxt=goal=0;
		fscanf(fp, "%d%d", &n, &m); r=0;
		sz=n*m;
		for(i=0;i<n;i++)
		{
			fscanf(fp, "%s", &a[i][0]);
			for(j=0;j<m;j++)
			{
				if(a[i][j]=='o'){nxt=nxt*sz+m*i+j; a[i][j]='.';}
				if(a[i][j]=='x'){goal=goal*sz+m*i+j; a[i][j]='.'; r++; gx[r]=i; gy[r]=j;}
				if(a[i][j]=='w'){nxt=nxt*sz+m*i+j; goal=goal*sz+m*i+j; a[i][j]='.'; r++; gx[r]=i; gy[r]=j;}
			}
		}
		while(!q.empty()) q.pop();
		chk.clear();
		nq.s=nxt; nq.d=0; nq.h=h(nxt); q.push(nq);
		ans=-1;
		while(!q.empty())
		{
			cq=q.top(); q.pop();
			if(chk.find(cq.s)!=chk.end()) continue;
			chk.insert(cq.s);
			if(cq.s==goal){ans=cq.d; break;}
			for(i=r;i>=1;i--)
			{
				tmp=cq.s%sz; cq.s/=sz;
				x[i]=tmp/m; y[i]=tmp%m;
			}
			for(i=1;i<=r;i++)
			{
				for(d1=1;d1<=4;d1++)
				{
					nx1=x[i]+dx[d1]; ny1=y[i]+dy[d1];
					bx1=x[i]-dx[d1]; by1=y[i]-dy[d1];
					tx1=x[i]; ty1=y[i];
					if(0<=bx1 && 0<=by1 && bx1<n && by1<m)
					{
						if(a[bx1][by1]=='#') continue;
						x[i]=bx1; y[i]=by1;
						if(f_conflict(x, y, i)){x[i]=tx1; y[i]=ty1; continue;}
						x[i]=tx1; y[i]=ty1;
					}
					if(nx1<0 || ny1<0 || nx1>=n || ny1>=m) continue;
					if(a[nx1][ny1]=='#') continue;
					x[i]=nx1; y[i]=ny1;
					if(f_conflict(x, y, i)){x[i]=tx1; y[i]=ty1; continue;}
					if(f_connected(x, y)) f_insert(x, y, cq.d+1);
					for(j=1;j<=r;j++)
					{
						for(d2=1;d2<=4;d2++)
						{
							if(i==j && d1+d2==5) continue;
							nx2=x[j]+dx[d2]; ny2=y[j]+dy[d2];
							bx2=x[j]-dx[d2]; by2=y[j]-dy[d2];
							tx2=x[j]; ty2=y[j];
							if(0<=bx2 && 0<=by2 && bx2<n && by2<m)
							{
								if(a[bx2][by2]=='#') continue;
								x[j]=bx2; y[j]=by2;
								if(f_conflict(x, y, j)){x[j]=tx2; y[j]=ty2; continue;}
								x[j]=tx2; y[j]=ty2;
							}
							if(nx2<0 || ny2<0 || nx2>=n || ny2>=m) continue;
							if(a[nx2][ny2]=='#') continue;
							x[j]=nx2; y[j]=ny2;
							if(f_conflict(x, y, j)){x[j]=tx2; y[j]=ty2; continue;}
							if(f_connected(x, y)) f_insert(x, y, cq.d+2);
							x[j]=tx2; y[j]=ty2;
						}
					}
					x[i]=tx1; y[i]=ty1;
				}
			}
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
