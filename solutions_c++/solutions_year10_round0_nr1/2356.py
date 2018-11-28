#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("answer.txt","w",stdout);

	int N,K,T;
	cin >> T;

	for(int i=1;i<=T;i++)
	{
		cin >> N >> K;

		cout << "Case #" << i << ": ";
		if ((K+1)%(1<<N)) cout << "OFF" << endl; else cout << "ON" << endl;
	}

	return 0;
}
