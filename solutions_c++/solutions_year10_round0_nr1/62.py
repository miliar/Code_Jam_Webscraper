#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int cn=1;cn<=T;cn++)
	{
		int N, K;
		cin >> N >> K;
		int tot = (1<<N);
		cout << "Case #" << cn << ": ";
		if((K+1)%tot == 0) cout << "ON" << endl;
		else cout << "OFF" << endl;
	}
	return 0;
}
