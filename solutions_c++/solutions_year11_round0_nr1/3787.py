#include<iostream>
#include<stdio.h>
#include<string>
#include<vector>
#include<cmath>
#include<algorithm>
using namespace std;

vector< pair<char,int> > input;

int findNext(char c, int ind) {
	int i;
	for(i=ind;i<input.size();i++)
		if(input[i].first == c) break;
	return i;
}

void move(int target, int &pos, int moves) {
	int dir = target>pos?1:-1;
	moves = min(moves,abs(target-pos));
	pos += dir*moves;
}

int main() {
	int T, N;
	scanf("%d", &T);
	int k = 0, b;
	char c;
	while(T--) {
		input.clear();
		scanf("%d", &N);
		while(N--) {
			scanf(" %c %d", &c, &b);
			input.push_back(make_pair(c,b));
		}
		int opos = 1, bpos = 1;
		int oind = findNext('O',0), bind = findNext('B',0);
		int sum = 0;
		int oinc, binc;
		int moves;
		while(oind<input.size() || bind<input.size()) {
			if(oind<bind) moves=abs(input[oind].second-opos), binc=1;
			else moves=abs(input[bind].second-bpos), oinc=1;
			sum += moves+1;
			move(input[oind].second,opos,moves+oinc);
			move(input[bind].second,bpos,moves+binc);
			if(oind<bind) oind=findNext('O',oind+1);
			else bind=findNext('B',bind+1);
		}
		printf("Case #%d: %d\n", ++k, sum);
	}
}
