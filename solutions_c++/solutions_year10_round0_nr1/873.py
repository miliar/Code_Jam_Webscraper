#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int t=1; t<=T; ++t)
	{
		unsigned int N, K;
		cin >> N >> K;
		bool on = ((1<<N)-1 & K) == ((1<<N)-1) ;
		cout << "Case #" << t << ": " << (on ?"ON" :"OFF") << endl;
	}

	return 0;
}
