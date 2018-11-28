#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;

int t,n;
char who[110];
int p[110];
int po,pb,no,nb;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("al1.txt","w",stdout);
    int i,j;
    scanf("%d",&t);
    int cas=1;
    while(t--)
    {
        scanf("%d",&n);
        po=pb=1;
        no=nb=1;
        int ans=0;
        for(i=0;i<n;i++)
            scanf(" %c %d",&who[i],&p[i]);
        
        for(i=0;i<n;i++)
        {
            if(who[i]=='O')
            {
                po=p[i];
                for(j=i+1;j<n;j++)
                {
                    if(who[j]=='B')
                    {
                        pb=p[j];
                        break;
                    }
                }
                
                while(po!=no)
                {
                    if(po>no)
                        no++;
                    if(po<no)
                        no--;
                    if(pb>nb)
                        nb++;
                    if(pb<nb)
                        nb--;
                    ans++;
                }
                if(pb>nb)
                    nb++;
                if(pb<nb)
                    nb--;
                ans++;
            }
            else
            {
                pb=p[i];
                for(j=i+1;j<n;j++)
                {
                    if(who[j]=='O')
                    {
                        po=p[j];
                        break;
                    }
                }
                while(pb!=nb)
                {
                    if(po>no)
                        no++;
                    if(po<no)
                        no--;
                    if(pb>nb)
                        nb++;
                    if(pb<nb)
                        nb--;
                    ans++;
                }
                if(po>no)
                    no++;
                if(po<no)
                    no--;
                ans++;
            }
            //printf(" %d %d %d %d  %d\n",po,no,pb,nb,ans);
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
    //system("pause");
    return 0;
}
