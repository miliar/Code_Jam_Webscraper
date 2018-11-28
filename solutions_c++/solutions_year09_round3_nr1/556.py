#include <iostream>
#include <cstring>
using namespace std;
char a[101]={0};
int b[101]={0},len=0;
int d[301]={0};
long long ans(int x)
{
    long long i,j,cnt=1;
    long long aa=0;
    for(i=len-1;i>=0;i--)
    {
            aa+=cnt*b[i];
            cnt*=x;
    }
    return aa;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("xout.txt","w",stdout);
    int i,j,cnt,t,Cs=1;
    cin>>t;
    while(t--)
    {
        bool used[301]={false};
        memset(d,0,sizeof(d));
        printf("Case #%d: ",Cs++);
        char c='\0';
        getchar();
        scanf("%s",a);
        len=strlen(a);
        cnt=0;
        b[0]=1;
        used[int(a[0])]=true;
        d[int (a[0])]=1;
        for(i=1;i<len;i++)
        {
            if(!used[int(a[i])])
            {
                if(cnt==1)cnt++;
                b[i]=cnt++;

                used[int(a[i])]=true;
                d[int (a[i])]=cnt-1;
            }
            else b[i]=d[int(a[i])];
        }
        if(cnt<=1)cnt=2;
        printf("%lld\n",ans(cnt));
    }

    return 0;
}
