#include <iostream>
#include <vector>

using namespace std;

int solve(int R, int k, int N, vector<int> &g)
{
	vector<int> nv, cv;
	nv.resize(N);
	cv.resize(N);
	
	int i;
	for(int j=0;j<N;j++)
	{
		i = j;
		int c=g[i];
		i = (i+1)%N;
		while(c+g[i]<=k&&i!=j)
		{
			c += g[i];
			i = (i+1)%N;
		}
		nv[j] = i;
		cv[j] = c;
	}
	
	i = 0;
	int euro = 0;
	for(int r=0;r<R;r++)
	{
		euro += cv[i];
		i = nv[i];
	}
	return euro;
}

int main(void)
{
	int T;
	cin >> T;
	
	for(int i=0;i<T;i++)
	{
		int R,k,N;
		cin >> R >> k >> N;
		vector<int> g;
		g.resize(N);
		for(int j=0;j<N;j++)
		{
			cin >> g[j];
		}
		cout << "Case #" << i+1 << ": "<<solve(R,k,N,g)<< endl;
	}
	return 0;
}
