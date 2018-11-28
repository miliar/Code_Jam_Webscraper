#include <iostream>
#include <queue>

using namespace std;

int T;
int R, k, N;
int g;

unsigned __int64 X;
queue<int> q;

void Solve()
{
	X = 0;
	int K = k;
	int f, n;

	for(int l=0; l<R; l++)
	{
		K = k;
		n = 0;
		do {
			n++;
			f = q.front();
			K -= f;
			q.pop();
			q.push(f);
		} while(K >= q.front() && n < N);

        X += (k - K);
	}
	
}

void main(int argc, char **argv)
{
	FILE *input;
	FILE *output;

	input = fopen(argv[1], "r");
	output = fopen(argv[2], "w");

	fscanf(input, "%u", &T);

	for(int i=1; i<=T; i++)
	{
		fscanf(input, "%u %u %u", &R, &k, &N);

		for(int j=0; j<N; j++)
		{
			fscanf(input, "%u ", &g);
			q.push(g);
		}

		Solve();

		while(!q.empty())
			q.pop();

		fprintf(output, "Case #%u: %I64u\n", i, X);
	}

	fclose(input);
	fclose(output);
}