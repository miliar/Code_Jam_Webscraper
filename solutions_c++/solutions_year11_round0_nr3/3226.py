#include <fstream>
#include <iostream>
#include <string>
#include <list>

using namespace std;

inline int add(int a, int b)
{
	return a ^ b;
}

int main()
{
	int T = 0;
	int N = 0;
	int* values = 0;
	ifstream in("in.in");

	in >> T;

	for(int k = 0; k < T; k++)
	{
		in >> N;
		values = new int[N];
		list<int> valuesList;
		int sum = 0;
		for(int i = 0; i < N; i++)
		{
			int n = 0;
			in >> n;
			valuesList.push_back(n);
		}

		valuesList.sort();

		list<int>::iterator it = valuesList.begin();

		int n = 0;
		for(it = valuesList.begin(); it != valuesList.end(); it++)
		{
			values[n++] = *it;
		}

		bool found = false;
		int y = 0;

		for(int i = 1; (i < N) && !found; i++)
		{
			int seanPile = 0;
			int patrickPile = 0;
			for(int j = 0; j < i; j++)
			{
				seanPile = add(seanPile, values[j]);
			}
			for(int l = i; l < N; l++)
			{
				patrickPile = add(patrickPile, values[l]);
				y += values[l];
			}
			if(seanPile == patrickPile)
			{
				found = true;
			}
		}

		cout << "Case #" << k+1 << ": ";
		if(found)
		{
			cout << y;
		}else
		{
			cout << "NO";
		}
		cout << endl;
	}

	return 0;
}