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

int xyz(int N, int K)
{
	int p = (int)pow(2.0, N);
	return (K+1)%p == 0;
}

int main()
{
	ifstream ifs("A-large.in", ios::in);
	ofstream ofs("A-large.out", ios::out);
	int C;
	ifs>>C;
	for(int i = 0; i < C; i++)
	{
		int N, K;
		ifs>>N;
		ifs>>K;
		bool f = xyz(N, K);
		ofs<<"Case #"<<(i+1)<<": "<<(f?"ON":"OFF")<<endl;
	}
}
