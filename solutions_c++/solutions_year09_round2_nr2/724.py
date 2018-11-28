#include <iostream>
#include <algorithm>
#include <queue>
#include <string>
using namespace std;

void work()
{


}

int main()
{

	freopen("lol4.in", "r", stdin);
	freopen("lol.out", "w", stdout);






	char lol[1000];
/*
	string a;
	getline(cin, a);

	for (int x=0; x<a.size(); x++)
		lol[x] = a[x];

	next_permutation(lol, lol+a.size());
	for (int x=0; x<a.size(); x++)
		cout << lol[x];
	cout << endl;
	return 0;
*/


	int T;
	scanf("%d\n", &T);
	for (int x=0; x<T; x++)
	{
		string s;
		getline(cin, s);

		for (int a=0; a<s.size(); a++)
			lol[a] = s[a];

		next_permutation(lol, lol+s.size());

		string t = "";
		for (int a=0; a<s.size(); a++)
			t += lol[a];

		printf("Case #%d: ", x+1);
		if (t > s)
			cout << t << endl;
		else
		{
			if (t[0] != '0')
			{
			cout << t[0];
			cout << "0";
			for (int y=1; y<t.size(); y++)
				cout << t[y];
			cout << endl;
			}
			else
			{
				int a;
				for (a=0; a<t.size(); a++)
					if (t[a] != '0')
						break;

				cout << t[a];
				cout << "0";
				cout << t.substr(0, a);
				cout << t.substr(a+1, t.size()-a-1);
				cout << endl;





			}
		}



	}
}
