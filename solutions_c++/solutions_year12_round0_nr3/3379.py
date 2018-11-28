#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int t, i, j, k, p, a, b, num, tmp, recycled, pw;
	int tt[10];
	bool ta;
	cin >> t;

	for(i = 1; i <= t; i++)
	{
		cin >> a >> b;
		num = 0;
		for(tmp = a; tmp <= b; tmp++)
		{
			recycled = tmp;
			pw = 0;
			while(recycled != 0)
			{
				recycled /= 10;
				pw++;
			}
			k = 0;
			for(j = 1; j < pw; j++)
			{
				recycled = tmp / pow(10, j);
				recycled = (tmp - recycled * pow(10, j)) * pow(10, pw - j) + recycled;
				if(recycled >=a && recycled <= b && recycled != tmp && recycled > pow(10, pw - 1)){
					num++;
				for(p = 0; p < k; p++)
					if(recycled == tt[p])
					{
						num--;
						ta = false;
						break;
					}
				if(ta)tt[k++] = recycled;
				}
				//if(recycled > tmp)cout << tmp << "," << recycled << endl;}
			}
		}
		cout << "Case #" << i << ": " << num / 2 << endl;
	}
	return 0;
}
