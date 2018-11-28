#include"iostream"
#include<stdio.h>
#include<memory.h>
using namespace std;
char ch[30][30];
int op[30][30];
char s[150];
char ans[150];
int main()
{
    int T,i,j,k,cas=1,n,len;
   freopen("B-large.in","r",stdin);
  freopen("B-large.out","w",stdout);
    scanf("%d",&T);
    while(T--)
    {

        memset(ch,'\0',sizeof(ch));
        memset(op,0,sizeof(op));
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%s",s);
            ch[s[0]-'A'][s[1]-'A']=s[2];
            ch[s[1]-'A'][s[0]-'A']=s[2];
        }
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%s",s);
            op[s[0]-'A'][s[1]-'A']=1;
            op[s[1]-'A'][s[0]-'A']=1;
        }
        scanf("%d%s",&len,s);
        for(i=1;i<len;i++)
        {
            k=-1;
            for(j=i-1;j>=0;j--)
                if(s[j]!='\0')
                {
                    k=j;
                    break;
                }
            if(k!=-1)
            {
                if(ch[s[k]-'A'][s[i]-'A']!='\0')
                {

                     s[i]=ch[s[k]-'A'][s[i]-'A'];
					 s[k]='\0';
                }
            }
            for(j=0;j<i;j++)
            {
                if(s[j]!='\0')
                {
                    if(op[s[i]-'A'][s[j]-'A'])
                    {
                        for(k=0;k<=i;k++)
                            s[k]='\0';
                        break;
                    }
                }
            }
        }
        int cnt=0;
        for(i=0;i<len;i++)
            if(s[i]!='\0')
                ans[cnt++]=s[i];
        printf("Case #%d: [",cas++);
        if(cnt>0)
            printf("%c",ans[0]);
        for(i=1;i<cnt;i++)
            printf(", %c",ans[i]);
        printf("]\n");
    }
    return 0;
}
