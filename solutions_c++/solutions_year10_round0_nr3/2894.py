#include <stdio.h>

int main()
{
	FILE *in = fopen("C-small-attempt0.in", "r");
	if(in==NULL)
	{
		perror("napaka");
		getchar();
		return 0;
	}
	FILE *out = fopen("C-small.out", "w");
	int T, R, k, N, i, casenum=1;
	fscanf(in, "%d", &T);
	for(i=0; i<T; i++) //num of test cases
	{
		printf("Case: %d\n", i+1);
		fscanf(in, "%d %d %d", &R, &k, &N);
		//printf("R:%d k:%d N:%d\n", R, k, N);
		int grupa[N], j, index=0, previndex=0;
		for(j=0; j<N; j++) //get groups
			fscanf(in, "%d", &grupa[j]);
		//getchar();
		unsigned long int zasluzek=0;
		for(j=0; j<R; j++) //num of rides per day
		{
			//printf("Ride: %d\n", j);
			long int sum=0;
			while(1)
			{
				zasluzek += grupa[index];
				//printf("zasluzek: %d\n", zasluzek);
				//getchar();
				sum += grupa[index++];
				if(index >= N) index=0;
				if(sum + grupa[index] > k || previndex==index) break;
			}
			previndex=index;
		}
		fprintf(out, "Case #%d: %ld\n", casenum++, zasluzek);
	}
	fclose(in);
	fclose(out);
	printf("Finished!");
	getchar();
	return 0;
}
