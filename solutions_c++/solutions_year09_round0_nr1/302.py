#include <iostream>
#include <cstdlib>
using namespace std;
char dic[5000][20];
char s[1000];
bool tmp[20][26],flag;
int L,D,N,Cn,i,j,k,tot;
int main()
{
    freopen("A-large.in.txt","r",stdin);
    freopen("A-large.out.txt","w",stdout);
    scanf("%d%d%d",&L,&D,&N);
    for (i=0;i<D;i++)
        scanf("%s",dic[i]);
    for (Cn=1;Cn<=N;Cn++)
    {
        scanf("%s",s);
        tot=0;
        memset(tmp,false,sizeof(tmp));
        j=0;
        flag=true;
        for (i=0;i<strlen(s);i++)
        {
            if (s[i]=='(')
                  flag=false;        
            else if (s[i]==')')
            {
                 flag=true;
                 j++;
            }
            else
            {
                tmp[j][s[i]-'a']=true;
                if (flag)
                   j++;
            }
        }
        for (i=0;i<D;i++)
        {
            flag=true;
            for (j=0;j<L;j++)
                if (!tmp[j][dic[i][j]-'a'])
                {
                    flag=false;
                    break;
                }
            if (flag)
               tot++;
        }
        printf("Case #%d: %d\n",Cn,tot);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
