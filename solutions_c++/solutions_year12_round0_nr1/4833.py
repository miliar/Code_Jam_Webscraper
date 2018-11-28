#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <fstream>
using namespace std;


char mapping[30] = "yhesocvxduiglbkrztnwjpfmaq";
int main()
{
//	ifstream fin("A-small-attempt1.in");
//	ofstream fout("A-small-attempt1.out");
	freopen("A-small-attempt4(2).in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);
	for (int i = 0; i < 25; i++)
	{
		if (mapping[i] == 0)
			mapping[i] = i + 'a';
//		cout << mapping[i] << ' ';
	}
//	cout << endl;
	
	int n;
	cin >> n;
	cin.get();
//	printf("n = %d\n", n);
	for (int i = 1; i <= n; i++)
	{
//		system("pause");
		string s;
		getline(cin, s);
		cout << "Case #" << i << ": ";
		for (unsigned int i = 0; i < s.length(); i++)
		{
			if (s[i] != ' ')
				cout << mapping[s[i] - 'a'];
			else
				cout << ' ';
		}
		cout << endl;
	}
	
	return 0;
}
