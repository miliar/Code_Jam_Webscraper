#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int main() {
    int test , i , tc = 1 , j;
    long  long n , d, g;
    freopen("s.in","r",stdin);
    freopen("s.out","w",stdout);
    scanf("%d",&test);
    while( test--  ) {
           cin>>n>>d>>g;
           //cout<<n<<d<<g<<endl;
           if( (g == 100 && d != 100) || ( g == 0 && d != 0) ) {
               printf("Case #%d: Broken\n",tc++);
               continue;
           }
           if( d == 0 || d == 100 ) {
               printf("Case #%d: Possible\n",tc++);      continue;
           }
           
           if( n >= 100 ) {
               printf("Case #%d: Possible\n",tc++);
           } else {
                  for( i = 1; i <= n;i++ ) {
                       if( (i*d)%100 == 0 ) {
                           break;
                       }
                  }
                  if( i <= n ) printf("Case #%d: Possible\n",tc++);
                  else  printf("Case #%d: Broken\n",tc++);
           }
    }
    return 0;
}
