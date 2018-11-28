#include <stdio.h>
#include <math.h>

int main()
{
        int nT;

        scanf("%d", &nT);

	int N;
	int K;

        for (int i = 0; i < nT; i++)
        {
                scanf("%d%d", &N, &K);

		int tpN = (int) pow(2, N); 

		K = K % tpN;

		if(K == tpN -1)
			printf("Case #%d: ON\n", i+1);
		else
			printf("Case #%d: OFF\n", i+1);

        }
}
