#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>

using namespace std;

const int nmax = 105;
int a[nmax];


int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int nn;
	cin >> nn;
	for (int test = 1;test <= nn; ++test){
		int n,l,h;

		cin >> n >> l >> h;

		for (int i = 0;i < n; ++i)
		{
			cin >> a[i];
		}

		
		int ans = -1;

		for (int i = l;i <= h; ++i)
		{
			bool ok = true;
			for (int j = 0;j < n; ++j)
				if (!(i % a[j] == 0 || a[j] % i == 0))
				{
					ok = false;
					break;
				}
			if (ok)
			{
				ans = i;
				break;
			}		
		}		
		
		printf("Case #%i: ",test);		
		if (ans > -1) cout << ans << endl;
		else cout << "NO" << endl;
	}
	
	return 0;
}