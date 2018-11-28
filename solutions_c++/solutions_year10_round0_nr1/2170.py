#include <iostream>

int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
	int res[30];
	res[1]=2;
	for(int i=2;i<=30;i++)
	{
	    res[i]=res[i-1]*2;
    }
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        int n,k;
        scanf("%d %d",&n,&k);
        int tmp=k%res[n];
        printf("Case #%d: ",t);
        if(tmp==res[n]-1)
        printf("ON\n");
        else
        printf("OFF\n");
    }
	return 0;
}
