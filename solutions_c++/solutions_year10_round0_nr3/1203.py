#include <stdio.h>
#include <queue>
using namespace std;
#define sz 1002

int grp[sz], worked[sz], how_many[sz];
queue <int> que, rol;

int main()
{
    int _kase,kase=0,r,k,n,i,j,l,a,d,sum,temp,t;
    freopen("C.in","r",stdin);
    freopen("C_out.txt","w",stdout);
    scanf("%d",&_kase);
    while(_kase--)
    {
        while(!que.empty()) que.pop();
        while(!rol.empty()) rol.pop();
        sum=0;

        scanf(" %d %d %d",&r,&k,&n);
        for(i=0;i<n;i++)
        {
            scanf(" %d",&a);
            grp[i]=a;
            worked[i]=-1;
            que.push(i);
        }

        for(d=0;d<r;d++)
        {
            i=que.front();
            if( worked[i]!=-1 )
            {
                j=worked[i];
                for(temp=0,l=j;l<d;l++)
                {
                    temp+=how_many[l];
                }

                if( true )
                {
                    r-=d;
                    sum+=(r/(d-j))*temp;
                    d=r%(d-j);
                    for(l=j;d>0;l++,d--)
                    {
                        sum+=how_many[l];
                    }
                }
                break;
            }
            else
            {
                for( temp=0; !que.empty(); )
                {
                    t=que.front();
                    if( temp+grp[t]<=k )
                    {
                        temp+=grp[t];
                        rol.push(t);
                        que.pop();
                    }
                    else break;
                }
                worked[i]=d;
                how_many[d]=temp;
                sum+=temp;
                //printf(" %d",temp);
                while( !rol.empty() )
                {
                    que.push(rol.front());
                    rol.pop();
                }
            }
        }
        printf("Case #%d: %d\n",++kase,sum);
    }
    return 0;
}
