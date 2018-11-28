#include<iostream>
using namespace std;

void solve(int poss)
{
    int n, r, k;
    int a[2048];
    int pos[2048];
    int suma[2048];
    
    scanf("%d%d%d" , &r, &k, &n);
    for( int i = 0; i < n; ++i ) scanf( "%d", &a[i] );
    for( int j = 0; j < n; ++j ) a[n+j] = a[j];
    
    for( int i = 0; i < n; ++i )
    {
     int sum = 0;
     for( int j = i; j < i + n; ++j )
     {
      sum += a[j];  
      if( sum <= k ) { pos[i] = j % n; suma[i] = sum; }
      else break;
     }
     
     //printf("suma %d\n",suma[i]);
    }

     int xpos = 0;
     long long ans = 0;
     
     for( int i = 0; i < r; ++i )
     {
        ans += suma[xpos];
        xpos = ( pos[xpos] + 1 ) % n;
     }
     
     printf("Case #%d: %I64d\n",poss,ans);
}
int main()
{
    int t, ;
    scanf("%d", &t);
    for(int i = 1; i <= t; ++i)solve(i);
    return 0;
}
