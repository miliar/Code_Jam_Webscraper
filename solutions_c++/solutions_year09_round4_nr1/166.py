#include <stdio.h>
#include <algorithm>
#include <memory.h>
using namespace std;
int a[50];
int tests;
int s[50];
int tmp[50];
char st[100];
int n;
int main()
{
    freopen("a2.in","r",stdin);
    freopen("a2.out","w",stdout);
    scanf("%d",&tests);
    for (int t0=1;t0<=tests;t0++)
    {
        memset(s,0,sizeof(s));
        scanf("%d",&n);
        for (int i=0;i<n;i++)
        {
          scanf("%s",st);
          a[i]=0;
          for (int j=0;j<n;j++)
          {
              if (st[j]=='1') a[i]=j;    
          }
          s[a[i]]++;
        }
        int ans=0;
        for (int i=n-1;i>=0;i--)
        {
            int j;
            memcpy(tmp,a,sizeof(a));
            for (j=i;j>=0;j--)
            {
                memcpy(a,tmp,sizeof(tmp));
                a[j]=i;
                sort(a,a+i+1);      
//                s[a[j]]--;
                int s0=0;
                for (int k=0;k<=i;k++)
                {
                    if (a[k]>k) s0=-1;
                }
                if (s0==-1) continue;
                break;
            }
            memcpy(a,tmp,sizeof(tmp));
            for (;j<i;j++) a[j]=a[j+1],ans++;
            memset(s,0,sizeof(s));
            for (j=0;j<i;j++) s[a[j]]++;       
        }
        printf("Case #%d: %d\n",t0,ans);
    }
}
