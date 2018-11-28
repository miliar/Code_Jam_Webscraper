#include <iostream>
#include <math.h>

using namespace std;

int C, N, K, B, T;

struct chick {
	int X;
	int V;
};

chick * ch;

void main(int argc, char **argv)
{
	FILE *input;
	FILE *output;

	input = fopen(argv[1], "r");

	fscanf(input, "%u", &C);

	for(int i=1; i<=C; i++)
	{
		fscanf(input, "%u %u %u %u", &N, &K, &B, &T);

		int CH = 0;
		int swaps = 0;

		ch = new chick[N];

		for(int j=1; j<=N; j++)
			fscanf(input, "%u", &ch[N-j].X);

		for(int j=1; j<=N; j++)
			fscanf(input, "%u", &ch[N-j].V);

		int j=0;

		do {
			if(ch[j].X + ch[j].V*T >= B)
			{
				CH++;
			} else {
				swaps += (K-CH);
			}
			j++;
		} while(j<N && CH < K);

		if(CH >= K) cout << "Case #" << i << ": " << swaps << "\n";
		else cout << "Case #" << i << ": IMPOSSIBLE\n";
	}
	
	fclose(input);
}