#include <vector>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <set>
#include <cmath>
using namespace std;

#define GI ({int t ;scanf("%d",&t);t;})
#define FORZ(i,n) for(typeof(n)i=0;i<n;i++)
#define all(x) (x).begin(),(x).end()
#define PB push_back
#define sz size()
#define FF first
#define SS second
typedef vector<int> VI;
typedef pair<int,int> pII;
typedef vector<string> VS;

const int INF = (int)(1e6);
int H , W;

bool valid (int a , int b)
{
	return (a >= 0 && a < H && b >= 0 && b < W);
}

int main ()
{
	int T = GI;
	FORZ (t , T)
	{
		H = W = 0;
		H = GI ; W = GI;
		int alt[H][W] , fallsin[H][W] , vis[H][W];
		char ans[H][W];
		FORZ (i , H)	
			FORZ (j , W)	
				alt[i][j] = GI , vis[i][j] = 0 , ans[i][j] = 'X';
				
		printf ("Case #%d:\n" , t + 1);
		
		FORZ (i , H)
		{
			FORZ (j , W)
			{
				int I = i , J = j , okay = 1;
				while (okay)
				{
					int htn = INF , htw = INF , hte = INF , hts = INF , ht = INF;
					if (valid (I - 1 , J)	&& alt[I - 1][J] < alt[I][J])	
						htn = alt[I - 1][J];
					if (valid (I , J - 1)	&& alt[I][J - 1] < alt[I][J])	
						htw = alt[I][J - 1];
					if (valid (I , J + 1)	&& alt[I][J + 1] < alt[I][J])	
						hte = alt[I][J + 1];
					if (valid (I + 1 , J)	&& alt[I + 1][J] < alt[I][J])	
						hts = alt[I + 1][J];
						
					VI v(4);v[0] = htn , v[1] = hts , v[2] = htw , v[3] = hte; sort(all(v));
					ht = v[0];				
				
					if (ht == INF || ht == alt[I][J])	
					{
						okay = 0;
						break;
					}
					
					if (ht == htn)	I --;
					else if (ht == htw)	J --;
					else if (ht == hte)	J ++;
					else if (ht == hts)	I ++;
				}
				
				fallsin[i][j] = I * W + J;
			}
		}
				
		char C = 'a';		
		FORZ (i , H)
		{
			FORZ (j , W)
			{
				if (ans[i][j] != 'X')	continue;
				FORZ (a , H) 	FORZ (b , W)	if (fallsin[a][b] == fallsin[i][j])	ans[a][b] = C;	
				C ++;
			}
		}		
		
		FORZ (i , H)
		{
			FORZ (j , W)
				printf ("%c%s" , ans[i][j] , (j == W - 1) ? "" : " ");
			printf ("\n");	
		}
	}
	return 0;
}

