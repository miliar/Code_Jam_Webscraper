#include<stdio.h>
#include<stdlib.h>
#include<math.h>
char form[40][5],oppo[40][5],input[150];
char stack[150];
int n,f,o;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,top,cas;
    scanf("%d",&t);
    for(cas=1;cas<=t;cas++)
    {
        scanf("%d",&f);
        for(int i=1;i<=f;i++)
        {
            scanf("%s",form[i]);
        }
        scanf("%d",&o);
        for(int i=1;i<=o;i++)
        {
            scanf("%s",oppo[i]);
        }
        scanf("%d",&n);
        scanf("%s",input);
        top=0;
        for(int i=0;i<n;i++)
        {
            stack[top++]=input[i];
            int mark=1;
            while(mark)
            {
                mark=0;
                for(int i=1;i<=f;i++)
                {
                    for(int pos=0;pos<=1;pos++)
                    {
                        if(stack[top-1]==form[i][pos])
                        {
                            if(top>=2&&stack[top-2]==form[i][pos^1])
                            {
                                stack[top-2]=form[i][2];
                                top--;
                                mark=1;
                                break;
                            }
                        }
                    }
                    if(mark)    break;
                }
            }
            if(top>=2)
            for(int i=1;i<=o;i++)
            {
                for(int pos=0;pos<=1;pos++)
                {
                    if(stack[top-1]==oppo[i][pos])
                    {
                        for(int j=0;j<top-1;j++)
                        {
                            if(stack[j]==oppo[i][pos^1])
                            {
                                top=0;
                                break;
                            }
                        }
                    }
                    if(top==0)  break;
                }
                if(top==0)  break;
            }
        }
        printf("Case #%d: ",cas);
        printf("[");
        if(top>=1)  printf("%c",stack[0]);
        for(int i=1;i<top;i++)
        {
            printf(", %c",stack[i]);
        }
        printf("]\n");
    }
}
