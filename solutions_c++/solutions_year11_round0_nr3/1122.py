# include <string>
# include <stdio.h>
# include <algorithm>
# include <map>

using namespace std;

typedef struct { int a, b, c; } VALUE;


bool  operator < ( VALUE a, VALUE b ){
  if( a.a != b.a ) return a.a < b.a;
  return a.b < b.b;
}

map<VALUE, int > hash[1001];
map<VALUE, bool > vis[1001];
int n, list[2000];

int solve(int position, VALUE value){
  int a = value.a, b = value.b,c = value.c, res = -(1<<25), t;
  if( position >= n ){
    if( a == b && c == 3) return 0;
    return -(1<<25);
  }
  if( vis[ position ][ value ] == true ) return hash[ position ][ value ];
  vis[position][ value ] = true;
  /* Patrick pile */
  VALUE tmp;
  tmp.a = a ^ list[ position ];
  tmp.b = b;
  tmp.c = c | (1<<0);
  t = solve( position + 1 , tmp ) + list[ position ];
  if( t < 0 ) t = -(1<<25);
  res = max( res,  t );
  tmp.a = a;
  tmp.b = b ^ list[ position ];
  tmp.c = c | (1<<1);
  t = solve( position + 1 , tmp );
  if( t < 0 ) t = -(1<<25);
  res = max( res,  t );
  return hash[position][value] = res;
}

main(){
  int x, res, ncases, cases;
  for(scanf("%d", &ncases), cases = 1; cases <= ncases; cases++ ){
     scanf("%d", &n);
     for( x = 0; x< 1000; x++){
       map <VALUE, bool> vistmp;
       vis[x] = vistmp;
     }
     for( x = 0; x <n  ; x++) scanf("%d", &list[ x ]);
     VALUE a;
     a.a = 0;
     a.b = 0;
     a.c = 0;
     res = solve( 0, a);
     if( res < 0 ) printf("Case #%d: NO\n", cases);
     else printf("Case #%d: %d\n", cases, res);
  }
  return 0;	
}