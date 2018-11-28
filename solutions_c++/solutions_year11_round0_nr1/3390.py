#include <vector>
#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int i = 0 ; i < T ; i ++)
	{
		int N;
		cin >> N;

		vector<int> vo, vb;
		vector<char> v;
		for (int j = 0 ; j < N ; j ++)
		{
			char c;
			int p;
			cin >> c >> p;
			v.push_back(c);
			if (c == 'O')
				vo.push_back(p);
			else
				vb.push_back(p);
		}

		int bpos = 1;
		int opos = 1;
		int iv, ivo, ivb;
		iv = 0;
		ivo = 0;
		ivb = 0;

		int t = 0;
		while (true)
		{
			bool pushed = false;
			bool moved = false;
			if (ivo < vo.size())
			{
				if (opos == vo[ivo])
				{
					if (v[iv] == 'O')
					{
						t ++;
						iv ++;
						ivo ++;
						pushed = true;
					}
				}
				else
				{
					if (opos < vo[ivo])
						opos ++;
					else
						opos --;
					moved = true;
				}
			}
			else
				moved = true;

			if (ivb < vb.size())
			{
				if (bpos == vb[ivb])
				{
					if (v[iv] == 'B' && !pushed)
					{
						t ++;
						iv ++;
						ivb ++;
						pushed = true;
					}
				}
				else
				{
					if (bpos < vb[ivb])
						bpos ++;
					else
						bpos --;
					moved = true;
				}
			}
			else
				moved = true;

			//cout << opos << " :: " << bpos << " :: " << iv << endl;
			if (moved && !pushed)
				t ++;

			if (iv >= v.size())
				break;
		}
		cout << "Case #" << i+1 << ": " << t << endl;
	}
	return 0;
}
