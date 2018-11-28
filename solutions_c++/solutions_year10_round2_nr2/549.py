#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;
const double ESP = 1e-10;
int N,K,B,T;
vector<int> V;
vector<int> X;
vector<double> time;

int solve()
{
	int ret = 0;
	time.assign(N,0);
	int k = 0;
	int last = N;
	for(int i = 0; i < N; i++)
	{
		time[i] = double(B - X[i]) / double(V[i]);
	}
	for(int i = N - 1; i >= 0; i--)
	{
		if(time[i] <= T)
		{
			ret += last - i - 1;
			last--;
			k++;
			if(k >= K)
				break;
		}
	}
	if(k >= K)
		return ret;
	return -1;
}
int main()
{
	ifstream input("B-large.in");
	ofstream out("test.out");
	int C;
	input >> C;
	int result = 0;
	for(int i = 1; i <= C; i++)
	{
		input >> N >> K >> B >> T;
		V.clear();
		X.clear();
		int t;
		for(int j = 0; j < N; j++)
		{
			input >> t;
			X.push_back(t);
		}
		for(int j = 0; j < N; j++)
		{
			input >> t;
			V.push_back(t);
		}
		result = solve();
		if(result == -1)
		{
			out << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
		}
		else
		{
			out << "Case #" << i << ": " << result << endl;
		}
	}
	return 0;
}