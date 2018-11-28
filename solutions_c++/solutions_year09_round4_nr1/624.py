#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int a[41];
char c;
int test, n;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	cin >> test;
	for (int tt=1; tt<=test; tt++) {
		printf("Case #%i: ",tt);
		cin >> n;
		for (int i=1; i<=n; i++) {
			int k=0;
			for (int j=1; j<=n; j++) {
				cin >> c;
				if (c=='1') k=j;
			}
			a[i]=k;
		}

		int sum=0;
		for (int i=1; i<=n; i++)
			if (a[i]>i) {
				int t, l;
				for (int j=i+1; j<=n; j++)
					if (a[j]<=i) { t=j; break; }
				l=a[t];
				for (int j=t; j>i; j--)
					a[j]=a[j-1];
				a[i]=l;
				sum+=t-i;
			}
		cout << sum << endl;
	}

	return 0;
}
