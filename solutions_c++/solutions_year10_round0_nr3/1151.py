#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int T, k, R, N, *g;
	int sum;
	int roller(int R, int k, int N, int *g);
	ifstream datain("C-small-attempt0.in");
	ofstream dataout("C-small-attempt0.out");
	datain>>T;
	for (int x=1; x<=T ;x++)
	{
		datain>>R>>k>>N;
		//cout<<R<<k<<N<<endl;
		int *g = new int [N];
		for (int i=0; i<N; i++)
		{
			datain>>g[i];
			//cout<<g[i];
		}
		//cout<<endl;
		sum = roller(R, k, N, g);
		delete [] g;
		dataout<<"Case #"<<x<<": "<<sum<<endl;
	}
	datain.close();
	dataout.close();
	return 0;
}

int roller(int R, int k, int N, int *g)
{
	int head = 0 , sum = 0;
	int *next = new int [N];
	int *add = new int [N];
	for (int i = 0; i < N; i++)
	{
		int j = 1 , s = g[i];
		while (j < N && s + g[(i+j) % N] <= k)
		{
			s += g[(i+j) % N];
			j++;
		}
		next[i] = j;
		add[i] = s;
	}
	for (int r = 0; r < R; r++)
	{
		sum += add[head]; 
		head = (head + next[head]) % N;
	}
	delete [] next;
	delete [] add;
	return sum;
}
