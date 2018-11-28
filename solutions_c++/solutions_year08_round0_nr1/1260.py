# include <stdio.h>
# include <string>
# include <algorithm>
# include <map>

using namespace std;
char line[1000];
char list[1002][100];
char eng[ 102][100];
int din[101][1001],  n, m;

int solve( int engine, int position ){
   int res = (1<<22), x;
   if( position >= m ) return 0;
   if( din[ engine ][ position ] != -1) return din[ engine ][ position ];
   if( strcmp( eng[ engine ] ,  list[ position ]) != 0) 
      return din[engine ][ position ] = solve( engine, position + 1);
   for( x = 0; x < n; x++)
   if( strcmp( eng[ x ], list[ position ]) != 0){
     res = min(res, solve( x , position + 1) + 1 );
   }
   return din[engine ][ position ] = res;    
}

main(){
  int x, casos, set, res;
  freopen("rata.in","r",stdin);
  freopen("salida.out","w", stdout);
  for( gets(line), sscanf(line, "%d", &casos), set = 1; set <= casos && gets(line) && sscanf(line, "%d", &n) ; set++){
     for( x = 0; x < n; x++){
        gets(line);
        strcpy( eng[ x ] , line );
     }
     gets( line); sscanf(line, "%d", &m);
     for( x = 0; x < m; x++)
       gets( list[x]);
     res = (1<<22);
     memset( din, -1, sizeof( din ));
     for( x = 0; x < n; x++)
       res = min(res, solve( x, 0 ));
     printf("Case #%d: %d\n", set, res);
  }
  return 0;       
}
