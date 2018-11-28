#include <iostream>
#include <cmath>
using namespace std;
long long abs(long long a)
{
	return (a >= 0? a : -a);
}
long long pb, po;
long long  tb, to;
int main()
{
	pb = 1;
	po = 1;
	tb = 0;
	to = 0;
	long long sum = 0;
	long long pos,time;
	char c;
	int cases;
	cin >> cases;
	int btns;
	for (int i = 0 ; i < cases; i++)
	{
		cin >> btns;
		for (int j = 0 ; j < btns; j++)
		{
			cin >> c;
			if (c == 'O')
			{
				cin >> pos;
				time = abs (pos - po) + 1;
				po = pos;
				to += time;
				if ( to*tb != 0 )
				{
					if (tb >= to){
						sum += tb; 
						tb = 0; to = 1;
					}else{
						sum += tb ;
						to -= tb; tb = 0; 
					}
				}
			}
			else // (c == 'B')
			{
				cin >> pos;
				time = abs (pos - pb)  + 1;
				pb = pos;
				tb += time;
				if ( to*tb != 0 )
				{
					if (tb <= to){
						sum += to;
						to = 0; tb = 1;
					}else{
						sum += to;
						tb -= to; to = 0;
					}
				}
			}
		}
		sum += to;
		sum += tb;
		cout << "Case #" << i + 1 << ": " << sum << endl;
		sum = 0;
		po = 1; pb = 1; tb = 0 ; to = 0;
	}
}
