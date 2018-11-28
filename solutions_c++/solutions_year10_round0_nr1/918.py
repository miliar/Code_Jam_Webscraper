#include <cstdio>

int pow[31];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	int test,testnum,i,k,n;

	pow[0] = 1;
	for (i = 1; i < 31; ++ i)
		pow[i] = pow[i-1] * 2;

	scanf("%ld",&testnum);
	for (test = 1; test <= testnum; ++ test){
		scanf("%ld %ld",&n,&k);
		if ((k + 1) % pow[n] == 0)
			printf("Case #%ld: ON\n",test);
		else
			printf("Case #%ld: OFF\n",test);
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}
