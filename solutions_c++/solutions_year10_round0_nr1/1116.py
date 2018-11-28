#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int n;
	cin >> n;

	for(int i=0; i<n; ++i)
	{
		int n,k;
		cin >> n >> k;
		cout << "Case #" << i+1 << ": " << (k%(1<<n)==((1<<n)-1) ? "ON" : "OFF") << endl;	
	}

	return 0;
}