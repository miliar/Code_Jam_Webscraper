#include <iostream>
using namespace std;

#define MAX 50

string a[MAX];
int r[MAX], nTest, test, n;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	cin >> nTest;
	for (int test=1; test<=nTest; ++test) {
		cin >> n;
		for (int i=0; i<n; ++i)
			cin >> a[i];
			
		for (int i=0; i<n; ++i) {
			r[i]=-1;
			for (int j=0; j<n; ++j)
				if (a[i][j]=='1')
					r[i]=j;
		}
		
		int c=0;
		
		for (int i=0; i<n; ++i) {
			int j;
			for (j=i; j<n; ++j)
				if (r[j]<=i) {
					break;
				}
			while (j>i) {
				swap(r[j-1],r[j]);
				--j;
				++c;				
			}
		}			
		
		cout << "Case #" << test << ": " << c << endl;
	}
	
	return 0;
}
