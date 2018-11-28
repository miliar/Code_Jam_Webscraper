#include <stdio.h>
#include <string.h>
#include <math.h>

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;
const int MAXN = 110;
typedef pair<int, int>	pii;
typedef vector<pii> vi;

const int INF = 1 << 30;

int 	cas, T = 0;

int 	be[10][10], bn;
int 	se[10][10], sn;
int 	ce[10][10];

void print()
{
	printf("Case #%d: ", ++T);
}

int 	p[10];
int 	lp[500000][10], cp;

void 	Perm(int pernum[], int s, int e)	// s = 0, e = N-1
{
	int i;
	if (s == e) 
	{
		memcpy(lp[cp++], p, sizeof(p));
		//for (i=0; i<=e; i++)
			
//			cout << pernum[i] << " ";
//		cout << endl;
	}
	else   
		for (i=s; i<=e; i++)
		{
			swap(pernum[s], pernum[i]);
			Perm(pernum, s+1, e);
			swap(pernum[s], pernum[i]);
		}
}


bool 	match()
{
	int 	i, j;
	
	for (i=0; i<sn; i++)
		for (j=0; j<sn; j++)
			if (se[i][j] == 1 && ce[i][j] == 0)
				return false;
	return true;		
}

int main()
{
	int 	i, j, k, kk;
	
	freopen("d.out", "w", stdout);
	freopen("D-small-attempt0.in", "r", stdin);	
	
	
	for (scanf("%d", &cas); cas; cas--)
	{
		memset(be, 0, sizeof(be));
		memset(se, 0, sizeof(se));
		
		scanf("%d", &bn);
		for (i=0; i<bn-1; i++)
		{
			int 	a, b;
			scanf("%d %d", &a, &b);
			--a, --b;
			be[a][b] = 1;
			be[b][a] = 1;
		}
		
		scanf("%d", &sn);
		for (i=0; i<sn-1; i++)
		{
			int 	a, b;
			scanf("%d %d", &a, &b);
			--a, --b;
			se[a][b] = 1;
			se[b][a] = 1;
		}
		
		for (i=0; i<sn; i++)	
			p[i] = i;
		cp = 0;
		Perm(p, 0, i-1);
		
		int 	flag = 0;
		int 	sz = 1 << bn;
		
		for (k=0; k<sz; k++)
		{
			int	 	cnt = 0;
			int		ntag[10];
			for (i=0; i<bn; i++)
				if (k & (1 << i))
					ntag[i] = cnt++;
			
			
			if (cnt != sn)	continue;
			int	 	use[10];
			for (kk=0; kk<cp; kk++)	
			{
				memcpy(use, lp[kk], sizeof(use));
				memset(ce, 0, sizeof(ce));
				for (i=0; i<bn; i++)
					for (j=0; j<bn; j++)
					{
						if (be[i][j] == 0)	continue;
						if (!(k & (1 << i)))	continue;
						if (!(k & (1 << j)))	continue;
						
						int 	a = ntag[i];
						int 	b = ntag[j];
						ce[use[a]][use[b]] = 1;
					}
				if (match())	
				{
					flag = 1;
					break;
				}
			}
			if (flag)	break;			
		}
		print();
		printf("%s\n", flag ? "YES" : "NO");		
	}

	return 0;
}
