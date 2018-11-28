#include <iostream>
#include<cstdio>

using namespace std;


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    char ch[10];
    int i,onum,bnum,Maxb,Maxo,n,t,x,m=1,preo,preb,temp;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        preb=1;
        preo=1;
        for(i=0,Maxo=0,Maxb=0;i<n;i++)
        {
            scanf("%s%d",ch,&x);
            if(ch[0]=='O')
            {
                temp=x-preo;
                if(temp<0)temp=-temp;
                if(temp+Maxo<Maxb)Maxo=Maxb+1;
                else Maxo+=temp+1;
                preo=x;
            }
            else
            {
                temp=x-preb;
                if(temp<0)temp=-temp;
                if(temp+Maxb<Maxo)Maxb=Maxo+1;
                else Maxb+=temp+1;
                preb=x;
            }
        }
        printf("Case #%d: %d\n",m++,max(Maxb,Maxo));
    }
    return 0;
}
