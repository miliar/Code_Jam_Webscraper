
#include <iostream>

using namespace std;

int abs(int a)
{
	return (a < 0) ? -a : a;
}

int main()
{
	int N;

	int b_idle, o_idle;
	int b_pos, o_pos;
	int cpoint;
	char r_last;

	cin >> N;

	for (int i = 0; i < N; i++)
	{
		int n;
		cin >> n;

		b_idle = o_idle = 0;
		b_pos = o_pos = 1;
		cpoint = 0;
		r_last = 0;

		for (int j = 0; j < n; j++)
		{
			// robot, position
			char r;
			int p;

			cin >> r >> p;

			//cout << "Read: " << r << " " << p << ", ";

			if (r == r_last || r_last == 0)
			{
				if (r == 'B')
				{
					// blue
					int amount = abs(b_pos - p) + 1;
					cpoint += amount;
					o_idle += amount;
					b_idle = 0;
					b_pos = p;
					//cout << "state: (" << cpoint << " " << b_pos << " " << o_pos << " " << b_idle << " " << o_idle << ")" << endl;
				} else
				{
					// orange
					int amount = abs(o_pos - p) + 1;
					cpoint += amount;
					b_idle += amount;
					o_idle = 0;
					o_pos = p;
					//cout << "state: (" << cpoint << " " << b_pos << " " << o_pos << " " << b_idle << " " << o_idle << ")" << endl;
				}
			} else
			{
				if (r == 'B')
				{
					int amount = abs(b_pos - p) + 1;
					amount -= b_idle;
					if (amount <= 0) amount = 1;
					cpoint += amount;
					o_idle += amount;
					b_idle = 0;
					b_pos = p;
					//cout << "state: (" << cpoint << " " << b_pos << " " << o_pos << " " << b_idle << " " << o_idle << ")" << endl;
				} else
				{
					int amount = abs(o_pos - p) + 1;
					amount -= o_idle;
					if (amount <= 0) amount = 1;
					cpoint += amount;
					b_idle += amount;
					o_idle = 0;
					o_pos = p;
					//cout << "state: (" << cpoint << " " << b_pos << " " << o_pos << " " << b_idle << " " << o_idle << ")" << endl;
				}
			}

			r_last = r;
		}
		cout << "Case #" << (i+1) << ": " << cpoint << endl;
	}
}
