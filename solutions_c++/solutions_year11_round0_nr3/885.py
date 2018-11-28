#include <string>
//#include <fstream>
#include <stdio.h>
using namespace std;

bool ok;
int res;

void solve(){
    int n;

    scanf("%d", &n);

    int min=1000000000;
    int sum=0;
    int or=-1;
    for( int i=0;i<n;i++){
         int c;
         scanf("%d", &c);
         if( min>c )
                  min=c;
         if( or==-1)
             or=c;
         else
             or^=c;
         sum+=c;
    }
    if( or!=0 )
        ok=false;
    else{
        res= sum-min;
		ok=true;
	}
}

int main(){
    freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    
    for( int i=1; i<=T; i++){
		
         printf("Case #%d: ", i);
		 solve();
		 if(ok)
			 printf("%d", res);
		 else
			 printf("NO");
		 printf("\n");
	}
}
