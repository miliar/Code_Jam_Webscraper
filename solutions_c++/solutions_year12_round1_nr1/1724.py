#include <iostream>

using namespace std;

int main()
{
	int t;
	cin >> t;
	
	for(int i = 0; i < t; i++)
	{
		int a, b;
		cin >> a;
		cin >> b;
//		cout << a << " " << b << " ";

		float* probability = new float[a];
		for(int j = 0; j < a; j++)
		{
			cin >> probability[j];
//			cout << probability[j] << " ";
		}
		
		float minkey;
		float curkey;
		minkey = b + 2;
		float allcorrect = probability[0];

		for(int j = 1; j < a; j++)
		{
			int compkey = (b - a) + 2 * (a - j) + 1;
//			cout << "compkey=" << compkey << " ";
			curkey = allcorrect * compkey + (1 - allcorrect) * (compkey + b + 1);
			allcorrect *= probability[j];
//			cout << curkey << endl;
			if(minkey > curkey)
			{
				minkey = curkey;
			}
		}

//		allcorrect *= probability[a - 1];
		curkey = allcorrect * (b - a + 1) + (1 - allcorrect) * (b - a + 1 + b + 1);
//		cout << curkey << endl;
		if(minkey > curkey)
		{
			minkey = curkey;
		}

//		cout << endl;
		cout.precision(6);
		cout.setf(ios::fixed,ios::floatfield);
		cout << "Case #" << i + 1 << ": " << minkey << endl;
		delete [] probability;
	}	

	return 0;
}
