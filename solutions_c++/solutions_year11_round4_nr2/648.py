#include <cstdio>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <queue>
#include <stack>
#include <sstream>

using namespace std;

#define EPS 1e-10
#define EQ(a,b) (abs((a)-(b))<EPS)

int r, c, d;
char field[10][11];

int main(void)
{
	int T;
	scanf("%d", &T);

	for(int caseN=1;caseN<=T;caseN++)
	{
		scanf("%d %d %d", &r, &c, &d);
		for(int i=0;i<r;i++) scanf("%s", field[i]);

		int K=min(r, c);
		while(K>=3)
		{
			bool isAns=false;
			for(int i=0;i<r-K+1;i++)
			{
				for(int j=0;j<c-K+1;j++)
				{
					double xSum=0, ySum=0;
					for(int q=0;q<K;q++)
					{
						for(int w=0;w<K;w++)
						{
							if(q==0 && w==0) continue;
							if(q==0 && w==K-1) continue;
							if(q==K-1 && w==0) continue;
							if(q==K-1 && w==K-1) continue;

							double tar=field[i+q][j+w]-'0';
							xSum+=tar*(q-K/2.0+0.5);
							ySum+=tar*(w-K/2.0+0.5);
						}
					}

					if(EQ(xSum, 0) && EQ(ySum, 0)) goto findAns;
				}
			}
			K--;
		}

findAns:
		printf("Case #%d: ", caseN);
		if(K>=3) printf("%d\n", K);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
