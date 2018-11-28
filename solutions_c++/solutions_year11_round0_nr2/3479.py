#include<stdio.h>
#include<string.h>
char combine[50][3],opposite[50][2],str[150],stack[150],temp[150],q;
int flag[200],top,ttop,m,p;


int push_stack(char a)
{
    top++;
//    printf("%c ",a);
    stack[top]=a;
    return 0;
}


int pop()
{
    top--;
    return 0;
}
int call_op(char a, char b)
{
    int i;
    for(i=0;i<p;i++)
    {
        if((a==opposite[i][0]&&b==opposite[i][1])||(b==opposite[i][0]&&a==opposite[i][1]))
            return 1;
    }
    return 0;
}

int call(char a, char b)
{
    int i;
    for(i=0;i<m;i++)
    {
        if((a==combine[i][0]&&b==combine[i][1])||(b==combine[i][0]&&a==combine[i][1]))
            return i;
    }
    return m;
}


int main()
{
    freopen("B-large.in","r",stdin);
    freopen("s.out","w",stdout);
    int n,i,j,n1,c,d,y,z,q,k;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        top=0;
        memset(flag,0,sizeof(flag));
        scanf("%d",&m);
        for(j=0;j<m;j++)
            scanf("%s",combine[j]);

        scanf(" %d",&p);
        for(j=0;j<p;j++)
            scanf("%s",opposite[j]);

        scanf(" %d",&n1);
        scanf("%s",str);

//         for(j=0;j<m;j++)
//        {
//            flag[combine[j][0]]=1;
//            flag[combine[j][1]]=1;
//        }
//
//        for(j=0;j<p;j++)
//        {
//            flag[combine[j][0]+32]=2;
//            flag[combine[j][1]+32]=2;
//        }


        push_stack(str[0]);
        for(j=1;j<n1;j++)
        {
            d=0;
            y=call(stack[top],str[j]);
            if(y!=m)
            {
                pop();
                push_stack(combine[y][2]);
                continue;
            }
            for(k=1;k<=top;k++)
            {
                z=call_op(stack[k],str[j]);
                if(z==1)
                {
                    top=0;
                    d=1;
                    break;
                }
            }
            if(d==1) continue;
            push_stack(str[j]);
        }

        printf("Case #%d: [",i+1);
        for(j=1;j<=top;j++)
            if(j!=top)
                printf("%c, ",stack[j]);
            else printf("%c",stack[j]);
        printf("]\n");
    }
    return 0;
}









