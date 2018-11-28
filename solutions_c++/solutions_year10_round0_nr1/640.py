#include <iostream>

using namespace std;

bool solve( int n,int k ){
    if( k==0 ) return 0;
    k=k%(1<<n);
    if( k==(1<<n)-1 ) return 1;
    else return 0;
}
int main()
{
    int tn;
    scanf("%d",&tn);
    for( int i=1;i<=tn;++i ){
        int N,K;
        scanf("%d%d",&N,&K);
        printf("Case #%d: ",i);
        if( solve( N,K ) ) printf("ON\n");
        else printf("OFF\n");
    }
    return 0;
}
