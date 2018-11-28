#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

bool mark[10000001];
int T;
long long n;

int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%d",&T);
    memset(mark,0,sizeof(mark));
    for (int i=2;i<=10000000;i++) if (!mark[i]){
        for (int j=2;j<=10000000/i;j++) mark[i*j]=1;
    }
    for (int Case=1;Case<=T;Case++){
        scanf("%I64d",&n);if (n==1){printf("Case #%d: %d\n",Case,0);continue;}
        int numx=0,numn=0;
        for (int i=2;i<=sqrt(n);i++) if (!mark[i]){
            numn++;
            long long now=1;
            for (int j=1;j<=1000;j++){
                now*=i;if (now>n){numx+=j-1;break;}
            }
        }   
        printf("Case #%d: %d\n",Case,numx-numn+1);
    }
}
