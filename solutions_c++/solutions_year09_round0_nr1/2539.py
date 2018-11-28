#include <cstdio>
#include <string>
#include <iostream>
using namespace std;
int main(){
	int l,d,n;
	scanf("%d %d %d\n",&l,&d,&n);
	string s[d];
	string w;
	for (int i=0; i<d; ++i)
		getline(cin,s[i]);
	bool a[l][26];
	int u;
	int ans;
	bool b;
	for (int test = 1; test <= n; ++test){
		for (int i=0; i<l; ++i)
			for (int j=0; j<26; ++j)
				a[i][j]=0;
		ans=0;
		u=0;
		getline(cin,w);
		//cout << w << endl;
		for (int i=0; i<w.length();)
			if (w[i] == '('){
				while (w[i] != ')')
					a[u][w[i++]-'a']=1;
				++u;
				++i;
			}
			else
				a[u++][w[i++]-'a']=1;
		for (int i=0; i<d; ++i){
			b=1;
			for (int j=0; j<l; ++j)
				if (!a[j][s[i][j]-'a']){
					b=0;
					break;
				}
			if (b) ++ans;
		}
		printf("Case #%d: %d\n",test,ans);
		/*
		for (int i=0; i<l; ++i){
			for (int j=0; j<26; ++j)
				printf("%c ",a[i][j]?'#':'.');
			printf("\n");
		}
		*/
	}
	return 0;
}
