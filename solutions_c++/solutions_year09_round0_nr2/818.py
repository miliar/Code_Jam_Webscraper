#include<iostream>
// North, West, East, South.\
// Up , Left , Right , Down
#include<cstdio>
#include<fstream>
#include<math.h>
#include<vector>
#include<iomanip>
using namespace std;

const char empty = '*';
const int inf = 9999999;
int H,W;
int mx[105][105];
char sol[105][105];

inline int min4( int a , int b , int c , int d ){
   return min( a , min(b , min(c,d) ) );
}

bool add;
char flow( char sym , int x , int y , bool flow_down = true ){
   int mn = min4( x-1>=0?mx[y][x-1]:inf , x+1<W?mx[y][x+1]:inf , y-1>=0?mx[y-1][x]:inf, y+1<H?mx[y+1][x]:inf );
   if( flow_down && mn < mx[y][x] ){
      char ch;
      if( y-1>=0 && mx[y-1][x] == mn )ch = flow( sym , x , y-1 , true );
      else if( x-1>=0 && mx[y][x-1] == mn )ch = flow( sym , x-1 , y , true );
      else if( x+1<W  && mx[y][x+1] == mn )ch = flow( sym , x+1 , y , true );
      else if( y+1<H  && mx[y+1][x] == mn )ch = flow( sym , x , y+1 , true );
      sol[y][x] = ch;
      return ch;
   }else{
      if( sol[y][x] == empty ){sol[y][x] = sym; add = true; }
      else add = false;
      return sol[y][x];
   }
}

int main(){
   freopen("Ulaz.txt","r",stdin);
   freopen("Izlaz.txt","w",stdout);
   int tests,i,j;
   scanf("%d",&tests);
   for( int t = 1 ; t <= tests ; t++ ){
      scanf("%d%d",&H,&W);
      for(i=0;i<H;i++)
         for(j=0;j<W;j++){
            scanf("%d",&mx[i][j]);
            sol[i][j] = empty;
         }
      char c = 'a';
      for(i=0;i<H;i++){
         for(j=0;j<W;j++){
            if( sol[i][j] == empty ){
               flow( c , j , i );
               c+=add;
            }
         }
      }
      printf("Case #%d:\n",t);
      for(i=0;i<H;i++){
         for(j=0;j<W;j++){
            printf("%c ",sol[i][j]);
         }printf("\n");
      }
   }
   return 0;
}
