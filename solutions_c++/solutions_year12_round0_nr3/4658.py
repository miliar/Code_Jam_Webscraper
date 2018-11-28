#include <iostream>
using namespace std;
int main()
{
	int T = 0; cin >> T;
	for (int x = 1; x <= T; x++)
	{
		cout << "Case #" << x << ": ";
		//Logic here
		int A = 0, B = 0, y = 0;
		cin >> A >> B;
		if ( A < 100)
		{
			int n = A;
			while (n <= B)
			{
				int d1 = n / 10;
				int d2 = n % 10;
				
				int m = (d2 * 10) + d1;
				if (m <= B && n < m) y++;
				n++;
			}
		}
		else if ( A < 1000)
		{
			int n = A;
			while (n <= B)
			{
				int d1 = n / 100;
				int d2 = (n % 100) / 10;
				int d3 = (n % 100) % 10; 
				
				int m = (d3 * 100) + (d1 * 10) + d2;
				if (m <= B && n < m) y++;
				
				m = (d2 * 100) + (d3 * 10) + d1;
				if (m <= B && n < m) y++;
				n++;
			}
		}
		else if ( A < 10000)
		{
			int n = A;
			while (n <= B)
			{
				int d1 = n / 1000;
				int d2 = (n % 1000) / 100;
				int d3 = (n % 1000) % 100 / 10;
				int d4 = (n % 1000) % 100 % 10;
				
				int m = (d4 * 1000) + (d1 * 100) + (d2 * 10) + d3;
				if (m <= B && n < m) y++;
				
				m = (d3 * 1000) + (d4 * 100) + (d1 * 10) + d2;
				if (m <= B && n < m) y++;		
				
				m = (d2 * 1000) + (d3 * 100) + (d4 * 10) + d1;
				if (m <= B && n < m) y++;	
				n++;
			}
		}
		else if ( A < 100000)
		{
			int n = A;
			while (n <= B)
			{
				int d1 = n / 10000;
				int d2 = (n % 10000) / 1000;
				int d3 = (n % 10000) % 1000 / 100;
				int d4 = (n % 10000) % 1000 % 100 / 10;
				int d5 = (n % 10000) % 1000 % 100 % 10;
				
				int m = (d5 * 10000) + (d1 * 1000) + (d2 * 100) + (d3 * 10) + d4;
				if (m <= B && n < m) y++;
				
				m = (d4 * 10000) + (d5 * 1000) + (d1 * 100) + (d2 * 10) + d3;
				if (m <= B && n < m) y++;		
				
				m = (d3 * 10000) + (d4 * 1000) + (d5 * 100) + (d1 * 10) + d2;
				if (m <= B && n < m) y++;	
				
				m = (d2 * 10000) + (d3 * 1000) + (d4 * 100) + (d5 * 10) + d1;
				if (m <= B && n < m) y++;					
				n++;
			}
		}		
		cout << y;
		//End Logic
		cout << endl;
	}	
	return 0;
}
