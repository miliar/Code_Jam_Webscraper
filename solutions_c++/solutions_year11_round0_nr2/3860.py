#include<stdio.h>

bool canCombine();
bool canClear();


int c,d,n;
int top;
char stack[200];
char combine[4];
char opposite[3];
char in[200];

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("out0.out", "w", stdout);

    int t,ca=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&c);
        if (c) scanf(" %s", combine);
        scanf("%d",&d);
        if (d) scanf(" %s", opposite);
        scanf("%d",&n);
        scanf(" %s", in);

        top=0;
        for (int i=0;i<n;i++)
        {
            stack[top++]=in[i];
            if (canCombine())
            {
                top-=2;
                stack[top++]=combine[2];
                continue;
            }
            if (canClear())
                top=0;
        }

        printf("Case #%d: [", ca++);
        for (int i=0;i<top;i++)
        {
            if (i) printf(", ");
            printf("%c", stack[i]);
        }
        printf("]\n");
    }
    return 0;
}

bool canCombine()
{
    if (c==0) return false;
    if (top<2) return false;
    if ((stack[top-2]==combine[0]&&stack[top-1]==combine[1])||(stack[top-2]==combine[1]&&stack[top-1]==combine[0]))
        return true;
    return false;
}

bool canClear()
{
    if (d==0) return false;
    if (top<2) return false;
    if (stack[top-1]==opposite[0])
    {
        for (int i=0;i<=top-2;i++)
            if (stack[i]==opposite[1]) return true;
    }
    if (stack[top-1]==opposite[1])
    {
        for (int i=0;i<=top-2;i++)
            if (stack[i]==opposite[0]) return true;
    }
    return false;
}
