#include <iostream>


using namespace std;

int main ()
{
	int cases;
	cin >> cases;
	int N;
	int R=0;
	int num;
	int sum=0;
	int min=200000000;
	for (int i=0;i<cases;++i)
	{
		R = 0;
		sum = 0;
		min=2000000000;
		cin >> N;
		
		for (int j=0;j<N;++j)
		{
			cin >> num;
			if (num < min)
				min = num;
			sum += num;
			R ^= num;
		}
		if (R != 0)
			cout << "Case #" << i+1 << ": NO" << endl;
		else
		{
			cout << "Case #" << i+1 << ": " << sum-min << endl;
		}
	}
}
