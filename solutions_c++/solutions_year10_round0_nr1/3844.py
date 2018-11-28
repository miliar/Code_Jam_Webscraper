#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	unsigned T, c, N, K;
	string res;

	cin >> T;
	for (c=1; c<=T; c++)
	{
		cin >> N >> K;

		if (K!=0 && K%(1U<<N) == (1U<<N)-1)
			res="ON";
		else
			res="OFF";

		cout << "Case #" << c << ": " << res << endl;
	}
}
