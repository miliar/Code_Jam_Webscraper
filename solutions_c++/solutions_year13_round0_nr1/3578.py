#include<fcntl.h>
#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <stdlib.h>
#include <math.h>
#include <netdb.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

#define loopab(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define loopn(a,b) loopab( a, 0, ( b ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define mms(a,b) memset( a, b, sizeof( a ) )

using namespace std;

template <class T> void out( T a, T b ) { bool first = true; for( T i = a; i != b; ++ i ) { if( !first ) printf( " " ); first = false; cout << * i; } printf( "\n" ); }
template <class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;



void solve(void)
{
	int board[4][4],mul_row,mul_col,player,i,j,k,l;
	bool not_comp = false;
	char c;
	loopn(i,4)
	{
		loopn(j,4)
		{
			if(j!=3)
				scanf("%c",&c);
			else
				scanf("%c\n",&c);

			if(c=='X')
				board[i][j] = 2;
			else if(c=='O')
				board[i][j] = 3;
			else if(c=='T')
				board[i][j] = 10;
			else
			{
				board[i][j] = 1;
				not_comp = true;
			}
			//printf("%d",board[i][j]);
		}
	}	
	//-------------------
	loopn(k,4)
	{
		mul_row = 1;
		mul_col = 1;
		loopn(l,4)
		{
			mul_row*=board[k][l];
			mul_col*=board[l][k];
		}
		if(mul_row==16 || mul_row==80 || mul_col==16 || mul_col==80)
		{
			printf("X won");
			return;
		}
		else if(mul_row==81 || mul_row==270 || mul_col==81 || mul_col==270)
		{
			printf("O won");
			return;
		}
	}
	mul_row = board[0][0]*board[1][1]*board[2][2]*board[3][3];
	mul_col = board[3][0]*board[2][1]*board[1][2]*board[0][3];
	if(mul_row==16 || mul_row==80 || mul_col==16 || mul_col==80)
	{
		printf("X won");
		return;
	}
	else if(mul_row==81 || mul_row==270 || mul_col==81 || mul_col==270)
	{
		printf("O won");
		return;
	}
	else if(not_comp)
	{
		printf("Game has not completed");
		return;
	}
	else
	{
		printf("Draw");
		return;
	}

}

int main(int argc, char *argv[])
{
        unsigned long int i,j,t;
       	int fdi = open("input.txt",O_RDONLY);
	close(0);
        dup(fdi);
        close(fdi);        
	int fdo = creat("output.txt",0644);
        close(1);
        dup(fdo);
        close(fdo);
        
	scanf("%ld\n",&t);
	for(j=0;j<t;j++)
        {
		printf("Case #%ld: ",j+1);
		solve();
		printf("\n");
        }
return 0;
}
