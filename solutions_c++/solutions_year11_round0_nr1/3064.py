#include <iostream>
#include <cstdio>
#include <cmath>

#define ct (int) 1e4

using namespace std;

struct action
{
	int num;
	char c;
};

int abs (int a)
{
	return ((a >= 0)? a : -a);
}

int t, n, o[ct], b[ct], o_n, b_n, x1, x2;
action all[ct];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> t;

	for (int i = 0; i < t; i++)
	{
		o_n = 0;
		b_n = 0;

		cin >> n;
		for (int j = 0; j < n; j++)
		{
			cin >> all[j].c >> all[j].num;	

			if (all[j].c == 'O')
				o[o_n++] = all[j].num;	
			else
				b[b_n++] = all[j].num;
		}

		x1 = 1;
		x2 = 1;
                  
		int ans = 0, num1 = 0, num2 = 0, num_all = 0;

		/*
		cout << "ACTION # " << i << ":" << endl << "	";
			for (int j = 0; j < n; j++)
				cout << all[j].num << ' ' << all[j].c << "; ";
		
		cout << endl << "Orange's action: ;" << endl;
		for (int j = 0; j < o_n; j++)
			cout << o[j] << ' ';
		
		cout << endl << "Blue's action: " << endl;
		for (int j = 0; j < b_n; j++)
			cout << b[j] << ' ';     	
		cout << endl;
		*/

		while (num_all < n)
		{	
			ans++;

			bool flag1 = false, flag2 = false;

			if (num1 < o_n && x1 != o[num1])
			{
				x1 += (o[num1] - x1) / abs(o[num1] - x1);
				flag1 = true;	
			}

			if (num2 < b_n && x2 != b[num2])
			{
				x2 += (b[num2] - x2) / abs(b[num2] - x2); 
				flag2 = true;
			}


			if (!flag1 && all[num_all].c == 'O')
			{
				num_all++;
				num1++;
			}	
			else if (!flag2 && all[num_all].c == 'B')
			{
				num_all++;
				num2++;
			}

			//cout << "	stap#" << ans << ": x1 = " << x1 << ", x2 = " << x2 << endl;	
		}

		cout << "Case #" << i + 1 << ": " << ans << endl;
	}

	return 0;
}