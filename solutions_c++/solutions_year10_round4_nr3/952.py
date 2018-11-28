#include <iostream>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#define nextline { while (getchar() != '\n') ; }
#define sqr(a) ((a)*(a))
#define has(mask,i) (((mask) & (1<<(i))) == 0 ? false : true)
using namespace std ;

#define mp make_pair
#define pb push_back
typedef long long ll ;
typedef long double ldb ;

const int INF = (1 << 30) - 1 ;
const ldb EPS = 1e-9 ;

bool ma[2][105][105] ;
int main()
{
	int nt ;
	scanf ("%d", &nt) ;
	int r ;
	int x1 , y1 , x2 , y2 ;
	int cr = 0 , ne = 0 ;
	for (int tt = 1; tt <= nt; tt++)
	{ 
		scanf ("%d", &r) ;
		memset (ma[0], false, sizeof(ma[0])) ;
		memset (ma[1], false, sizeof(ma[1])) ;
		for (int i = 1; i <= r; i++)
		{
			scanf ("%d%d%d%d", &x1, &y1, &x2, &y2) ;
			for (int x = x1; x <= x2; x++)
				for (int y = y1; y <= y2; y++)
					ma[0][x][y] = ma[1][x][y] = 1 ;
		}
		int res = 0 ;
		bool ch = true ;
		cr = 0 , ne = 1 ;
		while (ch)
		{
			res++ ;
			ch = 0 ;
			for (int i = 1; i <= 100; i++)
				for (int j = 1; j <= 100; j++)
				{
					if (ma[cr][i][j])
					{
						if (!ma[cr][i - 1][j] && !ma[cr][i][j - 1]) ma[ne][i][j] = 0 ;
						else
						{
							ch = 1 ;
							ma[ne][i][j] = 1 ;
						}
					}
					if (ma[cr][i - 1][j] && ma[cr][i][j - 1] && !ma[cr][i][j])
					{
						ch = 1 ;
						ma[ne][i][j] = 1 ;
					}
				}	
			memset (ma[cr],0,sizeof(ma[cr])) ;
			swap (ne,cr) ;
		}	
		printf ("Case #%d: %d\n", tt, res) ;
	}	
	return 0 ;
}
