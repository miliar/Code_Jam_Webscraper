#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>

using namespace std;

const int nmax = 45;

string a[nmax];
int b[nmax];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);	

	int ntest;
	cin >> ntest;
	for (int test = 1;test <= ntest; ++test){
		int n;
		cin >> n;
		memset(b,0,sizeof(b));
		for (int i = 0;i < n; ++i){
			cin >> a[i];
			for (int j = 0;j < n; ++j)
				if (a[i][j] == '1') b[i] = j;
		}

		int sum = 0;
		for (int i = 0;i < n; ++i){
			if (b[i] > i){
				int t = -1;
				for (int j = i + 1;j < n; ++j)
					if (b[j] <= i){
						t = j;
						break;
					}
				sum += t - i;
				int tt = b[t];
				for (int j = t-1;j >= i; --j) b[j+1] = b[j];
				b[i] = tt;
			}
		}
		printf("Case #%i: %i\n",test,sum);
	}
	
	return 0;
}