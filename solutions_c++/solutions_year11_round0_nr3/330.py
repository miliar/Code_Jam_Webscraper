#include <iostream>
#include <algorithm>

using namespace std;

int a[1001];

int main()
{
	int t;   
	int n;
    cin >> t;
    
    for(int tt=1; tt<=t; tt++)
    {
		cin >> n;
		int check = 0;
		for(int i=0; i<n; i++) { cin >> a[i]; check ^= a[i]; }
		
		if (check != 0)
		{
			printf("Case #%d: NO\n", tt);
		}
		else
		{
			sort(a, a+n);
			int res = 0;
			for(int i=1; i<n; i++) res+= a[i];
			printf("Case #%d: %d\n", tt, res);
		}
    }
    return 0;
}
