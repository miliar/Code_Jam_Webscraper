#include <iostream>
using namespace std;

void solve()
{
	int N, K;
	cin >> N >> K;

	K++;

	if (K % (1<<N) == 0)
		cout << "ON";
	else
		cout << "OFF";
	
	cout << endl;
}

int main()
{
	int ncase; cin >> ncase;
	for(int icase=0; icase < ncase; icase++)
	{
		cout << "Case #" << (icase+1) << ": ";
		solve();
	}
}
