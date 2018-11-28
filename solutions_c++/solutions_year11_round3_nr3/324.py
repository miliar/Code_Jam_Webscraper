#include <iostream>

using namespace std;

int main()
{
	int t;
	int n, l, h;
	int a[1000];
    cin >> t;
    
    
    for(int tt=1; tt<=t; tt++)
    {
		cin >> n >> l >> h;
		for(int j=0; j<n; j++) cin >> a[j];
		
		
		int res = -1;
		for(int i=l; i<=h; i++)
		{
			bool ok = true;
			for(int j=0; j<n; j++) if (i % a[j] != 0 && a[j] % i != 0) { ok = false; break; }
			
			if (ok) { res = i; break; }
		}
		
		
		if (res == -1)
		{
			printf("Case #%d: NO\n", tt);
		}
		else
		{
			printf("Case #%d: %d\n", tt, res);
		}
    }
    
    return 0;
}
