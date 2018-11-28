#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>

#define MAX 1000

using namespace std;

int main()
{
	int num_test_cases;
	scanf("%d ", &num_test_cases);

	for(int test=1;test<=num_test_cases;test++)
	{
		int p,k,l,f[MAX],tmp;
		scanf("%d %d %d", &p, &k, &l);

		for(int i=0;i<l;i++)
			scanf("%d",&f[i]);
		
		for(int i=0;i<l;i++)
			for(int j=0;j<i;j++)
				if(f[i]>f[j])
				{
					tmp=f[i];
					f[i]=f[j];
					f[j]=tmp;
				}
				
		int c=0, x=1, t=0, z=0;
		while(z<l)
		{
			t++;
			if(t==k+1)
			{
				t=1;
				x++;
			}
			
			c+=x*f[z];
			z++;
		}
		
		if(l>k*p)
			printf("Case #%d: impossible\n",test);
		else
			printf("Case #%d: %d\n",test,c);
	}

	return 0;
}
