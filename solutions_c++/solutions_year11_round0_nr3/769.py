#include <stdio.h> 
#include <vector> 
#include <list>
#include <string>
#include <set>
#include <algorithm> 
#include <fstream> 
#include <iostream> 
using namespace std;

int main() 
{ 
	int T;
	cin >> T;
	
	for (int test = 1; test <= T; ++test)
	{
		int N;
		cin >> N;
		int Min = 10000000;
		unsigned sum = 0;
		int xor = 0;
		for (int i = 0; i < N; ++i)
		{
			int a;
			cin >> a;
			if (Min > a)
				Min = a;
			sum += a;
			xor ^= a;
		}
		if (xor)
		{
			cout << "Case #" << test << ": NO\n";		
		}
		else
		{
			cout << "Case #" << test << ": " << (sum-Min) << "\n";		
		}
	}
#ifndef ONLINE_JUDGE
#ifndef FULLREDIRECT
	ifstream console("CONIN$");
	char fdasfadsfdasfdsa;
	console.getline(&fdasfadsfdasfdsa,1);
	console.close();
#endif
#endif
	return 0; 
}