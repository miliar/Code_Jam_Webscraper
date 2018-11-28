#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	int testow;
	scanf("%d",&testow);
	for(int z=1;z<=testow;++z) {
		printf("Case #%d: ",z);
		char s[33];
		scanf("%s",s);
		vector<char> v;
		v.push_back('0');
		for(int i=0;s[i];++i)
			v.push_back(s[i]);
		next_permutation(v.begin(),v.end());
		int od=0;
		while(v[od]=='0')
			++od;
		for(int i=od,n=v.size();i<n;++i)
			putchar(v[i]);
		puts("");
	}
}
