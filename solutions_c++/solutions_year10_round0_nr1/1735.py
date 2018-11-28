#include<iostream>
#include<string>
using namespace std;
FILE* fin = fopen("A-large.in", "r");
FILE* fout = fopen("large_A.out", "w");
int main()
{
	int n, k, T, t, i;
	int num[31] = {0, 1, 2};
	for(i = 3; i < 31; i++)
		num[i] = num[i - 1] + i - 1;
	fscanf(fin, "%d", &T);
	//scanf("%d", &T);
	for(t = 1; t <= T; t++){
		fscanf(fin, "%d%d", &n, &k);
		int tmp = 1 << n;
		//scanf("%d%d", &n, &k);
		if(k % tmp != tmp - 1)
			fprintf(fout, "Case #%d: OFF\n", t);
			//printf("Case #%d: OFF\n", t);
		else fprintf(fout, "Case #%d: ON\n", t);
			//printf("Case #%d: ON\n", t);
	}
	return 0;
}