#include <cstdio>
#include <algorithm>

using namespace std;

int main(void)
{
	int t;
	scanf("%d", &t);
	for(int caseN=1;caseN<=t;caseN++)
	{
		int n, data[1000];
		scanf("%d", &n);
		int xored=0, sum=0;
		for(int i=0;i<n;i++) 
		{
			scanf("%d", data+i);
			xored^=data[i];
			sum+=data[i];
		}

		printf("Case #%d: ", caseN);
		if(xored) printf("NO\n");
		else
		{
			sort(data, data+n);
			printf("%d\n", sum-data[0]);
		}
	}

	return 0;
}
