#include <iostream>

using namespace std;

int main()
{
    int T,y,hasil,N,S,p,g[105];
    scanf("%d",&T);
    y=0;
    while(T--)
    {
        y++;
        hasil=0;
        scanf("%d%d%d",&N,&S,&p);
        for(int a=0;a<N;a++) 
        {
            scanf("%d",&g[a]);
            if(g[a]<p && p!=0 || (g[a]==p && p>2)) continue;
            //if(g[a]/3>=p || (g[a]/3+1>=p && g[a]%3!=0))
            if(g[a]>=3*p-2) 
            {
                //printf("AAA %d\n",g[a]);
                hasil++;
            }
            else
            {
                //if(g[a]/3+2>=p && S>0 && )
                if(g[a]>=3*p-4 && S>0)
                {
                    hasil++;
                    S--;
                }
            }
        }   
        printf("Case #%d: %d\n",y,hasil);
    }
    return 0;
}
