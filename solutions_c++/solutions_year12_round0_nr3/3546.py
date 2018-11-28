




#include <stdio.h>
 #include <math.h>
 int main () {
 int t,e=1;
 scanf ( "%d", &t );
 while ( t-- ) {
 int a, b;
 scanf ( "%d %d", &a, &b );
 int i, j, k,l,m,n,o1,zer[100],p,in=0;
 int sum = 0;
 char yer[5]; 
for ( i = a; i <= b; i++ ) {
 j = i;
 n = i;
 l=0;
 m=i;
 while ( j != 0 ) {
 k = j%10;
 j = j / 10;
 yer[l]=k+48;
 l++;
 }
 l--;
 o1 = l; 
in = 0;
 while(l>0){
 m = (m - ( yer[l] - 48 ) * pow ( 10, o1 ))*10 + yer[l] - 48;
 zer[in++]=m;
 if(m<=b&&m>n){
 for ( p = 0;p<in-1;p++){
 if(m==zer[p])
 break;
 }
 if(p==in-1)
 sum++;
 }
 //printf ( "%d %d\n", m,n);

 // printf ( "%d %d\n", m,n);
 l--;
 }
 }
 printf ( "Case #%d: %d\n",e, sum);
 e++;
 }
 return 0;
 }
