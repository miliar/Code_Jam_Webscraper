#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <queue>
#include <math.h>
#include <time.h>

using namespace std;

#define RP(a,h) for(int (a)=0; (a)<(h); (a)++)
#define FR(a,l,h) for(int (a)=(l); (a)<=(h); (a)++)
#define INF 2000000000
#define sz size()
#define pb push_back
#define sv(v) sort((v).begin(), (v).end())
#define ABS(x) (((x)>0)?(x):(-(x)))


#define IMAX 30000000
#define EPS 1e-7

int a[100][100];
int p[100][100];
int best;
int n, l;
int v[100][100];
int vl[100];
int vc;

void loang(int pos)
{
	if (vc >= best) return;
	RP(i, vc)
	{
		int ok = true;
		RP(j, vl[i])
		{
			if (a[pos][v[i][j]] == 1) { ok = false; break; }
		}
		
		if (ok)
		{
			v[i][vl[i]] = pos; vl[i]++;
			if (pos == n-1) best <?= vc;
			else loang(pos+1);
			vl[i]--;
		}
	}
	
	if (pos == n-1) { best <?= vc+1; }
	else
	{
		v[vc][0] = pos;
		vl[vc] = 1;
		vc++;
		loang(pos+1);
		vc--;
	}
}

int main()
{   
	int t;	
	cin >> t;
	
    RP(test, t)
    {
		cin >> n >> l;
		
		RP(i, n)
		{
			RP(j, l) cin >> p[i][j];
		}
		
		memset(a, 0, sizeof(a));
		RP(i, n)
		{
			FR(j, i+1, n)
			{
				RP(k, l-1)
				{
					if (p[i][k] == p[j][k] || p[i][k+1] == p[j][k+1]) { a[i][j] = 1; a[j][i] = 1; }
					else
					{
						if (p[i][k] < p[j][k] && p[i][k+1] > p[j][k+1]) { a[i][j] = 1; a[j][i] = 1; }
						if (p[i][k] > p[j][k] && p[i][k+1] < p[j][k+1]) { a[i][j] = 1; a[j][i] = 1; }
					}
				}
			}
		}
		
		vc = 0;
		memset(vl, 0, sizeof(vl));
		best = 100000;
		loang(0);
		printf("Case #%d: %d\n", test+1, best);
	}
    
    return 0;
}
