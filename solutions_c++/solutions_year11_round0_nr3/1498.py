#include <iostream>
using namespace std;

int main ()
{
	int T;
	int cases;
	cin >> T;

	for (cases=1 ;cases<=T ;cases++)
	{
		cout << "Case #" << cases << ": ";

		int N;
		cin >> N;
		int data[10000];
		for (int i=0 ;i<N ;i++)
			cin >> data[i];

		int sum = 0;
		int total = 0;
		int min = data[0];
		for (int i=0 ;i<N ;i++)
		{
			sum ^= data[i];
			total += data[i];
			if (data[i]<min)
				min = data[i];
		}

		if (sum!=0)
		{
			cout << "NO" << endl;
		}
		else
			cout << total - min << endl;


	}
	return 0;
}
