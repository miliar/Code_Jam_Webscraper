#include<iostream>
#include<cstdio>
#include<cmath>
#include<string.h>
#include<string>
#include<algorithm>
using namespace std;

int bit[100],temp[100],i,j,pos,x,y,a,b,k,T,ans,s;

int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    scanf("%d",&T);
    for (int tt=1;tt<=T;tt++)
    {
        scanf("%d%d",&a,&b);
        ans=0;
        for (i=a;i<b;i++)
        {
            x=i; pos=0; s=0;
            memset(bit,0,sizeof(bit));
            while (x)
            {
                  bit[pos++]=x%10; x/=10;
                  }
            for (j=0;j<pos-1;j++)
            {
                if (bit[j]==0) continue;
                y=bit[j];
                k=j-1;
                if (k<0) k=pos-1;
                while (k!=j)
                {
                      y*=10; y+=bit[k];
                      k--;
                      if (k<0) k=pos-1;
                      }
                if (y>i&&y<=b) temp[s++]=y;
            }
            for (j=0;j<s-1;j++)
                for (k=1;k<s;k++)
                if (temp[j]>temp[k]) swap(temp[j],temp[k]);
            for (j=0;j<s;j++)
            {
                while (temp[j]==temp[j+1]) j++;
                ans++;
  //              printf("%d %d\n",i,temp[j]);
            }
        }
        printf("Case #%d: %d\n",tt,ans);
    }
    return 0;
}
