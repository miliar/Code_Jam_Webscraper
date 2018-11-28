#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
using namespace std;

struct win
{
	int a,b;
}w[1003];


int main()
{

    int cas,ct=1;
    int i,j,k;
    int n;

    freopen("A-large.in","r",stdin);
    //freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);


    scanf("%d",&cas);
    while (cas--)
    {

        scanf("%d",&n);

		for (i=0; i<n; i++)
		{
			scanf("%d%d",&w[i].a,&w[i].b);
		}

		int res = 0;

		for (i=0; i<n; i++)
		{
			for (j=i+1; j<n; j++)
			{
				if ((w[i].a - w[j].a) * (w[i].b - w[j].b) < 0)
				{
					res++;
				}
			}
		}



        printf("Case #%d: ",ct++);
		printf("%d\n",res);      
        }

return 0;
}