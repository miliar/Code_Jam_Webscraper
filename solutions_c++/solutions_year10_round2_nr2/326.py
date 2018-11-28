
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
int x[100],v[100];
int main()
{
   int k, t, tests;
   int g;
   scanf("%d", &tests); 
   int b,i,j;
   
   for( g = 1; g <= tests; g++) {
       scanf("%d %d %d %d",&n,&k,&b,&t);
       vector<int> r(n);
       for(i = 0; i < n;i++) {
	   scanf("%d", &x[i]); 
       }
       for(i = 0; i < n;i++) {
	   scanf("%d", &v[i]); 
       }
       for(i = 0; i < n; i++) 
	   if( x[i] + v[i] * t < b ) {
	       r[i] += 10000000;
	   }
       for(i = 0; i < n; i++) {
	   for(j = i + 1; j < n; j++) {
	       if( r[j] < 100000 ) continue;
	       double time = x[i] - x[j];
	       if( v[i] != v[j] ) {
		   time /= v[j] - v[i];
		   if ( time > 0 &&  time < t && x[i] + v[i] * time < b) {
		       r[i] ++;
		    //   printf("%d,",j);
		   }
	       }
	   }
	 //  printf("r%d = %d\n",i,r[i]);
       }
       sort(r.begin(), r.end());
       int s=0;
       for(i = 0; i < k; i++) s += r[i];
       printf("Case #%d: ",g);
       if( s > 10000) {
	   printf("IMPOSSIBLE\n");
       }
       else printf("%d\n",s);

       


   }
   return 0;
}
