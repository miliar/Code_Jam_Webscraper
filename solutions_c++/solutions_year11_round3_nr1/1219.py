#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char** argv)
{
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		int R, C;
		cin >> R >> C;
		vector <string> v(R);
		for (int j = 0; j < R; ++j)
			cin >> v[j];
		bool impossible = false;
		for (int j = 0; j < v.size(); ++j)
			for (int k = 0; k < v[j].size(); ++k)
				if (v[j][k] == '#')
				{
					if (j + 1 < v.size() && k < v[j].size() && v[j][k + 1] == '#' && v[j + 1][k] == '#' && v[j + 1][k + 1] == '#')
					{
						v[j][k] = v[j + 1][k + 1] = '/';
						v[j][k + 1] = v[j + 1][k] = '\\';
					}
					else
						impossible = 1;
				}
		cout << "Case #" << (i + 1) << ":" << endl;
		if (impossible)
			cout << "Impossible" << endl;
		else
			for (int j = 0; j < v.size(); ++j)
				cout << v[j] << endl;
	}
	return 0;
}
