#include <iostream>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <cstring>
using namespace std;

char f[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int n;
string s;

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d\n", &n);
	for (int i = 1; i <= n; i++){
		getline(cin, s);
		for (int j = 0; j < s.size(); j++)
			if (s[j] != ' ')
				s[j] = f[s[j] - 'a'];
		printf("Case #%d: %s\n", i, s.c_str());
	}
}
