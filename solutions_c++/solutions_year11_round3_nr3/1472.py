#include<iostream>
#include<cstdio>
#include<cstring>
#define MAX 10001

using namespace std;

int main()
{
   int t;
   scanf("%d", &t);
   for( int i = 1; i <= t; i++ )
   {
	 int n,l, h;
	 int freq[MAX];
     scanf("%d%d%d", &n, &l, &h);
	 for( int j = 1; j <= n; j++ )
	  scanf("%d", &freq[j]);

	 int s = l, e = h;
	 int min = -1;
	 bool f = true;
	 for( int m = l; m <= h; m++ )
	 {
	   
	   for( int j = 1; j <= n; j++ )
	   {
		  if( m % freq[j] == 0 || freq[j] % m == 0 )f = true;
		  else
		  {
			 f = false;
			 break;
		  }
	   }
	   if( f )
	   {
		 min = m;
		 break;
	   }
	 }
	 if( !f )
	  printf("Case #%d: NO\n", i);
	 else
	  printf("Case #%d: %d\n", i, min);
   }
   return 0;
}