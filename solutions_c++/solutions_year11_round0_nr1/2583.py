#include<cstdio>

struct bot
{
   int mov, pos;
};

char c;
int t, n, x, caso, m;
bot orange, blue;

int abso( int a )
{
   if( a < 0 )
      return a*(-1);
   return a;
}

main(){

scanf("%d", &t);
for(caso=1;caso<=t;caso++)
{
   orange.mov = blue.mov = 0;
   orange.pos = blue.pos = 1;
   scanf("%d", &n);
   for(x=0;x<n;x++)
   {
      scanf(" %c%d", &c, &m);
      if( c == 'O' )
      {
         orange.mov = orange.mov + abso(orange.pos - m) + 1;
         if( blue.mov >= orange.mov )
            orange.mov = blue.mov+1;
         orange.pos = m;
      }
      else if( c == 'B' )
      {
         blue.mov = blue.mov + abso(blue.pos - m) + 1;
         if( orange.mov >= blue.mov )
            blue.mov = orange.mov+1;
         blue.pos = m;
      }
   }
   printf("Case #%d: %d\n", caso, blue.mov>orange.mov?blue.mov:orange.mov);
}

return 0;
}
