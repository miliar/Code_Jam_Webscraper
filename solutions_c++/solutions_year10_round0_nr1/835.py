#include<iostream>
#include<cmath>
#include<bitset>
#include<cstdio>
using namespace std;

int main()
{
	//bitset<11> snappers;
	int T;
	cin >> T;
	for(int t = 0; t < T; t++)
	{
		int N, K;
		cin >> N >> K;
		K = K % (1 << N);
		bool hasPower = true;
		for(int k = 0; k < N && hasPower; k++)
		{
			if((K & (1 << k)))
				continue;
			hasPower = false;
		}
		cout << "Case #" << (t+1) << ": " << (hasPower?"ON":"OFF") << endl;
	}
	return 0;
}
