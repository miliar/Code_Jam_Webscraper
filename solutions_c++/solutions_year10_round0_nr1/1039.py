#include <stdio.h>
#include <string.h>

int m;


int main()
{
	//freopen("A.in","r",stdin);
	//freopen("A.out","w",stdout);
	int i,j,k,cases,c=1,p;
	scanf("%d",&cases);
	while(cases--)
	{
        scanf("%d%d",&m,&k);
        int t=1<<m;
        if(k%t==t-1)
        printf("Case #%d: ON\n",c++);
        else
        printf("Case #%d: OFF\n",c++);
    }
	return 0;
}
