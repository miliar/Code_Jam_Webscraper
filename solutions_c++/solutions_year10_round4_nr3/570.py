
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<string>
#include<set>
#include<map>
#include<queue>
#include<cstdio>

using namespace std;
int m, n;
int a[200][200];
int main()
{
   int k, t, tests;
   int itest;
   for(itest = 1, scanf("%d",&tests); itest <= tests; itest++) {
       memset(a,0,sizeof(a));
       int x1,x2,y1,y2;
       int r;
       scanf("%d", &r); 
       int i,j,x,y;
       for(i = 0 ; i < r; i++) {
	   scanf("%d%d%d%d", &x1,&y1,&x2,&y2); 
	   for(x = x1; x <= x2; x++) {
	       for(y = y1; y <= y2; y++) {
		   a[x][y] = 1;
	       }
	   }
       }
       int answer = 0;
       int c = 1;
       while(c && ++answer ) {
	   c = 0;
	   for(i = 100; i > 0 ; i-- ) {
	       for(j = 100; j > 0 ; j-- ) {
		   if( a[i-1][j] == 0 and a[i][j-1] == 0 ) {
		       a[i][j] = 0;
		   }
		   if( a[i-1][j] == 1 and a[i][j-1] == 1) {
		       a[i][j] = 1;
		   }
		   if( a[i][j] == 1) c ++;
	       }
	   }
       }

       printf("Case #%d: %d \n", itest,answer);
   }
   return 0;
}
