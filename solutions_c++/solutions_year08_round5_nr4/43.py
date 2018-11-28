#include <vector>
#include <algorithm>
using namespace std;
#include <stdio.h>
#include <string.h>

FILE *Fin = fopen("D-small-attempt0.in","r");
FILE *Fou = fopen("d.out","w");
//FILE *Fin = stdin;
//FILE *Fou = stdout;

int n,m,c;
int x[20], y[20];

#define MOD 10007



int C(int n, int m)
{
	int cc = n/MOD - (m/MOD) - (n-m)/MOD;
	if (cc>0) return 0;

	int up, down, i,j;
	up = 1;
	if ( (n/MOD) %2 !=0 ) up = MOD-1;
	for (i=1; i<=n%MOD; i++)
		up = up*i % MOD;
	down = 1;

	if ( (m/MOD) %2 !=0 ) down = down*(MOD-1)%MOD;
	if ( ((n-m)/MOD) %2 !=0 ) down = down*(MOD-1)%MOD;
	for (i=1; i<=m%MOD; i++)
		down = down*i % MOD;
	for (i=1; i<=(n-m)%MOD; i++)
		down = down*i % MOD;
	for (j=0; j<MOD; j++)
		if (down*j%MOD==up)
			return j;
	fprintf(stderr,"ERROR\n");
	return 0;
}

int get(int n, int m)
{
	if (n>m) swap(n,m);
	int x = m-n;
	int y = n-x;
	if (y<0 || y%3!=0) return 0;
	x += y/3;
	y/=3;
	return C(x+y, x);
}

int main()
{
	int i,j,k,caseN;
	fscanf(Fin,"%d",&caseN);
	for (int t=1; t<=caseN; t++)
	{
		fscanf(Fin,"%d%d%d",&n,&m,&c);
		for (i=0; i<c; i++)
		{
			fscanf(Fin,"%d%d",x+i,y+i);
		}

		int tot = 0;
		for (i=0; i<(1<<c); i++)
		{
			int mask = 0;
			for (j=0; j<c; j++)
				if (i&(1<<j)) mask++;
			vector<pair<int, int> > lst;
			lst.push_back(make_pair(1,1));
			lst.push_back(make_pair(n,m));
			for (j=0; j<c; j++)
				if (i&(1<<j))
					lst.push_back(make_pair(x[j], y[j]));
			sort(lst.begin(), lst.end());
			bool okay = true;

			for (j=0; j+1<lst.size(); j++)
				if (lst[j].second>lst[j+1].second)
					okay = false;
			if (okay)
			{
				int ans = 1;
				for (j=0; j+1<lst.size(); j++)
				{
					ans *= get(lst[j+1].first-lst[j].first, lst[j+1].second-lst[j].second);
					ans %= MOD;
				}
				if (mask%2==0)
					tot += ans;
				else
					tot -= ans;
				tot %= MOD;
			}
		}

		tot %= MOD;
		if (tot<0) tot+=MOD;
		tot %= MOD;
		fprintf(Fou,"Case #%d: %d\n",t, tot%MOD);
	}
	return 0;
}

