#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#define MAXL 1000
using namespace std;

char s1[MAXL+1],s2[MAXL+1];
int pos[MAXL+1];
int n,len,cnt,ans;

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    int c,i,j,k,t,factorial;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        scanf("%d",&n);
        scanf("%s",s1);
        factorial=1;
        for(i=0;i<n;i++)
        {
            pos[i]=i;
            factorial=factorial*(i+1);
        }
        len=strlen(s1);
        ans=1000000000;
        for(i=0;i<factorial;i++)
        {
            for(j=0;j<len;j=j+n)
            {
                for(k=0;k<n;k++)
                {
                    s2[j+k]=s1[j+pos[k]];
                }
            }
            cnt=1;
            for(j=1;j<len;j++)
            {
                if(s2[j]!=s2[j-1])
                {
                    cnt++;
                }
            }
            ans=min(ans,cnt);
            next_permutation(pos,pos+n);
        }
        printf("Case #%d: %d\n",c+1,ans);
    }
    return 0;
}
