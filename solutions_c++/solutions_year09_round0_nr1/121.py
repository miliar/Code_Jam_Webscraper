#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;

#define FOR( i , a , b ) for( int (i)=(a);(i)<=(b);i++)
int N , M , L;
int A[5005][25];
bool Ok[25][35];

void Init()
{
     scanf("%d%d%d\n" , &L , &N , &M);
     char ch;
     FOR( i , 1 , N )
     {
          FOR( j , 1 , L )
          {
               scanf("%c" , &ch);
               A[i][j] = ch - 'a';
          }
          scanf("\n");
     }
}

int Find()
{
    int Res = 0;
    FOR( i , 1 , N )
    {
         bool flag = true;
         FOR( j , 1 , L )
         if( !Ok[j][A[i][j]] ) { flag = false; break; }
         Res += flag;
    }
    return Res;
}        

void Work()
{
     FOR( t , 1 , M )
     {
          memset( Ok , false , sizeof(Ok));
          char ch;
          FOR( i , 1 , L )
          {
               scanf("%c" , &ch);
               if( ch != '(' )
               {
                   Ok[i][ch-'a'] = true;
                   continue;
               }
               while( scanf("%c" , &ch) == 1 )
               {
                      if( ch == ')' ) break;
                      Ok[i][ch-'a'] = true;
               }
          }
          scanf("\n");
          printf("Case #%d: %d\n" , t , Find() );
     }
}
     

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
        Init();
        Work();
    return 0;
}
