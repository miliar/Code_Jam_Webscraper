#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;

int t;
int c,d,n;
char tmp[5];
char s[110];
int mp[28][28];
int mp1[28][28];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("bl1.txt","w",stdout);
    int i,j;
    scanf("%d",&t);
    int cas=1;
    while(t--)
    {
        memset(mp,-1,sizeof(mp));
        memset(mp1,-1,sizeof(mp1));
        scanf("%d",&c);
        for(i=0;i<c;i++)
        {
            scanf("%s",tmp);
            mp[tmp[0]-'A'][tmp[1]-'A']=mp[tmp[1]-'A'][tmp[0]-'A']=tmp[2];
        }
        scanf("%d",&d);
        for(i=0;i<d;i++)
        {
            scanf("%s",tmp);
            mp1[tmp[0]-'A'][tmp[1]-'A']=mp1[tmp[1]-'A'][tmp[0]-'A']=0;
        }
        scanf("%d",&n);
        scanf("%s",s);
        for(i=1;i<n;i++)
        {
            if(s[i-1]!='*'&&mp[s[i]-'A'][s[i-1]-'A']!=-1)
            {
                s[i-1]=mp[s[i]-'A'][s[i-1]-'A'];
                s[i]='*';
            }
            else
            {
                for(j=0;j<i;j++)
                    if(s[j]!='*'&&mp1[s[i]-'A'][s[j]-'A']==0)
                    {
                        for(int k=0;k<=i;k++)
                            s[k]='*';
                    }
            }
        }
        printf("Case #%d: [",cas++);
        int flag=0;
        for(i=0;i<n;i++)
        {
            if(s[i]!='*')
            {
                if(flag==1)
                    printf(", ");
                printf("%c",s[i]);
                flag=1;
            }
        }
        printf("]\n");
    }
    //system("pause");
    return 0;
}
