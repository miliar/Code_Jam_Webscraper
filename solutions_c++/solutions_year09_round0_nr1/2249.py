#include <cstdio>
#include <string>
using namespace std;


char wrd[5005][20];
char au[40][40];
char reg[450];
int flag,c;
int l,d,n,i,j,k;

int main()
{
    scanf("%d%d%d\n",&l,&d,&n);
    for(i=0;i<d;i++)
    {
        gets(wrd[i]);
//        printf("%s\n",wrd[i]);
    }
        
    for(k=0;k<n;k++)
    {
        gets(reg);
//        printf("reg = %s\n",reg);
        flag = 0;
        c = 0;
        memset(au,0,sizeof(au));
        for(i=0;i<strlen(reg);i++)
        {
            if(reg[i] == '(')
            {
                 flag = 1;
                 continue;
            } 
            if(reg[i] == ')')
            {
                flag = 0;
                c++;
                continue;
            }
            au[c][reg[i]-'a'] = 1;
            if(!flag) c++;
        }

        c = 0;
        for(i=0;i<d;i++)
        {
            flag = 1;
            for(j=0;j<l&&flag;j++)
                if(au[j][wrd[i][j]-'a'] == 0) flag = 0;
            if(flag) c++;
        }
        printf("Case #%d: %d\n",k+1,c);
    }
    return 0;
}