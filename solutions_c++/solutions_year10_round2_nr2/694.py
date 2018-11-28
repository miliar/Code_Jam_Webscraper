#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <queue> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <fstream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
#include <cstring> 
using namespace std;

string xyz(vector<int> X, vector<int> V, int K, int B, int T)
{
	vector<int> dis;
	for(int i = 0; i < X.size(); i++)
	{
		int dist = T * V[i];
		dis.push_back(dist + X[i]);
	}
	int swaps = 0;
	int k = 0;
	for(int i = X.size() - 1; i >=0; i--)
	{
		if(dis[i] < B && k < K)
		{
			for(int j = i-1; j >= 0; j--)
			{
				if(dis[j] >= B)
				{
					int temp = dis[j];
					dis[j] = dis[i];
					dis[i] = temp;
					swaps += i - j;
					k++;
					break;
				}
			}
		}
		else
		{
			k++;
		}
	}
	stringstream ss;
	if(k >= K)
		ss<<swaps;
	else ss<<"IMPOSSIBLE";
	return ss.str();
}

int main()
{
	ifstream ifs("B-large.in", ios::in);
	ofstream cout("a-small.out", ios::out);
	int C;
	ifs>>C;
	for(int j = 0; j < C; j++)
	{
		int N, K, B, T;
		ifs>>N>>K>>B>>T;
		vector<int> X, V;
		for(int i = 0; i<N; i++)
		{
			int xx;
			ifs>>xx;
			X.push_back(xx);
		}
		for(int i = 0; i<N; i++)
		{
			int xx;
			ifs>>xx;
			V.push_back(xx);
		}
		cout<<"Case #"<<(j+1)<<": "<<xyz(X, V, K, B, T)<<endl;
	}
}