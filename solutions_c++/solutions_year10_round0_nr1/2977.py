#include <stdio.h>

int pow(int n, int power)
{
	if(!power) return 1;
	int result = 1, i;
	for(i=0; i<power; i++)
		result *= n;
	return result;
}

int main()
{
	FILE *f = fopen("A-large.in", "r"), *o = fopen("A-large.out", "w");
	if(f==NULL)
	{
		perror("napaka");
		getchar();
		fclose(o);
		return 0;
	}
	int T, N, K, casenum=1;
	fscanf(f, "%d", &T);
	while(fscanf(f, "%d %d", &N, &K)==2)
	{
		int limit = pow(2, N);
		printf("Limit is: %d\n", limit);
		//getchar();
		int counter = 0;
		int i;
		for(i=0; i<K; i++)
		{
			counter++;
			if(counter >= limit) counter = 0;
		}
		fprintf(o, "Case #%d: %s\n", casenum++, (counter==limit-1)?"ON":"OFF");
	}
	fclose(f);
	fclose(o);
	getchar();
	return 0;
}
