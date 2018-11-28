#include<stdio.h>
#include<string.h>
#include<queue>
#include<string>
#include<set>
#include<map>
#include<algorithm>
#include<math.h>
#include<stack>
#include<sstream>
using namespace std;

char grid[4][4];
int t,dots;

int counting ( char x , int ind , int rc )
{
	int cnt=0 ;
	if ( rc==1 )
	{
		for(int i=0 ; i<4 ; i++)
			cnt += grid[ind][i]==x || grid[ind][i]=='T' ;
	}
	else if ( rc==0 )
	{
		for(int i=0 ; i<4 ; i++)
			cnt += grid[i][ind]==x || grid[i][ind]=='T' ;
	}
	else {
		for(int i=0 ; i<4 ; i++ )
			cnt += grid[i][i]==x || grid[i][i]=='T' ;
		int cnt2=0;
		for(int i=0 ; i<4 ; i++ )
			cnt2 += grid[i][4-i-1]==x || grid[i][4-i-1]=='T' ;
		cnt = max ( cnt , cnt2 );
	}
	return cnt;
}

int check()
{
	for(int i=0 ; i<4 ; i++)
		if ( counting('X',i,0)==4 || counting('X',i,1)==4 || counting('X',i,2)==4 ) return 1 ;
	for(int i=0 ; i<4 ; i++)
		if ( counting('O',i,0)==4 || counting('O',i,1)==4 || counting('O',i,2)==4 ) return 2 ;
	if ( dots != 0 )
		return 3 ;
	return 0;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	int tests=t;
	for(int tc=1 ; tc<=tests ; tc++)
	{
		printf("Case #%d: ",tc);
		dots=0;
		for(int i=0 ; i<4 ; i++)
		{
			scanf("%s",grid[i]);
			for(int j=0 ; j<strlen(grid[i]) ; j++)
				if ( grid[i][j]=='.' ) 
					dots++;
		}
		int ans = check();
		if ( ans == 3 ) printf("Game has not completed\n");
		else if ( ans == 1 ) printf("X won\n");
		else if ( ans == 2 ) printf("O won\n");
		else printf("Draw\n");
	}
	//while(1);
}