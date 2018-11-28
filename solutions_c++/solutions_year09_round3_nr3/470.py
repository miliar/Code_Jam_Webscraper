#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	freopen("C.in","rt",stdin);
	freopen("C.out","wt",stdout);
	
	int t, ti;
	cin >> t;
	
	for (ti = 1; ti < t + 1; ti++)
	{
		int r[5], p, q;
		cin >> p >> q;
		for (int i = 0; i < q; i++) cin >> r[i];

		int ans = 1000000000;

		if (q == 1) ans = p - 1;
		
		sort(r,r + q);
		do
		{
			int mans = 0;
			for (int i = 0; i < q; i++)
			{
				int ll = 0, rr = p + 1; 
				for (int j = 0; j < i; j++)
				{
					if (r[j] < r[i] && ll < r[j]) ll = r[j];
					if (r[j] > r[i] && rr > r[j]) rr = r[j];
				}
				mans += rr - ll - 2;
			}
			
			ans = min(mans,ans);
		} while (next_permutation(r,r + q));
		
		cout << "Case #" << ti <<": " << ans << endl;
//		cout << p << " " << q << endl; 	for (int i = 0; i < q; i++) cout << r[i] << " "; cout << endl;
	}
	fclose(stdin); fclose(stdout);
	return 0;
}