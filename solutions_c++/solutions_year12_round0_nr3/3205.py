#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<map>
#include<set>
#include<queue>
#include<string>
#include<vector>
#include<ctime>
using namespace std;
int ten[10]={1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000};
bool bo[2000005];
int aa[2000005];
int L(int n)
{
    if(n==0)return 1;
    int res=0;
    while(n)
    {
        n/=10;
        res++;
    }
    return res;
}
void gao(int n,int &num,int len,int a,int b)
{
    if(bo[n] && n>=a && n<=b)
    {
        num++;
        return;
    }
    bo[n]=1;
    int res=n/10+n%10*ten[len-1];
    //cout<<n<<' '<<res<<endl;
    if(n>=a && n<=b)aa[num]++;
    gao(res,num,len,a,b);
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-out.out","w",stdout);
    int t,tt=0,a,b,len,num,sum,i;
    scanf("%d",&t);
    while(t--)
    {
        tt++;
        sum=0;
        scanf("%d%d",&a,&b);
        len=L(a);
        memset(bo,0,sizeof(bo));
        memset(aa,0,sizeof(aa));
        num=0;
        for(i=a;i<=b;i++)
            if(!bo[i])
                gao(i,num,len,a,b);
        for(i=0;i<num;i++)sum+=aa[i]*(aa[i]-1)/2;
        printf("Case #%d: %d\n",tt,sum);
    }
    return 0;
}
