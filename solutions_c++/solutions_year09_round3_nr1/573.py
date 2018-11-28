#include <iostream>
#include <cstring>
using namespace std;
char a[101]={'\0'};
int b[101]={0},len=0;
int d[301]={0};
long long ans(int x)
{
    long long i,j,k=1;
    long long aa=0;
    for(i=len-1;i>=0;i--)
    {
            aa+=k*b[i];
            k*=x;
    }
    return aa;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int i,j,k,t,Cs=1;
    cin>>t;
    while(t--)
    {
        bool v[301]={false};
        memset(d,0,sizeof(d));
        printf("Case #%d: ",Cs++);
        char c='\0';
        getchar();
        scanf("%s",a);
//        cout<<a<<endl;
        len=strlen(a);
        k=0;
        b[0]=1;
        v[int(a[0])]=true;
        d[int (a[0])]=1;
        for(i=1;i<len;i++)
        {
            if(!v[int(a[i])])
            {
                if(k==1)k++;
                b[i]=k++;

                v[int(a[i])]=true;
                d[int (a[i])]=k-1;
            }
            else b[i]=d[int(a[i])];
        }
        if(k<=1)k=2;
//        for(i=0;i<len;i++)cout<<b[i];
//        cout<<endl<<k<<endl;;
        printf("%lld\n",ans(k));
    }

    return 0;
}
