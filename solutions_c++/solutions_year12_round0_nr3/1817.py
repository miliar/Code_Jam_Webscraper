#include <fstream>
#include <string>
#include <set>
using namespace std;

int getLength(int a)
{
	int length = (a == 0) ? 1 : 0;
	while (a)
	{
		length++;
		a /= 10;
	}
	return length;
}

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int N;
	cin >> N;
	for (int tc = 1; tc <= N; tc++)
	{
		int a, b;
		cin >> a >> b;

		int length = getLength(a);
		int multiplier = pow(10.0, length - 1);

		set<pair<int, int>> s;
		for (int i = a; i <= b; i++)
		{
			int value = i;
			for (int j = 0; j < length - 1; j++)
			{
				int lastChar = value % 10;
				int newValue = lastChar * multiplier + value / 10;

				if (newValue != i && newValue >= a && newValue <= b)
				{
					s.insert(make_pair(i, newValue));
				}

				value = newValue;
			}			
		}

		cout << "Case #" << tc << ": " << s.size() / 2 << endl;
	}
	return 0;
}