#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream> 
#include <fstream> 
#include <algorithm>

using namespace std;

ofstream out("A.txt");
ifstream in("A-large.in");

int main()
{
	
	int T, N, K;
	in >> T;
	for(int t = 1; t <= T; t++)
	{
		in >> N >> K;
		out << "Case #" << t << ": "; 
		int i = 1 << N;
		if(K % i == (i - 1)) 
			out << "ON" << endl;
		else 
			out << "OFF" << endl;
	}	
	return 0;
}
 
