#include <iostream>
#include <string>
using namespace std;

#define N 55

char map[N][N]={0};

char * solve(int n,int K)
{
	char tem[N][N];
	for ( int i = 0 ; i < n ; i++ )
	{
		int j;
		for ( j = 0 ; j < n ; j++ )
			tem[i][n-j-1] = map[j][i];
		tem[i][n] = '\0';
//		printf("%s\n",tem[i]);
	}
	for ( int j = 0 ; j < n ; j++ )
	{
		for ( int i = 0 ; i < n ; i++ )
		{
			for ( int k = n-1 ; k > i ; k-- )
			{
				if ( tem[k][j]=='.' && tem[k-1][j]!='.' )
					swap(tem[k][j],tem[k-1][j]);
			}
		}
	}
	/*
	for ( int i = 0 ; i < n ; i++ )
		printf("%s\n",tem[i]);
		*/
	int flag1 = 0;
	int flag2 = 0;
	for ( int i = 0 ; i < n ; i++ )
		for ( int j = 0 ; j < n ; j++ )
		{
			int k;
			for ( k = 0 ; k < K && i+k<n ; k++ )
				if ( tem[i+k][j] != tem[i][j] )
					break;
			if ( k==K )
			{
				if ( tem[i][j]=='B' )
					flag1 = 1;
				else if ( tem[i][j]=='R' )
					flag2 = 1;
			}

			for ( k = 0 ; k < K && j+k<n ; k++ )
				if ( tem[i][j+k] != tem[i][j] )
					break;
			if ( k==K )
			{
				if ( tem[i][j]=='B' )
					flag1 = 1;
				else if ( tem[i][j]=='R' )
					flag2 = 1;
			}

			for ( k = 0 ; k < K && i+k<n && j+k<n ; k++ )
				if ( tem[i+k][j+k] != tem[i][j] )
					break;
			if ( k==K )
			{
				if ( tem[i][j]=='B' )
					flag1 = 1;
				else if ( tem[i][j]=='R' )
					flag2 = 1;
			}

			for ( k = 0 ; k < K && i-k>=0 && j+k<n ; k++ )
				if ( tem[i-k][j+k] != tem[i][j] )
					break;
			if ( k==K )
			{
				if ( tem[i][j]=='B' )
					flag1 = 1;
				else if ( tem[i][j]=='R' )
					flag2 = 1;
			}
		}

	if ( flag1==1 && flag2==1 )
		return "Both";
	else if ( flag1==1 && flag2==0 )
		return "Blue";
	else if ( flag1==0 && flag2==1 )
		return "Red";
	return "Neither";

}

int main(void)
{
	freopen("A-large.in","r",stdin);
	freopen("A-large-out.out","w",stdout);
	int T;
	scanf("%d",&T);
	for ( int c = 1 ; c <= T ; c++ )
	{
		int n,K;
		scanf("%d %d",&n,&K);
		for ( int i = 0 ; i < n; i++ )
			scanf("%s",map[i]);
		printf("Case #%d: %s\n",c,solve(n,K));
	}
//	system("pause");
	return 0;
}