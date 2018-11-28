#include <stdio.h>
#include <string.h>
#include <iostream>
#include <queue>
using namespace std;

int xx[1100];

queue< int > q,e,em;

int main()
{
	//freopen("B.in","r",stdin);
	//freopen("B.out","w",stdout);
	int i,j,cases,r,k,n,sum,t;
	scanf("%d",&cases);
	for(j=1;j<=cases;j++)
	{
	    q=em;
	    sum=0;
	    scanf("%d%d%d",&r,&k,&n);
	    for(i=0;i<n;i++)
	    {
            scanf("%d",&xx[i]);
            q.push(xx[i]);
	    }
        while(r--)
        {
            t=0;
            for(i=0;i<n;i++)
            {
                if(t+xx[i]<=k)
                {
                    t+=xx[i];
                    q.pop();
                    q.push(xx[i]);
                }
                else
                break;
            }
            e=q;
            for(i=0;i<n;i++)
            {
                xx[i]=e.front();
                e.pop();
            }
            sum+=t;
        }
        printf("Case #%d: %d\n",j,sum);
    }
	return 0;
}
