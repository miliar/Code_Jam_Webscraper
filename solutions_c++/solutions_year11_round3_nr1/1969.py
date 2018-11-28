#include<iostream>
#include<cstdio>
#include<cstring>
#define MAX 500

using namespace std;

int main()
{
   int t;
   scanf("%d", &t);
   for( int i = 1; i <= t; i++ )
   {
	  int r, c;
	  char grid[MAX][MAX];
	  scanf("%d%d", &r, &c);
	  for( int j = 1; j <= r; j++ )
	  {
        char line[MAX];
		getchar();
		scanf("%[^\n]", line);
		for( int k = 0; k < strlen( line );k++ )
		  grid[j][k+1] = line[k];
	  }
      bool f = true;
	  for( int j = 1; j <= r; j++ )
	  {
		for( int k = 1; k <= c; k++ )
		{
		   if( grid[j][k] == '#')
		   {
			 if( grid[j][k+1] == '#' && grid[j+1][k] == '#' && grid[j+1][k+1] == '#')
			 {
			   f = true;
			   grid[j][k] = '/';
			   grid[j][k+1] = '\\';
			   grid[j+1][k] = '\\';
			   grid[j+1][k+1] = '/';
			 }
			 else
			 {
			   f = false;
			   break;
			 }
		   }
		}
		if( !f ) break;
	  }
	  printf("Case #%d:\n", i);
	  if( !f )printf("Impossible\n");
	  else
	  {
		for( int j = 1; j <= r; j++ )
		{
		  for( int k = 1; k <= c; k++ )
			printf("%c", grid[j][k]);
		   printf("\n");
		}
	  }
   }
   return 0;
}