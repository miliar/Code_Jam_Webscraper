#include <iostream>

using namespace std;

int main()
{
	int t;   

	int n, pd, pg;
    cin >> t;
    
    for(int tt=1; tt<=t; tt++)
    {
		cin >> n >> pd >> pg;
		bool ok = false;
		
		if (pd == 0 && pg >= 0 && pg < 100) { ok = true; }
		else if (pd != 0)
		{
			for(int i=1; i<=n && i<=100; i++)
			{
				int td = (int) (i * pd / 100);
				if (td * 100 == i * pd)
				{
					if (pd > 0 && pg > 0) { 
						if ((pd < 100 && pg < 100) || (pd == 100 && pg <= 100)) { ok = true; break;  }
					}
					
				}			
			}
		}
		
		if (ok)
			printf("Case #%d: Possible\n", tt);
		else
			printf("Case #%d: Broken\n", tt);
    }
    
    return 0;
}
