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

string s,A[5500];
int l,d,n; 

bool good(string&a, string&b) {
	int pos = 0;
	for (int i=0; i<l; i++)
		if (b[pos]=='(') {
			bool f=false;
			while (pos<b.length() && b[pos]!=')') {
				if(a[i]==b[pos]) f=true;
				pos++;
			} pos++;
			if (!f) return false;
		} else {
			if (pos>=b.length() || a[i]!=b[pos])
				return false;
			pos++;
		}
	return true;
}

int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	cin>>l>>d>>n;
	for (int i=0; i<d; i++)
		cin>>A[i];
	for(int o=1; o<=n; o++) {
		int res =0; cin>>s;
		for (int i=0; i<d; i++)
			if (good(A[i],s))
				res++;
		printf("Case #%d: %d\n",o,res);
	}
	return 0;
}