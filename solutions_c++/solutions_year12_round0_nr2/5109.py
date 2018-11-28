#include<cstdio>
#include<iostream>

using namespace std;

int main()
{
    int T,N,S,P,i,j,k,l,max,in;

    freopen ("B-small-attempt2.in","r",stdin);
    freopen ("BBO.txt","w",stdout);


    scanf("%d",&T);

    for(i=1; i<=T; i++)
    {
        max=0;
        S=0;
        scanf("%d%d%d",&N,&S,&P);

        for(j=0; j<N; j++)
        {
            scanf("%d",&in);

            if(P == 0)
            {
                max++;
                continue;
            }

            else if(P>0 && in==0) continue;

            else if((((in-P)/2) +2 ) >P) max++;

            else if( (( (in-P)/2) +2 ) == P)
            {
                if(S==0) continue;

                S--;
                max++;
            }

        }

        printf("Case #%d: %d\n",i,max);

    }
    fclose(stdin);
    fclose(stdout);

    return 0;
}
