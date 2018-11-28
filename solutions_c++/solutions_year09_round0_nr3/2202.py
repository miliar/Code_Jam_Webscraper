#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

string A = string("welcome to code jam"),s;
int f[500];
int main() {
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int n; cin>>n;
	getline(cin,s);
	int l = A.length()-1;
	for (int o=1; o<=n; o++) {
		getline(cin,s);
		memset(f,0,sizeof f);
		for (int i=0; i<s.length(); i++)
			if (s[i]==A[l]) f[i]=1;
		for (int j=l-1; j>=0; j--) {
			int sum = 0;
			for (int i=s.length(); i>=0; i--) {
				sum = (sum+f[i])%10000;
				if (s[i]==A[j]) f[i] = sum;
				else f[i] = 0;
			}
		}
		int res = 0;
		for (int i=0; i<s.length(); i++)
			res = (res+f[i])%10000;
		printf("Case #%d: %04d\n",o,res);
	}
	return 0;
}