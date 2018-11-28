#include <iostream>
using namespace std;

int t,i,n,k,x,j;
bool ok;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	
	scanf("%d",&t);
	for (x=1; x<=t; x++)
	{
		scanf("%d%d",&n,&k);
		j=0;
		while (1)
		{
			j++;
			if (j==n)
			{
				if (k%2==1) ok=true; else ok=false;
				break;
			}
			if (k%2==0) {ok=false; break;}
			k/=2;
		}
		printf("Case #%d: ",x);
		if (ok) printf("ON\n"); else printf("OFF\n");
	}
	
//	system("pause");
	return 0;
}
