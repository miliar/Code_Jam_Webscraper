#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
char cmd[120];
char com[300][300];
bool op[300][300];
char stk[200];
int has[200];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,cas=1;
    scanf("%d",&t);
    while(t--)
    {
        memset(com,0,sizeof(com));
        memset(op,0,sizeof(op));
        memset(has,0,sizeof(has));
        int C,R;
        scanf("%d",&C);
        int tail = 0;
        for(int i=0; i<C; i++)
        {
            scanf("%s",cmd);
            com[cmd[0]][cmd[1]] = cmd[2];
            com[cmd[1]][cmd[0]] = cmd[2];
        }
        scanf("%d",&R);
        for(int i=0; i<R; i++)
        {
            scanf("%s",cmd);
            op[cmd[0]][cmd[1]] = true;
            op[cmd[1]][cmd[0]] = true;
        }
        int len;
        scanf("%d %s",&len,cmd);
        char ch;
        for(int i=0; i<len; i++)
        {
next:
            if(i>=len)
                break;
            stk[tail++] = cmd[i];
            has[cmd[i]]++;
            while(tail>=2)
            {
                while(com[stk[tail-1]][stk[tail-2]])
                {
                    ch  = com[stk[tail-1]][stk[tail-2]];
                    has[stk[tail-1]] --;
                    has[stk[tail-2]] --;
                    tail--;
                    stk[tail-1] = ch;
                    has[ch] ++;
                    for(int k=0; k<tail; k++)
                    {
                        if(op[ch][stk[k]])
                        {
                            memset(has,0,sizeof(has));
                            tail = 0;
                            i++;
                            goto next;
                        }
                    }
                }
                ch = stk[tail-1];
                for(int k=0; k<tail; k++)
                {
                    if(op[ch][stk[k]])
                    {
                        memset(has,0,sizeof(has));
                        tail = 0;
                        i++;
                        goto next;
                    }
                }
                break;
            }
        }
        printf("Case #%d: ",cas++);
        if(tail>1)
        {
            printf("[%c,",stk[0]);
                for(int i=1;i<tail;i++)
            printf(" %c%c",stk[i],i==tail-1?']':',');
            printf("\n");
        }
        else if (tail == 1)
        {
            printf("[%c]\n",stk[0]);
        }
        else
        {
            printf("[]\n");
        }

    }
    return 0;
}
