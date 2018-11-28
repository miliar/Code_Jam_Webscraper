#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <stack>

using namespace std;

char grid[200+1][200+1];
int k;


void imprime(int n){
for( int i=0;i<n;i++,putchar('\n') )
    for( int j=0;j<n;j++ )
	   printf("%c",grid[i][j]);
  return ;
}

void rotar(int n){
  char nueva[n][n];
  int c1=0, c2=0;
  for( int i=0;i<n;i++ )
    for( int j=0;j<n;j++ )
	 nueva[i][j]=grid[j][i];
  for( int i=0;i<n;i++ )
    for( int j=0;j<n;j++ )
	 grid[i][j]=nueva[i][n-j-1];
  return ;

}

int horizq(int r, int c, char A){
  int  cont=0;
  for(int  i=0;i<k;i++ )
    if( grid[r][c-i]==A  ) cont++;
  if( cont==k ) return 1;
  return 0;
}

int horder(int r, int c, char A){
  int  cont=0;
  for( int i=0;i<k;i++ )
    if( grid[r][c+i]==A  ) cont++;
  if( cont==k ) return 1;
  return 0;
}

int verup(int r, int c, char A){
  int cont=0;
  for(int i=0;i<k;i++ )
    if( grid[r-i][c]==A  ) cont++;
  if( cont==k ) return 1;
  return 0;
}

int verlow(int r, int c, char A){
  int cont =0;
  for( int i=0;i<k;i++ )
    if( grid[r+i][c]==A  ) cont++;
  if( cont==k ) return 1;
  return 0;
}

int d1(int r, int c, char A){
  int cont =0;
  for( int i=0;i<k;i++ )
    if( grid[r-i][c-i]==A  ) cont++;
  if( cont==k ) return 1;
  return 0;
}

int d2(int r, int c, char A){
  int cont =0;
  for( int i=0;i<k;i++ )
    if( grid[r-i][c+i]==A  ) cont++;
  if( cont==k ) return 1;
  return 0;
}

int d3(int r, int c, char A){
  int cont=0;
  for( int i=0;i<k;i++ )
    if( grid[r+i][c-i]==A  ) cont++;
  if( cont==k ) return 1;
  return 0;
}

int d4(int r, int c, char A){
  int  cont=0;
  for(int  i=0;i<k;i++ )
    if( grid[r+i][c+i]==A  ) cont++;
  if( cont==k ) return 1;
  return 0;
}

int cuenta(int n, char A){
  int sol=0;
  for( int i=0;i<n;i++ )
    for( int j=0;j<n;j++ ){
	 if( i>=k-1 ) sol=sol+horizq(i,j,A);
	 if( i<=n-k+1 ) sol=sol+horder(i,j,A);
	 if( j>=k-1 ) sol=sol+verup(i,j,A);
	 if( j<=n-k+1 ) sol=sol+verlow(i,j,A);  
	 if( i>=k-1  && j>=k-1 ) sol=sol+d1(i,j,A);
	 if( i>=k-1 && j<=n-k+1 ) sol=sol+d2(i,j,A);
	 if( i<=n-k+1 && j>=k-1 ) sol=sol+d3(i,j,A);
	 if( i<=n-k+1 && j<=n-k+1 ) sol=sol+d4(i,j,A);
    }
  return sol;
}


void gravedad(int n){
  char nueva[n][n];
  for( int i=n-1;i>=0;i-- )
    for( int j=n-1;j>=0;j-- )
	  if( grid[i][j]=='R' || grid[i][j]=='B' ){
		char actual=grid[i][j];
		int d=i+1;
		while( d<n && grid[d][j]=='.'  ){
		    grid[d-1][j]='.';
		    d++;   
		}
		grid[d-1][j]=actual;
	   } 
  return ;
}


int main(){
  freopen("entrada.in","r",stdin);
  freopen("salida.out","w",stdout);
  int T, n;
  char c;
  scanf("%d", &T);
  for( int I=1;I<=T;I++){
    scanf("%d%d\n",&n, &k);
    for(int i=0;i<201;i++)
	 for(int j=0;j<201;j++)
	   grid[i][j]='.';
    for( int i=0;i<n;i++,scanf("%c",&c) )
	 for( int j=0;j<n;j++ )
		scanf("%c",&grid[i][j]);
    rotar(n);
    
    gravedad(n);
    //imprime(n);
    int red=0, blue=0;
    red=cuenta(n,'R');
    blue=cuenta(n,'B');
    
    printf("Case #%d: ",I);
    if( red>=1 ){
	 if( blue>=1 )
		printf("Both\n");
	 else printf("Red\n");
    }
    else{
	   if( blue>=1 )
		printf("Blue\n");
		else printf("Neither\n");
    }
  }
  

  return 0;
}
