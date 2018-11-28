#include<stdio.h>
#include<cstring>
#include<vector>
using namespace std;
char inv[1000][1000];
int op[1000][1000];
int main()
{
    int t,i,j;
    //freopen("GBS.in","r",stdin);
    freopen("GBL.out","w",stdout);
    scanf("%d",&t);getchar();
    for(int cn=1;cn<=t;cn++)
    {
        int c,d,n;
        memset(inv,0,sizeof(inv));
        memset(op,0,sizeof(op));
        scanf("%d",&c);getchar();
        while(c--)
        {
            char a,b,to;
            scanf("%c%c%c",&a,&b,&to);getchar();
            inv[a][b]=inv[b][a]=to;
        }
        scanf("%d",&d);getchar();
        while(d--)
        {
            char a,b;
            scanf("%c%c",&a,&b);getchar();
            op[a][b]=op[b][a]=1;
        }
        scanf("%d",&n);getchar();
        char li[1000];
        scanf("%s",li);
        //printf("%s\n",li);
        vector<char> ele;
        ele.clear();
        for(int l=0;l<n;l++)
        {
            ele.push_back(li[l]);
            int len=ele.size();
            //printf("%d\n",len);
            if(len>=2&&inv[ele[len-1]][ele[len-2]])
            {
                ele.pop_back();
                ele[len-2]=inv[ele[len-1]][ele[len-2]];
            }
            len=ele.size();
            for(i=0;i<len;i++)
            {
                for(j=i+1;j<len;j++)
                {
                    if(op[ele[i]][ele[j]])
                    {
                        i=len;
                        ele.clear();
                    }
                }
            }
        }
        printf("Case #%d: [",cn);
        for(i=0;i<ele.size();i++)
        {
            printf("%c",ele[i]);
            if(i!=ele.size()-1)printf(", ");
        }
        printf("]\n");
    }
    return 0;
}
