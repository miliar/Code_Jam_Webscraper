#include <iostream>
#include <string>
#include <map>

#define NUM 1440

using namespace std;

inline int conv(string str)
{
	return (str[0] - '0')*10*60 + (str[1] - '0')*60 + (str[3] - '0')*10 + (str[4] - '0');
}

int main()
{
	int n, count = 1;
	int trainsa[NUM + 10]; int trainsb[NUM + 10];

	cin >> n;

	for (; n>0; n--)
	{
		int t, numa, numb;
		cin >> t;

		for (int i=0; i<NUM; i++)
			trainsa[i] = trainsb[i] = 0;

		cin >> numa; cin >> numb;

		for (int i = 0; i < numa; i++)
		{
			string str1, str2;
			cin >> str1; cin >> str2;
			trainsa[conv(str1)]--; trainsb[conv(str2) + t]++;
		}
		for (int i = 0; i < numb; i++)
		{
			string str1, str2;
			cin >> str1; cin >> str2;
			trainsb[conv(str1)]--; trainsa[conv(str2) + t]++;
		}

		int suma = 0, sumb = 0, mina = 0, minb = 0;
		for (int i = 0; i < NUM; i++)
		{
			suma += trainsa[i]; sumb += trainsb[i];
			if (suma < mina) mina = suma; if (sumb < minb) minb = sumb;
		}

		cout << "Case #" << count++ << ": " << -mina << " " << -minb << endl;
	}

	return 0;
}
