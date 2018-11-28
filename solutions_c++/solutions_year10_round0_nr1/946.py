#include <iostream>
using namespace std;

int tot,n,k,t;

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&tot);
    for (int tc=1;tc<=tot;++tc)
    {
    	scanf("%d%d",&n,&k);
    	printf("Case #%d: ",tc);
    	if (k%(1<<n)==((1<<n)-1))
			printf("ON\n");
		else
			printf("OFF\n");
    }
    return 0;
}
