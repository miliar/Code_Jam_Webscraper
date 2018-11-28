#include <cstdio>
#include <algorithm>

using namespace std;

int main(void)
{
	int t;
	scanf("%d", &t);
	for(int caseN=1;caseN<=t;caseN++)
	{
		int a1, a2, b1, b2;
		scanf("%d %d %d %d", &a1, &a2, &b1, &b2);

		int ans=0;
		for(int i=a1;i<=a2;i++) for(int j=b1;j<=b2;j++) 
		{
			int maxV=max(i, j);
			int minV=min(i, j);
			if(i==j) continue;

			int turn=0;
			while(1)
			{
				if(maxV>=minV*2)
				{
					if(turn%2==0) ans++;
					break;
				}
				else
				{
					maxV-=minV;
					swap(maxV, minV);
				}

				if(minV==0)
				{
					if(turn%2) 
					{
						ans++;
					}
				}
				turn++;
			}
		}
		printf("Case #%d: %d\n", caseN, ans);
	}

	return 0;
}
