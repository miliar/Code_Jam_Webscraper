#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>

using namespace std;

const int nmax = 1005;

int a[nmax];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int nn;
	cin >> nn;
	for (int test = 1;test <= nn; ++test){

		int n;

		cin >> n;

		for (int i = 0;i < n; ++i) cin >> a[i];

		int xor = 0;
		for (int i = 0;i < n; ++i) xor = xor ^ a[i];

		if (xor != 0)
		{
			printf("Case #%i: NO\n",test);
		}
		else
		{	
			int sum = 0;
			sort(a,a+n);
			for (int i = 1;i < n; ++i) sum += a[i];
			printf("Case #%i: %i\n",test,sum);		
		}
	}
	
	return 0;
}