#include<iostream>


using namespace std;
int main()
{
	int t;
	cin >> t;
	
	for(int i = 1; i <= t; i++)
	{
		int n, k;
		cin >> n >> k;
		k = k % (1<<n);
		cout << "Case #"<<i<<": ";
		if(k == ( (1<<n) - 1))
			cout << "ON";
		else
			cout << "OFF";
		cout << endl;
	}
	return 0;
}
