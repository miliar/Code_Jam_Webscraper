#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

int main()
{
	ifstream fin("A.in", ios_base::in);
	ofstream fout("A.out", ios_base::out);

	int t;
	fin >> t;

	for (int count = 0; count != t; ++count)
	{
		long result = 0;
		int k;
		fin >> k;
		fin.get();
		string diamond[2 * k - 1];

		for (int i = 0; i != 2 * k - 1; ++i)
		{
			getline(fin, diamond[i]);
//			cout << diamond[i] << endl;
		}

		bool v[2 * k - 1], h[2 * k - 1];
		for (int i = 0; i != 2 * k - 1; ++i	)
		{
			v[i] = h[i] = true;
		}

		for (int i = 0; i != 2 * k - 1; ++i)
			for (int j = abs(k - i - 1); j <= 2 * k - 2 - abs(k - i - 1); j += 2)
			{
				int x = i + 2;
				int y = j + 2;
				while (x <= 2 * k - 2 - abs(k - j - 1))
				{
					if (diamond[x][j] != diamond[i][j])
						h[(x + i) / 2] = false;
					x += 2;
				}
				while (y <= 2 * k - 2 - abs(k - i - 1))
				{
					if (diamond[i][y] != diamond[i][j])
						v[(y + j) / 2] = false;
					y += 2;
				}
			}
//
//		for (int i = 0; i != 2 * k - 1; ++i)
//			cout << h[i] << " ";
//		cout << endl;
//		for (int i = 0; i != 2 * k - 1; ++i)
//					cout << v[i] << " ";
//				cout << endl;

		int diffx = -1, diffy = -1;
		for (int i = 0; i != k; ++i)
		{
			if (diffx != -1 && diffy != -1) break;
			if (diffx == -1 && (h[k + i - 1] || h[k - 1 - i])) diffx = i;
			if (diffy == -1 && (v[k + i - 1] || v[k - i - 1])) diffy = i;
		}

		result = (diffx + diffy + k) * (diffx + diffy + k) - k * k;

		fout << "Case #" << (count + 1) << ": " << result << endl;
	}
	fin.close();
	fout.close();

	return 0;
}
