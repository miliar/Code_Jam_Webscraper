
#include <iostream>

using namespace std;

struct o
{
	bool p;
	int i;
};

o data[1000];

int test(int n)
{
	while (n > 1)
	{
		if (!data[n].p) return false;
		n = data[n].i;
	}
	return true;
}

int main()
{
	int results[30], n;
	for (n = 2; n <= 25; n++)
	{
	//int n;
	//cin >> n;

	int total = 0;
	for (int i = 0; i < (1 << n-2); i++)
	{
		//cout << "set " << i << ": ";
		int pos = 0;
		for (int j = 2; j < n; j++)
		{
			data[j].p = ((i >> (j-2)) & 1);
			if (data[j].p)
			{
				pos++;
				data[j].i = pos;
				//cout << j << " ";
			}
		}
		data[n].p = true;
		data[n].i = pos + 1;
		
		if (test(n))
		{
			total++;
			//cout << "is pure";
		}

		//cout << endl;
	}
	//cout << (total % 100003) << endl;
	results[n] = total % 100003;
	}

	cin >> n;
	for (int i = 1; i < n+1; i++)
	{
		int d;
		cout << "Case #" << i << ": ";
		cin >> d;
		cout << results[d] << endl;
	}

	return 0;
}

