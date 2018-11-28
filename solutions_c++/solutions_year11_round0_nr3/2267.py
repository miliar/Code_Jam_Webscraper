
#include <stdio.h>

int main(int argc, char* argv[])
{

	freopen("c:\\input.in","r",stdin);
	freopen("C:\\output.txt","w",stdout);

	int T = 0;

	scanf("%d", &T);

	for(int t = 0 ; t < T ; t++)
	{
		int N;
		scanf("%d", &N);

		long long sum = 0;
		
		unsigned int minValue = 0xffffffff;
		int xorRet = 0;

		for(int n = 0 ; n < N ; n++)
		{
			int value;
			scanf("%d", &value);

			sum += value;

			minValue = (value < minValue) ? value : minValue;

			xorRet ^= value;
		}


		if(xorRet)
		{
			printf("Case #%d: NO\n", t+1);
		}
		else
		{
			printf("Case #%d: %I64d\n", t+1, sum-minValue);
		}

//		
	}

	return 0;
}