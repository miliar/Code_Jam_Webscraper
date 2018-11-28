#include <cstdio>
#include <cstdlib>
#include <cmath>

#include <iostream>
using namespace std;
typedef long long int64;

#define for0(i,n) for(int i=0; i<n; i++)

int main()
{
//	freopen("test.in","r",stdin); freopen("test.out","w",stdout);
	freopen("C-small-attempt0.in","r",stdin); freopen("C-small-attempt0.out","w",stdout);
//	freopen("C-small-attempt1.in","r",stdin); freopen("C-small-attempt1.out","w",stdout);
//	freopen("C-large.in","r",stdin); freopen("C-large.out","w",stdout);

//	freopen("test.in","r",stdin); freopen("test.out","w",stdout);
//	freopen("C-small-practice.in","r",stdin); freopen("C-small-practice.out","w",stdout);
//	freopen("C-large-practice.in","r",stdin); freopen("C-large-practice.out","w",stdout);

	int totalCases;
	cin >> totalCases;

	for (int caseNo = 1; caseNo <= totalCases; caseNo++) {
		
		int64 n, l, h;
		cin >> n >> l >> h;
		int64 c[10000];
		for0(i,n)
			cin >> c[i];

		bool possible = false;
		int64 ret = 0;
		for (int i=l; i<=h; i++) {
			int j;
			for (j=0; j<n; j++) {
				if ( (i>c[j] && i%c[j]!=0) || (c[j]>i && c[j]%i!=0) )
					break;
			}
			if (j==n) {
				possible = true;
				ret = i;
				break;
			}
		}			

		cout << "Case #" << caseNo << ": ";
		if (!possible)
			cout << "NO";
		else
			cout << ret;
		cout << endl;
	}

	return 0;
}
