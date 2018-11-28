#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool solve(unsigned int N, unsigned int K)
{
	unsigned int n = 1u<<N;
	return (K+1)%n==0;
}

int main(int argc, char* argv[])
{
	unsigned int T, N, K;
	cin >> T;
	//cout << "T=" << T << endl;
	for(unsigned int i=0;i<T;i++)
	{
		cin >> N >> K;
		//cout << i << ": N=" << N << " K=" << K << endl;
		cout << "Case #" << i+1 << ": " << (solve(N,K)?"ON":"OFF") << endl;
	}
	
	return 0;
}
