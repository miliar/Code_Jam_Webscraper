#include<stdio.h>
#include<string.h>
#include<cmath>
#include<algorithm>
#include<queue>
#include<iostream>
using namespace std;
typedef long long LL;
const int maxn = 555;
#define mp make_pair
int cas = 0;
int mat[ maxn ][ maxn ];
LL sum[ maxn ][ maxn ];
pair< LL, LL > vecsum[ maxn ][ maxn ];
int n, m, D;
typedef pair< LL, LL> PLL;
pair< LL, LL> operator + ( PLL a, PLL b) {
         return mp( a.first + b.first, a.second + b.second );  
}

pair< LL, LL> operator - ( PLL a, PLL b) {
         return mp( a.first - b.first, a.second - b.second );  
}

pair< LL, LL> operator * ( PLL a, LL b) {
         return mp( a.first * b, a.second * b );  
}

void dp(){
     int i, j;
     for(i = 1; i <= n; ++ i)
           for(j = 1; j <=m; ++ j) {
                 sum[ i ][ j ] = sum[ i - 1] [ j ] + sum[i ][j - 1] - sum[i - 1][j - 1] + D + mat[i][j];      
           } 
     for(i = 1; i <= n; ++ i)
           for(j = 1; j <=m; ++ j) {
                 vecsum[ i ][ j ] = vecsum[ i - 1][ j ] + vecsum[ i ][ j - 1] - vecsum[ i - 1][j - 1] + 
                  (mp((LL)i + i, (LL)j + j) * ((LL)D + mat[i][j]));      
           }    
}

void get(){ 
     cin >> n >> m >> D;
     int i, j;
     memset( sum, 0, sizeof sum);
     
     for(i = 1; i <= n; ++ i) 
      for(j = 1; j <= m; ++ j){
            scanf("%1d", &mat[i][j]);      
      }
      dp();
}

LL get_sum( int x, int y, int len){
   return sum[ x + len - 1][ y + len - 1]
    + sum[ x - 1][ y - 1]
    - sum[ x + len - 1][y - 1]
    - sum[ x - 1][ y + len - 1];            
}

PLL get_vec_sum( int x, int y, int len){
     return vecsum[ x + len - 1][ y + len - 1]
    + vecsum[ x - 1][ y - 1]
    - vecsum[ x + len - 1][y - 1]
    - vecsum[ x - 1][ y + len - 1];     
}

PLL SS(int x, int y){
    return mp((LL)x + x, (LL)y + y) * ((LL)D + mat[x][y]);    
}
bool ok(int x, int y, int len){
     int mx, my;
     -- len;
     mx = x + x  + len ;
     my = y + y + len;
     PLL cc = mp( mx, my);
     ++ len;
     LL tot_sum =   get_sum( x, y, len);
     
     tot_sum -= (LL)D * 4;
     tot_sum -= mat[ x ][ y ] + mat[x][y + len - 1] + mat[x + len-1][y] + mat[x+len-1][y+len-1];
     //if(x == 1 && y == 1 && len == 2) cout << mx<<'_' << my << endl;
     //if(x == 1 && y == 1 && len == 2) cout << "t_sum = " << tot_sum << endl;
     PLL pmul =  get_vec_sum( x, y, len);
     //if(x == 1 && y == 1 && len == 2) cout << "!!!!!" << pmul.first <<'_' << pmul.second << endl;
     pmul = pmul -  SS(x, y);
     pmul = pmul -  SS( x + len - 1, y );
     pmul = pmul -  SS( x , y + len - 1);
     pmul = pmul -  SS( x + len - 1 , y + len - 1 ); 
     //if(x == 1 && y == 1 && len == 3) cout << "!!!!!" << pmul.first <<'_' << pmul.second << endl;
     pmul = pmul - (cc * tot_sum);
     //if(x == 1 && y == 1 && len == 3) cout << pmul.first <<'_' << pmul.second << endl;
     return pmul.first == 0 && pmul.second == 0;
}

void work(){
     ++ cas;
     int i, j, k, best = - 1;
     for(i = 1; i <= n; ++ i)
           for(j = 1; j <= m; ++ j) {
                for(k = 3; i + k <= n + 1 && j + k <= m + 1 ; ++ k) 
                      if(ok(i, j, k)) best = max( best, k );      
           }
     printf("Case #%d: ", cas);
     if( best == -1) puts("IMPOSSIBLE"); 
     else cout << best << endl;
}

int main(){
    freopen("D:\\B-large.in","r",stdin);
    freopen("D:\\out.txt","w",stdout);
    int T;
    cin >> T;
    while(T --){
         get();
         work();           
    }
	return 0;
}
