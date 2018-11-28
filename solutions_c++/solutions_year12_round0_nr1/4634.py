#include<stdio.h>
#include<iostream>
#include<string.h>
#include<algorithm>
using namespace std;
int main ()
{
    char arr [27];
    arr[0] = 'y';
arr[1] = 'h';
arr[2] = 'e';
arr[3] = 's';
arr[4] = 'o';
arr[5] = 'c';
arr[6] = 'v';
arr[7] = 'x';
arr[8] = 'd';
arr[9] = 'u';
arr[10] = 'i';
arr[11] = 'g';
arr[12] = 'l';
arr[13] = 'b';
arr[14] = 'k';
arr[15] = 'r';
arr[16] = 'z';
arr[17] = 't';
arr[18] = 'n';
arr[19] = 'w';
arr[20] = 'j';
arr[21] = 'p';
arr[22] = 'f';
arr[23] = 'm';
arr[24] = 'a';
arr[25] = 'q';
int t ; 
char g[105];
char g1[105];
scanf ("%d",&t);
t ++ ;
//fflush(stdin);
int t1 = 0;
int chk = 0 ;
while ( t -- )
{
      gets(g);
      int i ;
      for (  i = 0 ; i < strlen(g) ; i ++ )
      {
          if ( g[i] == ' '){
             g1[i] = ' ';
             continue;
          }
          g1[i] = arr[g[i] - 'a'];
      }
      g1[i] = '\0';
      if( t1!=0 ){
      printf ("Case #%d: ",t1);
      puts(g1);}
      t1++;
      chk ++ ;
      
}
    
}

