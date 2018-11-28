#include <cstdio>
#include <iostream>
#include <memory.h>
#include <vector>
using namespace std;

const int MAX_N = 128;

int n;
char s[MAX_N];

char comb[256][256];
char opp[256][256];

vector<char> ans;

void input()
{
	int i, c, d;

	memset(comb, 0, sizeof(comb));
	memset(opp, 0, sizeof(opp));
	
	scanf("%d", &c);
	for(i=0; i<c; i++) {
		scanf("%s", s);
		comb[ s[0] ][ s[1] ] = s[2];
		comb[ s[1] ][ s[0] ] = s[2];
	}

	scanf("%d", &c);
	for(i=0; i<c; i++) {
		scanf("%s", s);
		opp[ s[0] ][ s[1] ] = 1;
		opp[ s[1] ][ s[0] ] = 1;
	}

	scanf("%d", &n);
	scanf("%s", s);
}

void solve()
{
	char *c, newc;
	vector<char>::iterator it;
	
	ans.clear();
	for(c=s; *c; c++) {
		if(!ans.empty()) {
			if(newc = comb[ans.back()][*c]) {
				ans.back() = newc;
				continue;
			}
		}

		int can_add = 1;
		
		for(it=ans.begin(); it!=ans.end(); it++) {
			if(opp[*it][*c]) {
				ans.clear();
				can_add = 0;
				break;
			}
		}

		if (can_add)
			ans.push_back(*c);
	}
}

void output(int t)
{
	printf("Case #%d: ", t);
	printf("[");
	
	vector<char>::iterator it;
	for(it=ans.begin(); it!=ans.end(); it++) {
		if (it!=ans.begin())
			printf(", ");
		printf("%c", *it);
	}

	printf("]\n");
}

int main()
{
	int i, t;
	scanf("%d", &t);

	for(i=1; i<=t; i++) {
		input();
		solve();
		output(i);
	}
	
	return 0;
}