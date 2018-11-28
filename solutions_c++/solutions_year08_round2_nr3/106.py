#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int w[100];

int t[5005];

int main()
{
	int lz;
	scanf("%d", &lz);
	for(int nz=1; nz<=lz; nz++)
	{
		int k,n;
		scanf("%d", &k);
		scanf("%d", &n);
		for(int i=0; i<n; i++) scanf("%d", &w[i]);
		for(int i=1; i<=k; i++) t[i]=-1;
		
		int cur=0;
		int p=0;
		for(int i=1; i<=k; i++)
		{
			while(p<i)
			{				
				cur%=k;
				cur++;
				if(t[cur]==-1)
					p++;
				
			}
			t[cur]=i;
			p=0;
			//	cur++;
		}
				
		printf("Case #%d: ", nz);
		for(int i=0; i<n; i++)
			printf("%d ", t[w[i]]);
		printf("\n");
	}
	return 0;
}
