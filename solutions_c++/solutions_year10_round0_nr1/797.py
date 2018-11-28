#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>

using namespace std;
vector<unsigned int> e(32,0);
void init()
{
	e[0] = 1;
	for(int i = 1; i < 32; i++)
	{
		e[i] = e[i-1] * 2;
	}
}


int main()
{
	int T,N,K;
	ifstream input("A-large.in");
	ofstream out("test.out");
	input >> T;
	init();
	for(int i = 1; i <= T; i++)
	{
		input >> N >> K;
		if((K % e[N]) == e[N] - 1)
		{
			out << "Case #" << i << ": " << "ON" << endl;
		}
		else
		{
			out << "Case #" << i << ": " << "OFF" << endl;
		}
	}
	return 0;
}
