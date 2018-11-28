#include <fstream>
#include <iostream>
using namespace std;

int main()
{
	ifstream is;
	is.open("C-small-attempt0.in");
	ofstream os;
	os.open("C-small-attempt0.out");
	
	int R,k,N;
	int T;
	is>>T;
	int sum;
	int total;
	for(int i = 0;i<T; i++)
	{
		total = 0;
		is>>R>>k>>N;
		int* p = new int[N];
		int j;
		for(j = 0; j<N; j++)
			is>>p[j];
		j = 0;
		for(int r = 0; r<R; r++)
		{
			sum = 0;
			int n = 0;
			while(sum <= k && n<=N)
			{
				sum += p[j++];
				j = j%N;
				n++;
			}
			total += sum - p[(j+N-1)%N ];
			j = (j-1+N)%N;
		}
		os<<"Case #"<<i+1<<": "<<total<<endl;
		delete [] p;
	}
				


	return 0;
}
