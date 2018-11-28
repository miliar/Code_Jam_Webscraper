#include <iostream>

using namespace std;

int main()
{
	int t;   
	int n;
    cin >> t;
    
    for(int tt=1; tt<=t; tt++)
    {
		cin >> n;
		int now = 0;
		int posO = 1, posB = 1;
		char ch;
		int a;
		int res = 0;
		int timeO = 0, timeB = 0;
		
		for(int i=0; i<n; i++)
		{
			cin >> ch >> a;
			if (ch == 'O')
			{
				if (posO >= a)
				{
					if (posO - timeO <= a) { res++; timeB++; }
					else { res += posO - timeO - a + 1; timeB += posO - timeO - a + 1; }
				}
				else
				{
					if (posO + timeO >= a) { res++; timeB++; }
					else { res += a - posO - timeO + 1; timeB += a - posO - timeO + 1; }
				}
				timeO = 0;
				posO = a;
			}
			else
			{
				if (posB >= a)
				{
					if (posB - timeB <= a) { res++; timeO++; }
					else { res += posB - timeB - a + 1; timeO += posB - timeB - a + 1; }
				}
				else
				{
					if (posB + timeB >= a) { res++; timeO++; }
					else { res += a - posB - timeB + 1; timeO += a - posB - timeB + 1; }
				}
				timeB = 0;
				posB = a;
			}
		}
		
		printf("Case #%d: %d\n", tt, res);
    }
    return 0;
}
