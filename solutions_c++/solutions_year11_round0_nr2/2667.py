#include<iostream>
using namespace std;
int base[26][26];
bool oppo[26][26];
int get(char c)
{
    return c-'A';
}
char to(int c)
{
    return c+'A';
}
char str[110];
int list[110];
int main()
{
    int cases;
    scanf("%d",&cases);
    for(int ca=1;ca<=cases;ca++)
    {
        int c,d,n;
        memset(base,-1,sizeof(base));
        memset(oppo,0,sizeof(oppo));
        scanf("%d",&c);
        for(int i=0;i<c;i++)
        {
            scanf("%s",str);
            base[get(str[0])][get(str[1])]=get(str[2]);
            base[get(str[1])][get(str[0])]=get(str[2]);
        }
        scanf("%d",&d);
        for(int i=0;i<d;i++)
        {
            scanf("%s",str);
            oppo[get(str[0])][get(str[1])]=true;
            oppo[get(str[1])][get(str[0])]=true;
        }
        scanf("%d",&n);
        scanf("%s",str);
        int now=0;
        for(int i=0;i<n;i++)
        {
            if(now==0)
            {
                list[now++]=get(str[i]);
            }
            else
            {
                if(base[list[now-1]][get(str[i])]!=-1)
                {
                    list[now-1]=base[list[now-1]][get(str[i])];
                }
                else
                {
                    bool judge=false;
                    for(int j=0;j<now;j++)
                    {
                        if(oppo[list[j]][get(str[i])])
                        {
                        //    system("pause");
                            judge=true;
                            break;
                        }
                    }
                    if(judge)
                    {
                        now=0;
                    }
                    else
                    list[now++]=get(str[i]);
                }
            }
        }
        printf("Case #%d: [",ca);
        if(now==0)
            puts("]");
        else
        {
            printf("%c",to(list[0]));
            for(int i=1;i<now;i++)
            {
                printf(", %c",to(list[i]));
            }
            puts("]");
        }
    }
}
