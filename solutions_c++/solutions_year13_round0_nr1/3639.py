#include<cstdio>
#include<cstring>
using namespace std;
char s[4][4];
int main()
{
	int cas;
	int ca = 0;
	scanf( "%d", &cas );
	while ( cas-- )
	{
		for ( int i = 0; i < 4; i++ )
			scanf( "%s", s[i] );
		int ans = 0;
		bool u = true;
		for ( int i = 0; i < 4; i++ )
		{
			u = true;
			for ( int j = 0; j < 4; j++ )
			if ( s[i][j] == 'O' || s[i][j] == '.' ) u = false;
			if ( u ) break;
		}
		if ( u ) 
		{
			ans = 1;
		}
		else
		{
			for ( int i = 0; i < 4; i++ )
			{
				u = true;
				for ( int j = 0; j < 4; j++ )
				if ( s[i][j] == 'X' || s[i][j] == '.' ) u = false;
				if ( u  ) break;
			}
			if ( u ) 
			{
				ans = 2;
			}
		}
		if ( ans == 0 )
		{
			u = true;
			for ( int i = 0; i < 4; i++ )
			{
				u = true;
				for ( int j = 0; j < 4; j++ )
				if ( s[j][i] == 'O' || s[j][i] == '.' ) u = false;
				if ( u ) break;
			}
			if ( u ) 
			{
				ans = 1;
			}
			else
			{
				for ( int i = 0; i < 4; i++ )
				{
					u = true;
					for ( int j = 0; j < 4; j++ )
					if ( s[j][i] == 'X' || s[j][i] == '.' ) u = false;
					if ( u ) break;
				}
				if ( u ) 
				{
					ans = 2;
				}
			}
		}
		if ( ans == 0 )
		{
			u = true;
			for ( int i = 0; i < 4; i++ )
			{
				if ( s[i][i] == 'O' || s[i][i] == '.' ) u = false;
				if ( u == false ) break;
			}
			if ( u ) 
			{
				ans = 1;
			}
			else
			{
				u = true;
				for ( int i = 0; i < 4; i++ )
				{
					if ( s[i][i] == 'X' || s[i][i] == '.' ) u = false;
					if ( u == false ) break;
				}
				if ( u ) 
				{
					ans = 2;
				}
			}
		}
		if ( ans == 0 )
		{
			u = true;
			for ( int i = 0; i < 4; i++ )
			{
				if ( s[3-i][i] == 'O' || s[3-i][i] == '.' ) u = false;
				if ( u == false ) break;
			}
			if ( u ) 
			{
				ans = 1;
			}
			else
			{
				u = true;
				for ( int i = 0; i < 4; i++ )
				{
					if ( s[3-i][i] == 'X' || s[3-i][i] == '.' ) u = false;
					if ( u == false ) break;
				}
				if ( u ) 
				{
					ans = 2;
				}
			}
		}
		ca++;
		printf("Case #%d: ",ca);
		if ( ans != 0 )
		{
			if ( ans == 1 ) printf("X won\n");
			else printf("O won\n");
		}
		else
		{
			for ( int i = 0; i < 4; i++ )
				for ( int j = 0; j < 4; j++ )
				if ( s[i][j] == '.' ) ans = -1;
			if ( ans == -1 ) printf("Game has not completed\n");
			else printf("Draw\n");
		}
	}
	return 0;
}
