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

int xyz(int R, int K, vector<int> v)
{
	int c = 0;
	int n = v.size();
	int euros = 0;
	for(int i = 0; i < R; i++)
	{
		int k = 0;
		int cc = 0;
		while(k + v[c%n] <= K && cc < n) 
		{
			k += v[c%n];
			c++;
			cc++;
		}
		euros += k;
	}
	return euros;
}

int main()
{
	ifstream ifs("C-small-attempt0.in", ios::in);
	ofstream cout("C-small-attempt0.out", ios::out);
	int C;
	ifs>>C;
	for(int i = 0; i < C; i++)
	{
		int R, K, N;
		ifs>>R>>K>>N;
		vector<int> q;
		for(int j = 0; j < N; j++)
		{
			int c;
			ifs>>c;
			q.push_back(c);
		}
		cout<<"Case #"<<(i+1)<<": "<<(xyz(R, K, q))<<endl;
	}
}
