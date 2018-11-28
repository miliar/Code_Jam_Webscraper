// Paste me into the FileEdit configuration dialog

#include <cmath>
#include <ctime>
#include <iostream>
#include <string>
#include <set>
#include <vector>
using namespace std;
 long long  a[1000001];
 long long b[1000001];
 long long total[1000001];
int main(int argc, char *argv[]) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt;
	cin >> tt;
	for (int t = 1; t<=tt; ++t)
	{
		int n, r, c;
		 long long L, T; 
		cin >> L >> T >> n >> c;
		for (int i = 0; i < c; ++i)
			cin >> a[i];
		for (int i = 0; i < n; ++i)
			b[i] = a[i%c] * 2;
		total[0] = 0;
		for (int k = 0; k < n; ++k)
			total[k+1]=total[k]+b[k];
		
		 long long cur = total[n];
		 long long ans = total[n];
		
		multiset< long long> Q;
			 long long all = 0, good = 0;
			if (L>0) {
				for (int i=n-1; i>=0; i--) {
					 long long t = max(( long long)0, T-total[i]);
					 long long time = total[i];
					t = min(t, b[i]);
					time += t;
					time += (b[i]-t)/2;
					time += (all-good)+good/2;
					Q.insert(b[i]);
					good += b[i];
					all += b[i];
					if (!Q.empty() && Q.size()>=L) {
						 long long q = *Q.begin();
						Q.erase(Q.begin());
						good -= q;
					}
					if (total[i]+b[i]>=T)
						ans = min(ans, time);
				}
			}						
		

		
		cout << "Case #" << t << ": ";
		cout << ans;
		cout << endl;
		
	}
	fclose(stdout);
}
