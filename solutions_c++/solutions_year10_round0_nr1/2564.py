#include <iostream>

using namespace std;

#define LL __int64
int n;
LL k;
LL b[100];
int main()
{
    freopen("large.in","r",stdin );
    freopen("largeO.txt","w",stdout );
    b[0] = 1;
    for(int i=1; i<40; i++ )
        b[i] = b[i-1]*2;
    int cnt;
    cin>>cnt;
    int cs=0;
    while(cnt--){
        scanf("%d %I64d",&n, &k);
        if( (k+1)%b[n]==0 )
            printf("Case #%d: ON\n",++cs);
        else
            printf("Case #%d: OFF\n",++cs );
    }
    return 0;
}
