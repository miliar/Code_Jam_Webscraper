#include <stdio.h>
#include <math.h>

int main()
{
	int T;
	scanf("%d", &T);
	
	char *msg[2] = {
		"OFF",
		"ON"
	};
	
	int imsg = 0;
	
	for (int i = 0; i < T; i++)
	{
		int N, K;
		scanf("%d %d", &N, &K);
		
		int first = pow(2, N-1);
		
		if (K < first) imsg = 0;
		else
		{
			if (((K / first) % 2) != 0 && ((K + 1) % first) == 0) imsg = 1;
			else imsg = 0;
		}
		
		printf("Case #%d: %s\n", i+1, msg[imsg]);
	}
	

	return 0;
}
