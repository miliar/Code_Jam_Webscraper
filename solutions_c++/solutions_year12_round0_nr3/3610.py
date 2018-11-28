#include <iostream>
using namespace std;

int main()
{
  int T; cin >> T;
	int caseNum = 1;
	
	while(T > 0)
	{
		int A,B;
		cin >> A >> B;
		int ans = 0;
		
		if(B > 9 && (A < 1000 && B <1000))
		{
			int num = A;
			if(B <= 99)
			{
				while(num < B)
				{
					int a,b;
					b = num % 10;
					a = (num - b)/10;
					
					int m = b * 10 + a; 
					if (b != 0 && num < m && m <= B) ans++;
					
					num++;
				}
			}
			else
			{
				while(num < B)
				{
					int a,b,c;
					c = num % 10;
					b = ((num % 100) - c)/10;
					a = (num - b*10 -c)/100;
					//cout << "a,b,c = " << a << " " << b << " " << c << " " << endl; //debug
					
					int m = b * 100 + c * 10 + a;
					if (b != 0 && num < m && m <= B) ans++;
					
					m = c * 100 + a * 10 + b;
					if (c != 0 && num < m && m <= B) ans++;
				
					num++;
				}
			}
		}
		
		cout << "Case #" << caseNum << ": " << ans << endl;
		caseNum++;
		T--;
	}

  return 0;
}
