#include <iostream>
#define MAXN 20010
#define inf INT_MAX

using namespace std;

int val[MAXN];
struct Nod 
{
	bool ord, ifChange;
	Nod () {}
	Nod ( bool ord , bool ifChange ):
	ord(ord), ifChange(ifChange) {}
};

int n, m;
Nod ND[MAXN];
int DP[MAXN][2];

void DFS ( int Root )
{
	if ( Root * 2 > n )
	{
		DP[Root][val[Root]] = 0;
		DP[Root][1-val[Root]] = -1;
		return;
	}
	DFS (Root*2);
	DFS (1+Root*2);
	DP[Root][0] = DP[Root][1] = inf;
	int leftA, leftB, rightA, rightB;
	leftA = DP[Root*2][0];
	leftB = DP[Root*2][1];
	rightA = DP[Root*2+1][0];
	rightB = DP[Root*2+1][1] ;
	if(ND[Root].ord == true)
	{
		if(leftA != -1 && rightA != -1)
		{
			if(DP[Root][0] > leftA + rightA)
				DP[Root][0] = leftA + rightA ;
		}
		if(leftA != -1 && rightB != -1)
		{
			if(DP[Root][0] > leftA + rightB)
				DP[Root][0] = leftA + rightB ;
		}
		if(leftB != -1 && rightA != -1)
		{
			if(DP[Root][0] > leftB + rightA)
				DP[Root][0] = leftB + rightA ;
		}
		if( leftB != -1 && rightB != -1)
		{
			if(DP[Root][1] > leftB + rightB)
				DP[Root][1] = leftB + rightB ;
		}
	}
	else
	{
		if(leftA != -1 && rightA != -1)
		{
			if(DP[Root][0] > leftA + rightA)
				DP[Root][0] = leftA + rightA ;
		}
		if(leftA != -1 && rightB != -1)
		{
			if(DP[Root][1] > leftA + rightB)
				DP[Root][1] = leftA + rightB ;
		}
		if(leftB != -1 && rightA != -1)
		{
			if(DP[Root][1] > leftB + rightA)
				DP[Root][1] = leftB + rightA ;
		}
		if( leftB != -1 && rightB != -1)
		{
			if(DP[Root][1] > leftB + rightB)
				DP[Root][1] = leftB + rightB ;
		}
	}
	if(ND[Root].ifChange == true)
	{
		if(ND[Root].ord == true)
		{
			if(leftA != -1 && rightA != -1)
			{
				if(DP[Root][0] > leftA + rightA + 1)
					DP[Root][0] = leftA + rightA + 1;
			}
			if(leftA != -1 && rightB != -1)
			{
				if(DP[Root][1] > leftA + rightB + 1)
					DP[Root][1] = leftA + rightB + 1;
			}
			if(leftB != -1 && rightA != -1)
			{
				if(DP[Root][1] > leftB + rightA + 1)
					DP[Root][1] = leftB + rightA + 1;
			}
			if( leftB != -1 && rightB != -1)
			{
				if(DP[Root][1] > leftB + rightB + 1)
					DP[Root][1] = leftB + rightB + 1;
			}
		}
		else
		{
			if(leftA != -1 && rightA != -1)
			{
				if(DP[Root][0] > leftA + rightA + 1)
					DP[Root][0] = leftA + rightA +1;
			}
			if(leftA != -1 && rightB != -1)
			{
				if(DP[Root][0] > leftA + rightB + 1)
					DP[Root][0] = leftA + rightB + 1;
			}
			if(leftB != -1 && rightA != -1)
			{
				if(DP[Root][0] > leftB + rightA + 1)
					DP[Root][0] = leftB + rightA+ 1 ;
			}
			if( leftB != -1 && rightB != -1)
			{
				if(DP[Root][1] > leftB + rightB + 1)
					DP[Root][1] = leftB + rightB + 1;
			}
		}
	}
	if(DP[Root][0] == inf ) 
		DP[Root][0] = -1;
	if(DP[Root][1] == inf )
		DP[Root][1] = -1;
}


int main (void)
{
	freopen ("A-large.in","r",stdin);
	freopen ("A.out","w",stdout);
	int T, Case = 0;
	scanf ("%d",&T);
	while ( T -- )
	{
		Case ++;
		int ord, ifChange;
		scanf ("%d%d",&n,&m);
		memset(val,-1,sizeof(val));
		int i;
		for ( i = 1; i <= (n-1)/2; i ++ )
		{
			scanf ("%d%d",&ord,&ifChange);
			if ( ord == 1 )
				ND[i].ord = 1;
			else
				ND[i].ord = 0;
			if ( ifChange == 1 )
				ND[i].ifChange = 1;
			else
				ND[i].ifChange = 0;
		}
		for ( i = (n-1)/2+1 ; i <= n ; i ++ )
			scanf ("%d",&val[i]);
		DFS (1);
		printf ("Case #%d: ",Case);
		if(DP[1][m] == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",DP[1][m]);
	}
	return 0;
}