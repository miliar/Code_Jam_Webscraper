#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
bool a[100],b[100];
int n,k;

int main(){
    freopen("A-small.in","r",stdin);
    freopen("A-small.out","w",stdout);
    int test,cas,i,j,n,k;
    scanf("%d",&test);
    for( cas=1; cas<=test; cas++){
        scanf("%d%d",&n,&k);
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        a[1]=true;
        while( k-- ){
            for( i=n; i>0; i-- )
                if( a[i] ){
                    if( b[i] ){
                        b[i]=false;
                        for( j=i+1; j<=n; j++) a[j]=false;
                    }
                    else
                    if( !b[i] ){
                        b[i]=true;
                        j=i;
                        while( j<=n&&b[j] ){
                            j++;
                            a[j]=true;
                        }
                    }
                }
                else
                if( !a[i] )
                    for( j=i; j<=n; j++) a[j]=false;
        }
        if( a[n]&&b[n] ) printf("Case #%d: ON\n",cas);
        else printf("Case #%d: OFF\n",cas);
    }
    return 0;
}
