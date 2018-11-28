#include <stdio.h>
#include <string.h>

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

char s[1111];

int main(void) {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	string res;
	int T; scanf("%d", &T);
	for(int tc=1;tc<=T;tc++) {
		res="";
		scanf("%s", s); int len = strlen(s);
		string a, b;

		a=b=s;
		sort(b.rbegin(), b.rend());	
		if(a==b) {
			sort(a.begin(), a.end());
			for(int i=0;i<a.length();i++) if(a[i]!='0') {
				res.push_back(a[i]);
				a[i]='0';
				break;
			}
			sort(a.begin(), a.end());
			res += a;
			printf("Case #%d: %s\n", tc, res.c_str());
			continue;
		}

		a=b="";
		for(int i=len-1;i>=0;i--) {
			a = s[i] + a;
			b = a;
			sort(b.rbegin(), b.rend());	
			if(a!=b) {
				for(int j=0;j<i;j++) res.push_back(s[j]);
				sort(a.begin(), a.end());
				for(int j=0;j<a.length();j++) if(a[j]>s[i]) {
					res.push_back(a[j]); a[j]='A';
					sort(a.begin(), a.end());
					a.resize(a.length()-1);
					res+=a;
					printf("Case #%d: %s\n", tc,  res.c_str());
					break;
				}
				break;
			}
		}
	}

	return 0;
}