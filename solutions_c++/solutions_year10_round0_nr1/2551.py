#include <cstdio>
#include <fstream>
#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;

int main()
{
	FILE *in = fopen("F:\\A-large.in", "r");
	FILE *out = fopen("F:\\result.txt", "w");
	int T;
	fscanf(in, "%d", &T);

	for(int l = 0; l < T; l++)
	{
		int N, K;
		fscanf(in, "%d %d", &N, &K);

		int times = 1 << N;

		if(K % times == times - 1)
			fprintf(out, "Case #%d: ON\n", l+1);
		else
			fprintf(out, "Case #%d: OFF\n", l+1);

	}
}