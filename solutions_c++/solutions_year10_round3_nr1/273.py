#include <iostream>
#include <math.h>

using namespace std;

struct wire {
	int A;
	int B;
};

int T, N, A, B, C;
wire *W;

void quicksort(int lo, int hi) {
    int Lo, Hi;
	int p;

	Lo = lo;
    Hi = hi;

	p = W[(Lo + Hi) / 2].A;

	do {
		while(W[Lo].A < p) Lo++;
		while(p < W[Hi].A) Hi--;
		if(Lo <= Hi) {
			wire h = W[Lo];
			W[Lo] = W[Hi];
			W[Hi] = h;
			Lo++;
			Hi--;
		}
	} while(Lo <= Hi);

	if(Hi > lo) quicksort(lo, Hi);
    if(Lo < hi) quicksort(Lo, hi);
}

void main(int argc, char **argv)
{
	FILE *input;

	input = fopen(argv[1], "r");

	fscanf(input, "%u", &T);

	for(int i=1; i<=T; i++)
	{
		C = 0;
		fscanf(input, "%u", &N);

		W = new wire[N];

		for(int j=0; j<N; j++)
		{
			fscanf(input, "%u %u", &A, &B);
			W[j].A = A;
			W[j].B = B;
		}

		quicksort(0, N-1);

		for(int k=0; k<N-1; k++)
		{
			for(int l=0; l<N-1-k; l++)
			{
				if(W[l+1].B < W[l].B) {
					C++;
					int h = W[l].B;
					W[l].B = W[l+1].B;
					W[l+1].B = h;
				}
			}
		}

		cout << "Case #" << i << ": " << C << "\n";
	}

	fclose(input);
}