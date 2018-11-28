#include <cstdlib>
#include <iostream>
#include <string>
#include <cstring>

using namespace std;
        
string dic[5010];
char g[20][1001];
int len[20];

bool findchar(int x, char y)
{
    int i;
    for(i=1;i<=len[x];i++)
       if(g[x][i] == y)
           return(true);
    return(false);
}

int main(int argc, char *argv[])
{
    int L,d,n;
   // freopen("E:/in.txt","r",stdin);
//freopen("E:/out.txt","w",stdout);

    while(scanf("%d%d%d",&L,&d,&n)==3)
    {
        int i,j,k,l;
        char word[5000];
        for(i=1;i<=d;i++)
        {
            scanf("%s",&word);
            dic[i] = word;
        }
        for(i=1;i<=n;i++)
        {
            scanf("%s",&word);
            memset(len,0,sizeof(len));
            l = strlen(word);
            k = -1;
            for(j = 0;j < l;)
            {
                if(word[j] == '(')
                {
                    k++; j++;
                    while(word[j] != ')')
                    {
                        g[k][++len[k]]  = word[j];
                        j++;
                    }
                    j++;
                }
                else
                {
                    k++;
                    g[k][++len[k]] = word[j];
                    j++;
                }
            }
            int ans = 0;
            for(j = 1;j <= d;j++)
            {
                bool flag = true;
                for(k=0;k<L;k++)
                {
                     if(!findchar(k,dic[j][k]))
                     {
                         flag = false;
                         break;
                     }
                }
                if(flag) ans++;
            }
            printf("Case #%d: %d\n",i,ans);
        }
    }
    return EXIT_SUCCESS;
}
