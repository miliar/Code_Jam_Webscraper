#include <iostream>
#include <sstream>
#include <cstring>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <map>
#include <deque>
#include <set>
#include <algorithm>

using namespace std;

int main()
{
	ofstream fout("A-large.out");
	ifstream fin("A-large.in");
	
	int T;
	fin >> T;
	for(int i = 0; i < T; i++)
	{
		int N, K;
		fin >> N >> K;
		
		long long x = (1<<N);
		K %= x;
				
		if(K != x-1)		
			fout << "Case #" << i+1 << ": " << "OFF" << endl;
		else fout << "Case #" << i+1 << ": " << "ON" << endl;
	}

	return 0;

}
		
