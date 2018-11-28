#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>

using namespace std;

const int nmax = 1000006;

int a[nmax];
long long d[nmax];



int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int nn;
	cin >> nn;
	for (int test = 1;test <= nn; ++test){
		
		int l,n,c;
		long long t;

		cin >> l >> t >> n >> c;
		for (int i = 0;i < c; ++i) cin >> a[i];

		for (int k = 0;; ++k)
		{
			if (k * c >= n) break;

			for (int i = 0;i < c; ++i) 
			{
				if (k * c + i >= n) break;

				d[ k * c + i] = a[i];
			}
		}

		long long sum = 0;
		int pos = -1;
		long long tt = t/2;

		for (int i = 0;i < n; ++i)
		{
			sum += d[i];
			if (sum > tt)
			{
				pos = i;
				break;
			}
		}
		long long ans = 0;

		if (pos == -1)
		{
			ans = sum * 2;
		}
		else
		{
			d[pos] = (sum-tt);

			sort(d+pos,d+n);

			ans = t;

			int ma = n-l;
			if (ma < pos) ma = pos;

			for (int i = pos;i < ma; ++i) ans += d[i] * 2;			

			for (int i = ma;i < n; ++i) ans += d[i];
		}
		
		printf("Case #%i: ",test);		
		cout << ans << endl;
	}
	
	return 0;
}