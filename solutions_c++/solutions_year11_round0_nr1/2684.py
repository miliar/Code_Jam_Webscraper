#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
#define abs(x) ((x) > 0 ? (x) : -(x))
const int maxn=10+2;
int T, N;
int A[maxn];
char buf[maxn][2];
int x1,x2,t1,t2;

void getin()
{
    scanf("%d",&N);
    for (int i=1;i<=N;i++) scanf("%s%d",buf[i],&A[i]);
}

void work()
{
    x1=A[1]; x2=1;
    t1=0; t2=A[1]-1+1; 
    for (int i=2;i<=N;i++)
    {
        if (buf[i][0]==buf[i-1][0])
        {
            t2+=abs(A[i]-x1)+1;
            x1=A[i];
        }
        else
        {
            int temp=x1; x1=x2; x2=temp;
            if (abs(A[i]-x1)>t2-t1)
            {
                int temp=t2;
                t2=t2+abs(A[i]-x1)-(t2-t1);
                t1=temp;
                t2++;
            }
            else
            {
                t1=t2;
                t2++;
            }
            x1=A[i];
        }
    }
    printf("%d\n",t2);
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("yy.out","w",stdout);
    scanf("%d",&T);
    for (int ii=1;ii<=T;ii++)
    {
        printf("Case #%d: ",ii);
        getin();
        work();
    }
    return 0;
}
