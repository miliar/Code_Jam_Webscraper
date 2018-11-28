#include<cstdio>
#include<cstring>

using namespace std;

char s[30][30];
bool opp[30][30];
int n;
char str[110];
int stk[110],top;
int main()
{
    freopen("B.out","w",stdout);
    int cs;
    scanf("%d",&cs);
    for(int t=1;t<=cs;t++)
    {
        memset(s,0,sizeof(s));
        memset(opp,0,sizeof(opp));
        int k;
        scanf("%d",&k);
        for(int i=0;i<k;i++){
            scanf("%s",str);
            s[str[0]-'A'][str[1]-'A']=str[2];
            s[str[1]-'A'][str[0]-'A']=str[2];
        }
        scanf("%d",&k);
        for(int i=0;i<k;i++){
            scanf("%s",str);
            opp[str[0]-'A'][str[1]-'A']=opp[str[1]-'A'][str[0]-'A']=true;
        }
        scanf("%d%s",&n,str);
        top=0;
        for(int i=0;i<n;i++)
        {
                    stk[top++]=str[i]-'A';
                    while(top>1 && s[stk[top-2]][stk[top-1]]) {
                        stk[top-2]=s[stk[top-2]][stk[top-1]]-'A';
                        top--;
                    }        
            for(int j=0;j<top;j++)
                for(int k=j+1;k<top;k++)
                if (opp[stk[j]][stk[k]])    top=0;                
        }
        printf("Case #%d: [",t);
        for(int i=0;i<top;i++)
            if(i==0) printf("%c",stk[i]+'A');
            else printf(", %c",stk[i]+'A');
        printf("]\n");
    }
    return 0;
}
