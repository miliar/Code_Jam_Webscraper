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
		int ans = N;
		int *x = new int[N];
		for (int i = 0; i < N; ++i)
		{
			cin >> x[i];
			--x[i];
			if (x[i]==i)
				--ans;
		}
		/*int tot = 0;
		for (int i = 0; i < N; ++i)
		{
			if (x[i] == -1)
				continue;
			int c = -1;
			int j = i;
			while (x[j] != -1)
			{
				int t = x[j];
				x[j] = -1;
				j = t;
				++c;
			};
			tot += c;
		} */

		cout << "Case #" << test << ": " << (ans) << "\n";		
		
		delete [] x;
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