#include<stdio.h>
#include<iostream>
#include<string>

using namespace std;

#define MAX 4
#define X 'X'
#define O 'O'
#define T 'T'
#define D 'D'
#define M '.'

#define FOR(i,n) for(int i=0;i<n;++i)
#define FORS(i,s,n) for(int i=s;i<;++i)

void print(char a[MAX][MAX])
{
	FOR(i,MAX)
	{
		FOR(j,MAX)
		{
			cout<<a[i][j];
		}
		
		cout<<endl;
	}
}

void repair(char a[MAX][MAX], const pair<int, int>& Tpos, char rep)
{
	if(Tpos.first!=-1)
	{
		a[Tpos.first][Tpos.second] = rep;
	}
}

bool solve_internal(char a[MAX][MAX], char p)
{
	pair<int,int> Tpos(-1,-1);
	
	// Replace T with p
	FOR(i,MAX)
	{
		FOR(j,MAX)
		{
			if(a[i][j]==T)
			{
				Tpos.first = i;
				Tpos.second = j;
				repair(a, Tpos, p);
				break;
			}
		}
	}

	// Check rows and cols
	FOR(i,MAX)
	{
		bool row=true, col=true;
	
		FOR(j,MAX)
		{
			row = (row && a[i][j] == p);
			col = (col && a[j][i] == p);		
		}

		if(row||col)
		{
			repair(a,Tpos,T);
			return true;
		}
	}

	bool d1=true, d2=true;
	// Check diagnols
	FOR(i,MAX)
	{
		d1 = d1 && (a[i][i] == p);
		d2 = d2 && (a[i][MAX-i-1]==p);
	}

	if(d1||d2)
	{
		repair(a,Tpos,T);
		return true;
	}

	repair(a,Tpos,T);
	return false;
	
}

char solve(char a[MAX][MAX])
{
	char winner = T;
	if(solve_internal(a, X)) return X;
	if(solve_internal(a, O)) return O;
	
	// Check incomplete;
	FOR(i,MAX)
	{
		FOR(j,MAX)
		{
			if(a[i][j]==M)
			{
				return M;
			}
		}
	}
		
	// Return draw
	return D;
}



int main()
{
	int t,n;
	char a[MAX][MAX];
	scanf("%d", &t);

	FOR(C,t)
	{
		scanf("%d",&n);
		
		FOR(i,MAX)
		{
			scanf("%s",&a[i]);	
		}
		
		char result = solve(a);
		
		printf("Case #%d: ",C+1);

		if(result == X || result == O)
		{
			printf("%c won\n", result);
		}
		else if(result==D)
		{
			printf("Draw\n");
		}
		else
		{
			printf("Game has not completed\n");
		}
	}

	return 0;
}
