#include<cstdlib>
#include<stdio.h>
#include<vector>

using namespace std;


int main()
{
	int t;
	scanf("%d",&t);
	//printf("t=%d\n",t);
	for(int i=0;i<t;++i)
	{
		int n;
		scanf("%d",&n);
		//printf("n=%d\n",n);
		vector<int> tab(n);
		vector<int> uzyte(n,0);
		for(int j=0;j<n;++j)
		{
			scanf("%d",&tab[j]);
			tab[j]--;
		}
		int suma=0;
		for(int j=0;j<n;++j)
			if((j!=tab[j])&&(uzyte[j]==0))
			{
				int tmp=j;
				while(uzyte[tmp]==0)
				{
					uzyte[tmp]=1;
					suma++;
					tmp=tab[tmp];
				}
			}
		printf("Case #%d: %d.000000\n",i+1,suma);
	}
}
