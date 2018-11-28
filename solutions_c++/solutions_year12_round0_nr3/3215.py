#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cstdio>
using namespace std;
char s[20];
bool bo[2100000];
int main()
{
   freopen("C-small-attempt1.in","r",stdin);
   freopen("C-small-attempt1.out","w",stdout);
    int t,a,b;
    scanf("%d",&t);
    for (int i=0; i<t; i++)
    {
        printf("Case #%d: ",i+1);
        int ans=0;
        scanf("%d%d",&a,&b);
        for (int p=a; p<=b; ++p)
        {
            memset(bo,0,sizeof(bo));
            itoa(p,s,10);
            int len=strlen(s);
            for (int j=1;j<len;j++)
            {
                char tmps[20];
                for (int k=j;k<len;k++)
                    tmps[k-j]=s[k];
                for (int k=0;k<j;k++)
                    tmps[len-j+k]=s[k];
                tmps[len]=0;
                //cout<<tmps<<endl;
                int num;
                num=atoi(tmps);

                if ( num<=b && num>p && bo[num]==false)
                {
                     //cout<<p<<"  "<<num<<endl;
                    ans++;
                    bo[num]=true;
                }
            }
        }
        cout<<ans<<endl;
    }
    return 0;
}
