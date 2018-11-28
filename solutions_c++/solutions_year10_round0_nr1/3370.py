#include <cstdio>
using namespace std;

int main()
{
	freopen("sn(in).txt","r",stdin);
	freopen("sn(out).txt","w",stdout);
	int t,n;
	unsigned long long k;
	scanf("%d",&t);
	for(int g=1; g<=t; g++)
	{
		scanf("%d%llu",&n,&k);
		bool f = true; 
		for(int j=0; j<n; j++)
		{
			if (!(k & (1 << j))) 
			{
				f = false;
				break;
			} 
		}
		if(f) printf("Case #%d: ON\n",g);
		else printf("Case #%d: OFF\n",g);
	}
	return 0;
}