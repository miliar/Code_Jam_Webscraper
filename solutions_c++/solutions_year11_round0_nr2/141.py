#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
char s[1111];
int mp[221][221];
bool cause[221][221];
int i,j,k,n,m;
int main()
{
    int cs,q=0;
    freopen("B-large.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&cs);
    while (cs--)
    {
        memset(mp,0,sizeof(mp));
        memset(cause,0,sizeof(cause));
        scanf("%d",&n);
        char ch1,ch2,ch3;
        for (i=1;i<=n;i++)
        {
            cin>>ch1>>ch2>>ch3;
            mp[ch1][ch2]=mp[ch2][ch1]=ch3;
        }
        scanf("%d",&m);
        for (i=1;i<=m;i++)
        {
            cin>>ch1>>ch2;
            cause[ch1][ch2]=cause[ch2][ch1]=true;
        }
        scanf("%d",&n);
        m=0;
        for (i=1;i<=n;i++)
        {
            cin>>ch1;
            if (m==0)
            {
               s[m++]=ch1;
            }
            else if (mp[ch1][s[m-1]]!=0)
            {
               s[m-1]=mp[ch1][s[m-1]];
            }
            else
            {
               bool flag=true;
               for (j=m-1;j>=0;j--)
               if (cause[ch1][s[j]])
               {
                  flag=false;
                  m=0;
                  break;
               }
               if (flag)
               s[m++]=ch1;
            }
        }
        s[m]=0;
        printf("Case #%d: [",++q);
        if (m!=0) printf("%c",s[0]);
        for (i=1;i<m;i++)
        printf(", %c",s[i]);
        puts("]");
    }
}
