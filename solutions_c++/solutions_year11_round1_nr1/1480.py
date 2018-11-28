#include<cstdio>
#include<cstring>
#define abs(x) ((x)<0?-(x):(x))
#define min(x,y) (x<y?x:y)
#define clr(a,b) memset(a,b,sizeof(a))

using namespace std;

int T,n;
int a,b;

void init()
{
    scanf("%d%d%d",&n,&a,&b);
}

int gcd(int p,int q)
{
    if (p%q==0)
        return q;
    else
        return gcd(q,p%q);
}

bool work()
{
    if (b==0&&a==0)
        return true;
    if (b==0&&a!=0)
        return false;
    int t,x,y,e,ne;
    ne=0;
    for (int d=1;d<=n;d++){
        if ((d*a)%100==0){
            x=d*a/100;
//            printf("!%d %d\n",x,d);
            t=gcd(100,b);
//            printf("!%d\n",t);
            int p=b/t,q=100/t;
            int tp=p,tq=q;
            e=0;
            while (p-x<0||q-d<0){
                p+=tp,q+=tq;
            }

            while ((p-x)<=(q-d)){
                if (p-x>=0&&q-d>=0){
//                    printf("#%d %d\n",p,q);
                    e=1;
                    break;
                }
                p+=tp;q+=tq;
            }
            if (e==1){
                ne=1;
                break;
            }
        }
    }
    if (ne==1)
        return true;
    else
        return false;
}

int main()
{
    FILE *cin=freopen("1A.txt", "w", stdout);
    scanf("%d",&T);
    for (int tnum=1;tnum<=T;tnum++){
        init();
        if (work())
            printf("Case #%d: Possible\n",tnum);
        else
            printf("Case #%d: Broken\n",tnum);

    }
}
