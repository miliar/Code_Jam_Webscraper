#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int gcd( int a, int b ){
	 if(a==0) return b;
    if(b==0) return a;
	 while( b>0 ){
	 		  a%=b;
			  a^=b^=a^=b;	 		  
    }
	 return a;
}

int main(){
    freopen("in.txt", "r", stdin);
    freopen("salida.out", "w", stdout);
    
    int ncases, n, t;
    
    scanf("%d", &ncases);
    for( int i=1;i<=ncases;i++ ){
         scanf("%d", &n);     
         vector<int> A, B;
         for( int j=0;j<n;j++ ){
              scanf("%d", &t);
              A.push_back(t);
         }
         sort( A.begin(), A.end() ); 
         for( int ii=0;ii<n;ii++ )
              for( int jj=ii+1;jj<n;jj++ )
                   B.push_back(A[jj]-A[ii]);
         int tam=B.size();
         int sol=B[0];
         for( int j=0;j<tam;j++ )
              sol=gcd(sol,B[j]);
         int max=-1;
         for( int j=0;j<n;j++ ){
              int m=A[j]%sol, s;
              if( m==0 )s=0;
              else s=sol-m;
              max=( max>s?max:s );
         }
         printf("Case #%d: %d\n",i, max);
              
    }
    return 0;
}

