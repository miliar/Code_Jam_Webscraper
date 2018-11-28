#include <iostream>
using namespace std;

int main()
{
	int pos_o, pos_b, left_o, left_b;

	int cnt, fact;
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	cin >> cnt;

	char role;
	int pos;
	int total = 0;

	int i = 0;
	while (cnt--) 
	{	
		++i;
		pos_o = pos_b = 1;
		left_o = left_b = 0;

		cin >> fact;
		while (fact--) 
		{
			cin >> role >> pos;
			if (role == 'B')
			{
				if (abs(pos - pos_b) > left_b)
				{
					left_o += abs(pos - pos_b) - left_b;
					total += abs(pos - pos_b) - left_b;
				}

				left_o += 1;
				left_b = 0;
				pos_b = pos;
			}
			else
			{
				if (abs(pos - pos_o) > left_o)
				{
					left_b += abs(pos - pos_o) - left_o;
					total += abs(pos - pos_o) - left_o;
				}

				left_b += 1;
				left_o = 0;
				pos_o = pos;
			}
			total += 1;
		}
		cout << "Case #" << i << ": " << total << endl;
		total = 0;
	}

	return 0;
}