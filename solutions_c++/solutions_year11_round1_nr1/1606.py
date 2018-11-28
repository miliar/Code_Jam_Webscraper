#include <iostream>

using namespace std;

int main()
{
	bool done;
	int t, n, pd, pg, a, b, x, y;
	cin >> t;
	for(int i = 0; i < t; i++)
	{
		cout << "Case #" << i+1 << ": ";
		cin >> n >> pd >> pg;
		done = false;
		for(b = 1; b <= n; b++)
		{
			if(b*pd % 100 == 0) //This is a possible val
			{
				a = b*pd / 100;
				done = true;
				//cout << "HERE: " << a << " " << b << endl;
				break;
			}
		}

		if(done)
		{
			done = false;
			x = 0;
			while(true)
			{
				if(pg == 100 && a != b) { break; }
				if(pg == 0 && a != 0) { break; }
				else
				{
					//cout << "Possible" << endl;
					done = true;
					break;
				}
				if((100*a + 100*x - pg*b)%pg == 0 && (100*a + 100*x - pg*b)/pg >= x)
				{
					//cout << "Possible" << endl;
					done = true;
					break;
				}
				x++;
			}
		}

		if(done)
		{
			cout << "Possible" << endl;
		}
		else
		{
			cout << "Broken" << endl;
		}
	}
}
