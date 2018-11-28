#include<cstdio>
#include<cstring>

char borra[32][2];
char comb[64][4];
char res[128];
int t, c, d, n, ncaso, x, y, z, r;

void reset()
{
   int i, j;
   for(i=0;i<32;i++)
      for(j=0;j<2;j++)
         borra[i][j] = 0;
   for(i=0;i<64;i++)
      for(j=0;j<4;j++)
         comb[i][j] = 0;
   for(i=0;i<128;i++)
      res[i] = 0;
}

main(){

scanf("%d", &t);
for(ncaso=1;ncaso<=t;ncaso++)
{
   reset();
   scanf("%d", &c);
   for(x=0;x<c;x++)
      scanf(" %s", &comb[x]);
   scanf("%d", &d);
   for(x=0;x<d;x++)
      scanf(" %c%c", &borra[x][0], &borra[x][1]);
   scanf("%d ", &n);
   for(r=x=0;x<n;x++,r++)
   {
      scanf("%c", &res[r]);
      for(y=0;y<c && r>0;y++)
      {
         if( (res[r-1] == comb[y][0] && res[r] == comb[y][1])
          || (res[r] == comb[y][0] && res[r-1] == comb[y][1]) )
         {
            res[--r] = comb[y][2];
            y = c;
         }
      }
      for(y=0;y<d;y++)
      {
         if( res[r] == borra[y][0] )
         {
            for(z=r-1;z>=0;z--)
               if( res[z] == borra[y][1] )
                  r = z = -1;
         }
         else if( res[r] == borra[y][1] )
         {
            for(z=r-1;z>=0;z--)
               if( res[z] == borra[y][0] )
                  r = z = -1;
         }
      }
   }
   printf("Case #%d: [", ncaso);
   if( r > 0 )
   printf("%c", res[0]);
   for(x=1;x<r;x++)
      printf(", %c", res[x]);
   printf("]\n");
}

return 0;
}
