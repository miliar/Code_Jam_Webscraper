#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

#define ONLINE

long long F[40];

int main()
{

#ifdef ONLINE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	
	F[1] = 1;
	for(int i = 2; i <= 30; i++)
	{
		F[i] = 0;
		for(int j = 1; j < i; j++)
			F[i] += F[j];
		F[i]++;
	}

	int iCaseTimes;
	scanf("%d", &iCaseTimes);

	for(int k = 0; k < iCaseTimes; k++)
	{
		int SnapperNum, SnapNum, Cycle;
		scanf("%d%d", &SnapperNum, &SnapNum);
		
		Cycle = 0;
		for(int i = 1; i <= SnapperNum; i++) Cycle += F[i];
		Cycle++; // all turn off, returning to the original state

		SnapNum %= Cycle;

		printf("Case #%d: ", k + 1);
		if(SnapNum == Cycle - 1) printf("ON\n");
		else printf("OFF\n");
	}

	return 0;
}