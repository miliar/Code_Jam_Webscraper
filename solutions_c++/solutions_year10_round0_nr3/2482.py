#include <iostream>

using namespace std;

#define LL __int64
const int maxn=1010;
int R,k,n;
int g[maxn];
LL sum=0;

int main()
{
    freopen("C-small-attempt0.in","r",stdin );
    freopen("Cs.txt","w",stdout );
    int cnt;
    cin>>cnt;
    int cs=0;
    while(cnt--){
        scanf("%d %d %d",&R, &k, &n);
        for(int i=0; i<n; i++ )
            scanf("%d", &g[i] );
        int front=0; int rear=n-1;
        sum = 0;
        for(int i=0; i<R; i++ ){
            int tmp=0;
            int J;
            for(J=front; J<=rear; J++ ){
                if( tmp + g[J % n] > k ) break;
                tmp = tmp + g[J % n];
            }
            front = J;  rear = front + n- 1;
            sum +=tmp;
//            printf("pos %d, sum %I64d\n", p, sum );
        }

        printf("Case #%d: %I64d\n", ++cs, sum );
    }
    return 0;
}
