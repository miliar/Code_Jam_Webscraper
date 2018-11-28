#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
using namespace std;
int n,b[110],o[110],c[110],T;
void Init()
{
     scanf("%d%*c",&n);
     b[0]=o[0]=1;
     for(int i=0;i!=n;++i)
     {
        char ch;
        scanf("%c",&ch);
        if(ch=='O')
        {
           scanf("%d%*c",&o[o[0]++]);
           c[i]=0;
        }
        else
        {
           scanf("%d%*c",&b[b[0]++]);
           c[i]=1;
        }
     }
}
void Work()
{
     int nowo=1,nowb=1,po=1,pb=1,ans=0;
     for(int i=0;i!=n;++i)
        if(c[i]==0)
        {
           int temp=abs(o[po]-nowo)+1;
           nowo=o[po];
           ans+=temp;
           if(pb!=b[0])
           {
              if(abs(b[pb]-nowb)<=temp) nowb=b[pb];else
              if(nowb>b[pb]) nowb-=temp;else nowb+=temp;
           }
           ++po;
        }
        else
        {
           int temp=abs(b[pb]-nowb)+1;
           nowb=b[pb];
           ans+=temp;
           if(po!=o[0])
           {
              if(abs(o[po]-nowo)<=temp) nowo=o[po];else
              if(nowo>o[po]) nowo-=temp;else nowo+=temp;
           }
           ++pb;
        }
     printf("Case #%d: %d\n",T,ans);
}
int main()
{
    int TT;
    scanf("%d",&TT);
    for(T=1;T<=TT;++T)
    {
       Init();
       Work();
    }
    return 0;
}
