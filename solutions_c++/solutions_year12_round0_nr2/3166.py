#include<stdio.h>
int main()
{
    long T,tc,N,S,P,inp,I,J,C;
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%ld",&T);
    for(tc=1;tc<=T;tc++)
    {
        scanf("%ld %ld %ld",&N,&S,&P);
        C = 0;
        for(;N>0;N--)
        {
            scanf("%ld",&inp);
            switch(inp%3)
            {
                case 0: if(inp/3 >= P)
                            C++;
                        else if(inp/3+1 >= P && S > 0 && inp != 0)
                        {
                            S--;
                            C++;
                        }
                        break;
                case 1: if(inp/3+1 >= P)
                            C++;
                        break;
                case 2: if(inp/3+1 >= P)
                            C++;
                        else if(inp/3+2 >= P && S > 0)
                        {
                            S--;
                            C++;
                        }
                        break;
            }
        }
        printf("Case #%ld: %ld\n",tc,C);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
