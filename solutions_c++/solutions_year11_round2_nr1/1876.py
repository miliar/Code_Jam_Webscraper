#include<cstdio>
#include<iostream>
#include<cstring>

#define MAX 400

using namespace std;

int main()
{
   int t;
   scanf("%d", &t);

   for( int i = 1;i <= t; i++ )
   {
	  int n;
	  int grid[MAX][MAX];
	  char line[MAX];
	  memset( grid, -1, sizeof( grid ) );
	  
	  scanf("%d", &n);
 
	  for( int j = 1; j <= n; j++ )
	  {
		getchar();
		scanf("%[^\n]", line);
// 		cout << line << endl;
		for( int k = 0; k < strlen( line ); k++ )
		{
		  if( line[k] == '1') grid[j][k+1] = 1;
		  else if( line[k] == '0' )grid[j][k+1] = 0;
		}
	  }
// 	  for( int j = 1; j <= n; j++ )
// 	  {
// 		for( int k = 1; k <=n; k++ )
// 		  printf("%d ", grid[j][k]);
// 		printf("\n");
// 	  }
	  double wp[MAX], owp[MAX], oowp[MAX];
      double data[MAX][MAX];
	  for( int j = 1; j <= n; j++ )for( int k = 1; k <= n; k++ )data[j][k] = -1.0;
	  for( int j = 1; j <= n; j++ )
	  {
		int total = 0, win = 0;
		for( int k = 1; k <= n; k++ )
		{
		   if( grid[j][k] != -1 )total += 1;
		   if( grid[j][k] == 1 )win += 1;
		}
		wp[j] = (win/ (double)total);
		for( int k = 1; k <= n; k++ )
		{
		   int t = total, w = win;
		   if( grid[j][k] != -1 )t -= 1;
		   if( grid[j][k] == 1 )w  -= 1;

		   data[j][k] = w/(double)t;
		}
	  }
//        for( int k = 1; k <= n; k++ )
//    		  printf("%lf  ", wp[k]);
//  	  for( int j = 1; j <= n; j++ )
//   	  {
//   		for( int k = 1; k <=n; k++ )
//   		  printf("%lf ", data[j][k]);
//   		printf("\n");
//   	  }
	  for( int j = 1; j <= n; j++ )
	  {
		double sum = 0;
		int total = 0;
		 for( int k = 1; k <= n; k++ )
		 {
		   if( grid[j][k] != -1 )
		   {
			 total += 1;
		    sum += data[k][j];
		   }
		 }
		 owp[j] = sum / total;
	  }
//     	for( int k = 1; k <=n; k++ )
//  		  printf("%lf ",owp[k]);
//       printf("\n\n");
	  
	  for( int j = 1; j <= n; j++ )
	  {
		double sum = 0;
		int total = 0;
		 for( int k = 1; k <= n; k++ )
		 {
		   if( grid[j][k] != -1 )
		   {
			 total += 1;
		     sum += owp[k];
		   }
		 }
		 oowp[j] = sum / total;
	  }

      printf( "Case #%d: \n", i );
	  for( int j = 1; j <= n; j++ )
	  {
		double rpi = 0.25*wp[j] + 0.50*owp[j] + 0.25*oowp[j];
		printf("%lf\n", rpi);
	  }
   }
   return 0;
}