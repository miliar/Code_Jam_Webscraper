#include <iostream>

using namespace std;

int main (int argc, char **argv)
{
	int cases, N;
	long long K;
	cin >> cases;
	
	for(int i=0; i<cases; i++)
	{
		cin >> N >> K;
		
		int max = 1<<N;
		if ((K % max) == (max-1))
			cout << "Case #" << i+1 << ": ON" << endl;
		else
			cout << "Case #" << i+1 << ": OFF" << endl;
		
	}
	
	return 0;
}