#include <stdio.h>
#include <map>

using namespace std;

map <int,bool> mymap;
int p[10],q,s;

int num_digit(int x)
{
    int r=0;

    while(x)
    {
        x/=10;
        r++;
    }

    return r;
}

int main()
{
    int i,j,k,T,t,a,b,r,c;

    freopen("C-large.in","r",stdin);
    freopen("c-out.txt","w",stdout);

    scanf("%d",&T);

    for(t=1;t<=T;t++)
    {
        scanf("%d %d",&a,&b);

        s=num_digit(a);

        for(r=0,i=a;i<=b;i++)
        {
            mymap.clear();
            for(k=i,j=s-1;j>=0;j--)
            {
                p[j]=k%10;
                k/=10;
            }

            for(j=1;j<s;j++)
            {
                if(p[j]<p[0]) continue;

                for(c=0,q=0,k=j;c<s;k=(k+1)%s,c++) q=q*10+p[k];

                if(q>=a && q<=b && q>i)
                {
                    if(mymap[q]==0)
                    {
                        r++;
                        mymap[q]=1;
                    }
                }
            }
        }

        printf("Case #%d: %d\n",t,r);
    }

    return 0;


    }
