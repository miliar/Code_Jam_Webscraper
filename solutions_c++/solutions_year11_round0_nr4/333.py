#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;



int main()
{
	int t;   
	int n;
	
    cin >> t;
    
    for(int tt=1; tt<=t; tt++)
    {
		cin >> n;
		vector<int> a(n);
				
		int now = 0;
		int minus = 0;
		
		for(int i=0; i<n; i++) 
		{
			cin >> a[i];
			a[i] --;
		}
			
		while(true)
		{
			bool ok = false;
			for(int i=0; i<a.size(); i++)
			{
				if (a[i] == i)
				{
					ok = true;
					for(int j=0; j<n; j++) if (a[j] > a[i]) a[j]--;
					a.erase(a.begin()+i);
					break;
				}
			}
			
			if (!ok) break;
		}
		
		n = a.size();
			
		int st = 0;
		int mx = 0;
		double res = 0;
		
		for(int i=0; i<n; i++)
		{			
			if (a[i] > mx) mx = a[i];
			
			if (i == mx)
			{
				int nn = mx - st + 1;
				
				if (nn > 1)
				{
					res += nn;					
				}
				mx = i+1;
				st = i+1;
			}
		}
		printf("Case #%d: %.6lf\n", tt, res);
    }
    return 0;
}
