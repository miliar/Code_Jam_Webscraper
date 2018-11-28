#include <iostream>

using namespace std;

#define N 1001

long long g[N];

long long flag[N], sum[N];

int main(){
    
    int tc, Tc;
    
//    freopen( "C-large.in", "r", stdin );
//    freopen( "c.large.out.txt", "w", stdout );
    
    scanf( "%d", &Tc );
    
    long long R, K;
    int n;
    
    for( tc = 1; tc <= Tc; tc++ ){
         
         scanf( "%I64d%I64d%d\n", &R, &K, &n );
         
         long long s = 0;
         for( int i = 0; i < n; i++ ){
              scanf( "%I64d", g + i );
              s += g[i];
         }
         
         if( s <= K ){
				printf( "Case #%d: %I64d\n", tc, s * R );
				continue;
		}
         for( int i = 0; i < n + 1; i++ ){
              flag[i] = -1;
              sum[i] = 0;
         }
         
         int index = 0;
         long long min, loop, sumloop;
         
         for( int i = 0; i <= n; i++ ){
/*
				for( int j = 0; j <= n; j++ ){
					cout<<flag[j]<<" ";
				}
				cout<<endl;
*/				
              if( flag[index] >= 0 ){
                  min = flag[index];
                  loop = i - flag[index];
                  sumloop = sum[i - 1];
                  if( flag[index] != 0 ){
                      sumloop -= sum[flag[index] - 1];
                  }
                  break;
              }
              
              flag[index] = i;
              long long ans = 0;
              for( int j = index; ; j = ( j + 1 ) % n ){
                   ans += g[j];
                   if( ans > K ){
                       ans -= g[j];
                       index = j;
//                       cout<<"index="<<index<<endl;
                       if( i == 0 ){
                           sum[i] = ans;
                       }
                       else{
                            sum[i] = sum[i - 1] + ans;
                       }
                       break;
                   }
              }
         }
/*         
         cout<< min<<" "<<loop<<" "<<sumloop<<endl;
         for( int i = 0; i < n; i++ ){
				cout<<sum[i]<<" ";
		}
		cout<<endl;
*/         
         long long ans = 0;
         if( R < min ){
             ans = sum[R];
         }
         else{
              if( min > 0 ){
                  ans += sum[min - 1];
                  R -= min;
//                  cout<<ans<<" "<<R<<" "<<min<<endl;
                  ans += R / loop * sumloop;
//                  cout<<"ans="<<ans<<endl;
                  ans += sum[ min - 1 + ( R % loop )] - sum[min - 1];
              }
              else{
					R--;
					ans = R / loop * sumloop + sum[R % loop];
				}
         }
         
         printf( "Case #%d: %I64d\n", tc, ans );
    }
    
    return 0;
}

              
         
    
