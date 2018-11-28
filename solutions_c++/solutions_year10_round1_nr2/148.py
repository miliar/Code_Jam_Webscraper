#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

int dynamic[101][256];
int D, I, M, data[100], n;

int getDynamic(int nth, int last);

int main(void)
{
	int t;
	scanf("%d", &t);
	for(int caseN=1;caseN<=t;caseN++)
	{
		scanf("%d %d %d %d", &D, &I, &M, &n);
		for(int i=0;i<n;i++) scanf("%d", data+i);

		memset(dynamic, -1, sizeof(dynamic));
		int ans=getDynamic(0, 0);
		for(int i=1;i<=255;i++) ans=min(ans, getDynamic(0, i));
		printf("Case #%d: %d\n", caseN, ans);
	}

	return 0;
}

int getDynamic(int nth, int last)
{
	int &ret=dynamic[nth][last];
	if(ret!=-1) return ret;

	ret=0;
	if(nth<n)
	{
		ret=getDynamic(nth+1, last)+D;
		for(int i=0;i<=255;i++)
		{
			int base=abs(i-data[nth]);
			int gap=abs(last-i);
			gap--;
			if(gap<0) gap=0;
			if(M==0)
			{
				if(last!=i) continue;
				ret=min(ret, base+getDynamic(nth+1, i));
			}
			else ret=min(ret, base+getDynamic(nth+1, i)+gap/M*I);
		}
	}

	return ret;
}
