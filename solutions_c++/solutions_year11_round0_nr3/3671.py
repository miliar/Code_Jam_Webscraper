#include <iostream>

using namespace std;

unsigned int patric_calc(int N, int offset, unsigned int * C)
{
	int sum = 0;
	for (int i = offset; i < N; i++) sum ^= C[i];
	return sum;
}

unsigned int sean_calc(int N, int offset, unsigned int * C)
{
	int sum = 0;
	for (int i = offset; i < N; i++) sum += C[i];
	return sum;
}

int cmp(const void * a, const void * b)
{
	return ( *(unsigned int*)b - *(unsigned int*)a );
}

void calc(int T, int N, unsigned int * C)
{
	cout<<"Case #"<<T<<": ";
	qsort(C, N, sizeof(unsigned int), cmp);

	int half = N - 1;

	if (patric_calc(half, 0, C) != patric_calc(N, half, C)) cout<<"NO";
	else cout<<max(sean_calc(half, 0, C), sean_calc(N, half, C));

	cout<<endl;
}

int main(int argc, char * argv[])
{
	int T, Tc = 1;
	cin>>T;

	while (T--)
	{
		int N;
		cin>>N;

		unsigned int * C = new unsigned int[N];
		for (int i = 0; i < N; i++)	cin>>C[i];
		calc(Tc++, N, C);

		delete [] C;
	}
	return 0;
}