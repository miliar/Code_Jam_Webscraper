#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;
long long a[1001],g[1001],c[1001];
bool b[1001];
int main () {
	int t;
	freopen( "input.txt","r",stdin);
	freopen( "output.txt","w",stdout);
	cin >> t;
	for (int jjj = 0 ; jjj < t; jjj++){
		 long long r, k, n, ans = 0;
		 cin >> k >> r >> n;
		 int lasti = 0;
		 int lastj = -1;
		 for (int i = 0; i < n; i++)
			 a[i] = b[i] = c[i] = g[i] = 0;
		 for (int i = 0; i < n; i++)
			 cin >> g[i];
		 long long fsum = 0;
		 for (int i = 0; i < k; i++) { 
			 long long sum = 0;
				 for (int j = lasti, P = 0; r - sum >= g[j] && P != n; j = (j+1)%n, P++){
					 sum += g[j];
					 lasti = j;
				 }
				 fsum += sum;
				 ans += sum;
			if (b[lasti])
			{
				long long A =(k - i - 1) / (i - c[lasti]);
				long long B =(k - i - 1) % (i - c[lasti]);
				ans += (fsum - a[lasti]) * A;
				for (int l = 0; l < B; l++)	{
					lasti++;
					sum = 0;
					for (int u = lasti, P = 0 ; r - sum >= g[u] && P != n; u = (u + 1) %n, P++){
						sum += g[u];
						lasti = u;
						ans += g[u];
					}

				}
				break;
			}
			 b[lasti] = true;
			 a[lasti] = fsum;
			 c[lasti] = i;
			 lasti = (lasti +1) % n;
		 }

		 cout << "Case #" << jjj+1 << ": " << ans << "\n" ;
	}
	 return 0;
 };