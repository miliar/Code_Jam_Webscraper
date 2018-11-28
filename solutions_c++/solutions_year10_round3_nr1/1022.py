#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;
#define ONLINE

struct Edge
{
	int p1, p2;
}Buf;

vector<Edge> E;


bool IsCrossed(int x1, int x2)
{
	if(E[x1].p1 == E[x2].p1) return false;

	if(E[x2].p1 < E[x1].p1)
	{
		if(E[x2].p2 > E[x1].p2) return true;
		else return false;
	}
	else if(E[x2].p1 > E[x1].p1)
	{
		if(E[x2].p2 < E[x1].p2) return true;
		else return false;
	}
}
int main()
{
#ifdef ONLINE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif


	int iCaseTimes, i, j;

	scanf("%d", &iCaseTimes);
	for(int kk = 1; kk <= iCaseTimes; kk++)
	{
		E.clear();
		int iEdgeNum;
		scanf("%d", &iEdgeNum);
		for(int i = 0; i < iEdgeNum; i++)
		{
			scanf("%d%d", &Buf.p1, &Buf.p2);
			E.push_back(Buf);
		}

		int iRet(0);
		for(int i = 0; i < E.size(); i++)
		{
			for(int j = 0; j < E.size(); j++)
			{
				if(IsCrossed(i, j))
					iRet++;
			}
		}

		printf("Case #%d: %d\n", kk, iRet / 2);
	}
	return 0;
}

