#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

//ifstream in("A-small.in");
//ofstream out("A-small.in");

int n,k;
int T;


int main()
{
	ifstream in("A-large.in");
    ofstream out("A-large.out");
	in >> T;
	for(int i = 0;i < T;i ++)
	{
		out << "Case #" << i + 1 << ": ";
		in >> n >> k;
		int N = (1 << n) - 1;
		k %= (N + 1);
		if(k == N)
		{
			out << "ON" << endl;
		}
		else
			out << "OFF" << endl;
	}

	
	return 0;
}
