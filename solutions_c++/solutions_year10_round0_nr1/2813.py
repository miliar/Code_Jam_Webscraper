#include<iostream>
using namespace std;

int main()

{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    int n,k,t;
	int mask,flag;
	cin>>t;
	for(int tcase=1;tcase<=t;tcase++)
	{
		mask=0;
		flag=0;
		cin>>n>>k;
		mask = ~(~0<<n);
		if((k&mask) == mask)
		{
			flag=1;
		}
		else
			flag=0;

		printf("Case #%d: %s\n",tcase,flag?"ON":"OFF");
	}

return 0;
}