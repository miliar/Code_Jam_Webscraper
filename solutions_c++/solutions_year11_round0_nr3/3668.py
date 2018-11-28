#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int T, N;
int candy[1000];
int setBit[32];

void ClearBit()
{
	for(int i = 0; i < 32; i++) setBit[i] = 0;
}

void SetBit(int in)
{
	for(int i = 0; i < 32; i++)
	{
		setBit[i] += in%2;
		in/=2;
	}
}

bool Alleven()
{
	for(int i = 0; i < 32; i++)
	{
		if(setBit[i] % 2 == 1) return false;
	}
	return true;
}

int main()
{
	int smallest;
	int allsum;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++)
	{
		ClearBit();
		scanf("%d", &N);
		smallest = 987654321;
		allsum = 0;
		for(int j = 0; j < N; j++)
		{
			scanf("%d", candy+j);
			SetBit(candy[j]);
			smallest = min(smallest, candy[j]);
			allsum += candy[j];
		}
		
		printf("Case #%d: ", i);
		if(Alleven() == false) puts("NO");
		else	  			   printf("%d\n", allsum - smallest);
	}

	return 0;
}
