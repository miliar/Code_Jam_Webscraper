#include "iostream"
#include "fstream"

using namespace std;

long calc(int R, int K, int N, long *g)
{
	long sum = 0;
	int j = 0;
	for(int i=0; i<R; i++)
	{
		long sub = 0;
		int idx = 0;
		while(sub <= K)
		{
			if(j > N - 1)
				j -= N;
			if(sub + g[j] > K)
				break;
			sub += g[j++];
			idx++;
			if(idx > N - 1)
				break;
		}
		sum += sub;
	}
	return sum;
}
void main()
{
	ifstream infile("C-small-attempt1.in");
	ofstream outfile("C-small.out");
	int C;
	long R, K, N;
	infile >> C;
	for(int i=0; i<C; i++)
	{
		infile >> R >> K >> N;
		long *g = new long[N];
		for(int j=0; j<N; j++)
		{
			infile >> g[j];
		}
		long sum = calc(R, K, N, g);
		outfile << "Case #" << i+1 << ": " << sum << endl;
	}
	infile.close();
	outfile.close();
}