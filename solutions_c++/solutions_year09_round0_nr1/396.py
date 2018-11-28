#include <stdio.h>
#include <string.h>
int j,ti,length,dictn,quern;
char dict[5000][15];
unsigned array[15];
inline bool istrue()
{
    for(ti=0;ti<length;ti++)
        if(!((array[ti]>>(dict[j][ti]-'a'))<<31))
            return false;
    return true;
}

int main()
{
    int i,p,c,l;
    bool isquote;
    char tstr[400];
    freopen("codejam.in","r",stdin);
    freopen("codejam.out","w",stdout);
    scanf("%d%d%d",&length,&dictn,&quern);
    for(i=0;i<dictn;i++)
        scanf("%s",&dict[i]);
    for(i=0;i<quern;i++)
    {
        scanf("%s",tstr);
        l=strlen(tstr);
        p=0;
        isquote=false;
        memset(array,0,15*sizeof(int));
        for(j=0;j<l;j++)
        {
            if(tstr[j]>='a' && tstr[j]<='z')
            {
                array[p]+=1<<(tstr[j]-'a');
                if(!isquote)
                    p++;
            }
            else if(tstr[j]==')')
            {
                p++;
                isquote=false;
            }
            else if(tstr[j]=='(')
                isquote=true;
        }
        c=0;
        for(j=0;j<dictn;j++)
            if(istrue())
            {
//                printf("%s\n",dict[j]);
                c++;
            }
        printf("Case #%d: %d\n",i+1,c);
    }
}
