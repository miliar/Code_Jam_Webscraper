#include <algorithm>
#include <iostream>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <ctime>
#include <stack>
#include <queue>
#include <map>
#include <set>

#define f first
#define s second
#define mp make_pair
#define pb push_back

#define ll long long

#define MIN(aa,bb) ((aa) < (bb) ? (aa) : (bb))
#define MAX(aa,bb) ((aa) > (bb) ? (aa) : (bb))
#define MIN3(aa,bb,cc) MIN((aa),MIN((bb),(cc)))
#define MAX3(aa,bb,cc) MAX((aa),MAX((bb),(cc)))

#define ABS(aa) ((aa) > 0 ? (aa) : -(aa))

#define INF INT_MAX
#define LINF 1000000000000000
#define KINF 1000000000
#define eps 1e-9

#define ii pair <int,int>
#define p_q priority_queue
#define vint vector <int>
#define vii vector <ii>
#define sint set <int>
#define sii	set <ii>

#define Kare(aa)	((aa) * (aa))
#define e(aa,bb) (ABS((aa) - (bb)) < eps)
#define all(aa)	aa.begin(),aa.end()
#define sz size()
#define csz(a) strlen(aa)
#define clr(aa) memset(aa,0,sizeof aa) 

using namespace std;

int T;
char A[10][10];
bool Win(char c)
{
	int i,j,s1,s2;
	for(i=1;i<=4;i++)
	{
		s1 = s2 = 0;
		for(j=1;j<=4;j++)
		{
			if(A[i][j] == c || A[i][j] == 'T')	s1++;
			if(A[j][i] == c || A[j][i] == 'T')	s2++;
		}
		if(s1 == 4 || s2 == 4)
			return 1;
	}
	s1 = s2 = 0;
	for(i=1;i<=4;i++)
	{
		if(A[i][i] == c 	|| A[i][i] == 'T')	s1++;
		if(A[i][5-i] == c || A[i][5-i] == 'T')	s2++;
	}
	return s1 == 4 || s2 == 4;
}
void Read()
{
	int i,j,k;
	bool flg;
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		flg = false;
		for(j=1;j<=4;j++)
			for(k=1;k<=4;k++)
			{
				scanf(" %c",&A[j][k]);
				if(A[j][k] == '.')
					flg = true;
			}
		printf("Case #%d: ",i);
		if(Win('X'))
			puts("X won");
		else if(Win('O'))
			puts("O won");
		else if(!flg)
			puts("Draw");
		else
			puts("Game has not completed");
	}
}
int main()
{
	Read();
	return 0;
}
