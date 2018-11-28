#include <iostream>
#include <sstream>

using namespace std;

int x,i,j,last;
bool b[100000];
int  a[210000];
char s[1000];


int check( int x, int i ) {
     int s = 0;

     //while (s != 1) {        

        if ( b[x] == 1 ) return x;
        b[x] = 1;

	while ( x > 0 ) {
            int k = (x%i); 
            k = k*k;
            s += k;
            x /= i;
         }
         
         if ( s == 1 ) { 
            return s;
         } else return check(s,i);
      //}
}

int main() {
   freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

   memset(a,0,sizeof(a));
   for ( j = 1; j <= 100000; j++ ) {
      int y = 0;

      for ( i = 2; i <= 10; i++ ) {
         last = 0; memset(b,0,sizeof(b));

         x = check(j, i);


         if ( x == 1 ) 
            y = y ^ ( 1 << i );

      }
      a[j] = y;
   }

   int nt;
   scanf("%d\n", &nt);

      for ( int t = 1; t <= nt; t++ ) {
         gets(s);   
         istringstream iss(s);

         int y = 0;
         while ( iss >> x ) 
            y = y ^ ( 1 << x );

         for ( int i = 2; i <= 100000; i++ )
            if ( (y & a[i]) == y ) {
               printf("Case #%d: %d\n", t, i);
               break;
            }
      }
   return 0;
}
