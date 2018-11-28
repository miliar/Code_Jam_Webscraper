#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

#define ONLINEJUDGE
#define MAXN 11000

int P, Q;
vector<int> v;
int Cell[MAXN];
int main()
{
#ifdef ONLINEJUDGE
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
#endif

	int iCaseTimes, i, j;
	int iBuf;
	int iMax, iRet, iMin;

	scanf("%d", &iCaseTimes);
	for(int k = 0; k < iCaseTimes; k++)
	{
		printf("Case #%d: ", k + 1);
		scanf("%d%d", &P, &Q);
		v.clear();
		for(i = 0; i < Q; i++)
		{
			scanf("%d", &iBuf);
			v.push_back(iBuf);
		}

		iMin = -1;
		do
		{
			memset(Cell, 0, sizeof(Cell));
			for(i = 1; i <= P; i++)
			{
				Cell[i] = 1;
			}

			iRet = 0;
			for(j = 0; j < v.size(); j++)
			{
				Cell[v[j]] = 0;
				for(i = v[j] - 1; i >= 1; i--)
				{
					if(Cell[i] == 0) break;
					iRet++;
				}
				for(i = v[j] + 1; i <= P; i++)
				{
					if(Cell[i] == 0) break;
					iRet++;
				}
			}
			if(iMin == -1 || (iMin != -1 && iRet < iMin)) iMin = iRet;
		}while(next_permutation(v.begin(), v.end()));

		printf("%d\n", iMin);
	}
		
	return 0;
}