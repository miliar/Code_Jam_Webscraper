#include <cstdio>
#include <algorithm>
#define LLD long long int

using namespace std;

int main()
{
	int lw;
	scanf("%d",&lw);

	for (int Lc=1;Lc<=lw;Lc++)
	{
		LLD a,n,m;
		scanf("%lld%lld%lld",&n,&m,&a);
	
		bool done = false;
		for (LLD i=0,j,k,l;i<=n;i++)
			for (j=0;j<=m;j++)
				for (k=0;k<=n;k++)
					for (l=0;l<=m;l++)
					{
						if ( (i*l-j*k == a)&&(i!=0 || j!=0)&&(k!=0 || l !=0) &&(i!=k || j!=l))
						{
							if (!done)
								printf("Case #%d: 0 0 %lld %lld %lld %lld\n",Lc,i,j,k,l);
							done = true;
						}
					}
		if (!done)
			printf("Case #%d: IMPOSSIBLE\n",Lc);
	}

	return 0;
}
