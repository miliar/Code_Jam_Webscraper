#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

int max_pile(int* C, int k, int n, int tmp_s, int tmp_xor1, int tmp_xor2, int candy)
{
	if(!k)
	{
		for(; candy<n; candy++)
			tmp_xor2^=C[candy];
		if(tmp_xor1==tmp_xor2)
			return tmp_s;
		else
			return 0;
	}
	if(n-candy==k)
	{
		for(; candy<n; candy++)
		{
			tmp_s+=C[candy];
			tmp_xor1^=C[candy];
		}
		if(tmp_xor1==tmp_xor2)
			return tmp_s;
		else
			return 0;
	}
	return max(max_pile(C, k-1, n, tmp_s+C[candy], tmp_xor1^C[candy], tmp_xor2, candy+1), max_pile(C, k, n, tmp_s, tmp_xor1, tmp_xor2^C[candy], candy+1));
}

	
int main()
{
	FILE* i_f=fopen("input.txt", "r"), *o_f=fopen("output.txt", "w");
	if(!i_f || !o_f)
	{
		fprintf(stderr, "Opening file error\n");
		return 0;
	}
	int T, N, C[1000], ans;
	fscanf(i_f, "%d", &T);
	for(int t=0; t<T; t++)
	{
		fscanf(i_f, "%d", &N);
		for(int i=0; i<N; i++)
			fscanf(i_f, "%d", &(C[i]));
		ans=0;
		for(int k=1; k<N; k++)
			ans=max(ans, max_pile(&(C[0]), k, N, 0, 0, 0, 0));
		fprintf(o_f, "Case #%d: ", t+1);
		if(ans)
			fprintf(o_f, "%d\n", ans);
		else
			fprintf(o_f, "NO\n");
	}
	fclose(i_f);
	fclose(o_f);
	return 0;
}