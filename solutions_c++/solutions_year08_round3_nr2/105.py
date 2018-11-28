#include <iostream>
#include <vector>
#include <stdio.h>
#include <string>
#include <cmath>
#include <algorithm>
#include <set>

using namespace std;

struct tt
{
	int x, y;
};


int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	int r;
	cin >> r;
	string temp;
	getline(cin, temp);
	for (int y = 1; y <= r; y++)
	{
		getline(cin, temp);
		long long cnt = 0;
		long long d = temp.length();
		long long tt = 1;
		for (int i = 1; i < d; i++)
			tt *= 3;
		for (int i = 0; i < tt; i++)
		{
			vector<int> a;
			int tmp = i;
			do 
			{ 
				a.push_back(tmp % 3);
				tmp /= 3;
			} 
			while(tmp);
			while(a.size() < d - 1) 
				a.push_back(0);
			long long t1 = temp[0] - '0';
			long long t2 = 0;
			long long j1;
			long long yy  = 0;
			for (j1 = 0; j1 < d - 1 && a[j1] == 0; j1++)
				t1 = t1 * 10 + temp[j1+1] - '0';
			for (int j = j1; j < d - 1; j++)
			{
				if (a[j] == 0)
					t2 = t2 * 10 + temp[j+1] - '0';
				if (a[j] == 1)
				{
					if (yy == 1)
						t1 += t2;
					else if (yy == 2)
						t1 -= t2;
					t2 = 0;
					t2 = t2 * 10 + temp[j+1] - '0';
					yy = 1;
				}
				if (a[j] == 2)
				{
					if (yy == 1)
						t1 += t2;
					else if (yy == 2)
						t1 -= t2;
					t2 = 0;
					t2 = t2 * 10 + temp[j+1] - '0';
					yy = 2;
				}
			}
					if (yy == 1)
						t1 += t2;
					else if (yy == 2)
						t1 -= t2;
			if (t1 % 5 == 0 || t1 % 2 == 0 || t1 % 3 == 0 || t1 % 7 == 0)
				cnt++;
		}



		cout << "Case #" << y << ": " << cnt << endl;
	}
	return 0;
}

