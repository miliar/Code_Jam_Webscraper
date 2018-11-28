#include <ctime>
#include <vector>
#include <fstream>
#include <iostream>
using namespace std;

vector<char> state;
vector<char> recv;
bool Solve(int n, int k)
{
	for(int i = 0; i < n; i++)
		if((k & (1 << i)) == 0)
			return false;
	return true;
}

int main()
{
	ifstream in("in.txt");
	int tests, n, k;
	in >> tests;
	for(int test = 1; test <= tests; test++)
	{
		in >> n >> k;
		cout << "Case #" << test << ": " << (Solve(n, k) ? "ON" : "OFF") << endl;
	}
	return 0;
}