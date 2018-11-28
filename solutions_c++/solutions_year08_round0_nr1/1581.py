#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string mygetline(void) {
	char c;
	string s;
	while(scanf("%c", &c) != EOF) {
		if(c == '\n') break;
		s += c;
	}
	return s;
}

string a[101];
int mark[101];
int n, q;

int main(void)
{
	int casos;
	string s;
	int count, res;
	scanf("%d", &casos);
	getchar();
	
	for(int caso = 1; caso <= casos; caso++) {
		scanf("%d", &n);
		getchar();
		for(int i=0; i<n; i++) a[i] = mygetline();
		scanf("%d", &q);
		getchar();
		
		count = 0;
		res = 0;
		memset(mark, 0, sizeof(mark));
		for(int i=0; i<q; i++) {
			s = mygetline();
			for(int j=0; j<n; j++) {
				if(s == a[j] && !mark[j]) mark[j] = 1, count++;
				if(count == n) {
					res++;
					count = 1;
					memset(mark, 0, sizeof(mark));
					mark[j] = 1;
				}
			}
		}
		
		printf("Case #%d: %d\n", caso, res);
		
	}
	
	return 0;
}
