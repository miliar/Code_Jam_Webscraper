#include <cstdio>
#include <set>
#include <string>
#include <iostream>

using namespace std;

#define eatline() for(char c='\0'; c!='\n'; c = getchar())

int main(){
	int tcs;
	scanf("%d", &tcs);
	for(int tc=0; tc<tcs; ++tc){
		int n, m, erg=0;
		set<string> searched;
		string t;
		scanf("%d", &n);
		eatline();
		for(int i=0; i<n; ++i)
			eatline();
		scanf("%d", &m);
		eatline();
		for(int i=0; i<m; ++i){
			getline(cin, t);
			searched.insert(t);
			if(searched.size() == (size_t)n){
				searched.clear();
				searched.insert(t);
				++erg;
			}
		}
		printf("Case #%d: %d\n", tc+1, erg);
	}
}
