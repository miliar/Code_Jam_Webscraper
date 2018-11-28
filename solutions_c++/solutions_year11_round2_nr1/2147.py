#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
#define MAXN 102

int Rint() {int x; scanf("%d", &x); return x;}

int team[MAXN][MAXN];		//0 1 -1
int tot[MAXN], win[MAXN];
double wp[MAXN];
double owp[MAXN];
double oowp[MAXN];
int n;

void solve()
{
	for(int i=0; i<n; i++)
		wp[i] = (double)win[i]/tot[i];
	for(int i=0; i<n; i++)
	{
		double cnt=0;
		for(int j=0; j<n; j++)
		{
			if(team[i][j] == 0)
			{
				if(win[j])	cnt+=(double)(win[j]-1)/(tot[j]-1);
				else cnt+=(double)(win[j])/(tot[j]-1);
			}
			else if(team[i][j] == 1)
			{
				cnt+=(double)(win[j])/(tot[j]-1);
			}
		}
		owp[i] = cnt/(double)tot[i];
	}
	for(int i=0; i<n; i++)
	{
		double cnt=0;
		for(int j=0; j<n; j++)
		{
			if(team[i][j] != -1)
			{
				cnt+=owp[j];
			}
		}
		oowp[i] = cnt/(double)tot[i];
	}
}
void print()
{
	for(int i=0; i<n; i++)
	{
		double ans = wp[i]*0.25+owp[i]*0.5+oowp[i]*0.25;
		printf("%.12lf\n", ans);
	}
}
void read()
{
	memset(tot, 0, sizeof(tot));
	memset(win, 0, sizeof(win));
	for(int i= 0; i<n; i++)	//row
	{
		char t[MAXN];
		scanf("%s", t);
		for(int j=0; j<n; j++)
		{
			if(t[j] == '0') {tot[i]++; team[i][j]=0;}
			else if(t[j] == '1') {tot[i]++; win[i]++; team[i][j]=1;}
			else team[i][j] = -1;
		}
	}
}

int main()
{
	int t = Rint();
	for(int i=0; i<t; i++)
	{
		printf("Case #%d:\n", i+1);
		n = Rint();
		read();
		solve();
		print();
	}
}