#include <stdio.h>

int main()
{
	int T, i, j, N, surprise, p, no, pom;
	scanf("%d", &T);
	for(i=0; i<T; i++)
	{
		no = 0;
		scanf("%d %d %d", &N, &surprise, &p);
		for(j=0; j<N; j++)
		{
			scanf("%d", &pom);
			if(pom >= 3*p-2) no++;
			else if(pom>=p && pom>=3*p-4 && pom<3*p-2 && surprise>0) { no++; surprise--;}
		}
		printf("Case #%d: %d\n", i+1, no);
	}
	return 0;
}