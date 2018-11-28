

#include <iostream>

using namespace std;


int main()
{
	int T, i;
	char dummy;
		
	cin >> T;
	scanf("%c", &dummy);
	
	for(i =1; i <= T; i++)
	{
		int n, s, p, G, j;
		int tot = 0;
				
		cin >> n >> s >> p;
		
		for(j = 0; j < n; j++)
		{
			cin >> G;
			
			int div = G/3;
			int m = G % 3;
			
			if(div >= p)
			{
				tot++;
			}
			else
			{			
				if((m == 0) && (s > 0) && (div > 0))	
				{
					if((div + 1) >= p)
					{
						tot++;
						s--;
					}
				}
				else if((m > 0) && ((div + 1) >= p))
				{
					tot++;
				}
				else if((m == 2) && (s > 0))
				{
					if((div + 2) >= p)
					{
						tot++;
						s--;
					}
				}
			}
		}
		
		cout << "Case #" << i << ": " << tot << endl;
		
	}
	
}

