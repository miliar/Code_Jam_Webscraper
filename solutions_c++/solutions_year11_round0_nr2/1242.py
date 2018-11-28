#include<stdio.h>
#include<cstdlib>
#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<cstring>

using namespace std;

#define REP(I,N) for(int I=0 ; I<N ; I++)
#define SZ(A) ((int)(A).size())
#define PB push_back
#define F first
#define S second

typedef pair<int,int> II;

char op[255];
char trans[255][255];

int main() {

	int T;
	cin >> T;
	for(int t=0 ; t<T ; t++) {

		memset(op, 0, sizeof(op));
		memset(trans, 0, sizeof(trans));

		int c, d, n;
		string s;
		cin >> c;
		REP(i, c) {
			cin >> s;
			trans[s[0]][s[1]] = s[2];
			trans[s[1]][s[0]] = s[2];
		}
		cin >> d;
		REP(i, d) {
			cin >> s;
			op[s[0]] = s[1];
			op[s[1]] = s[0];
		}

		string list = "";
		cin >> n >> s;
		for(int i=0 ; i<n ; i++) {
			list += s[i];
			int last = SZ(list) - 1;

			if(SZ(list) > 1 && trans[ list[last] ][ list[last-1] ] != 0) {
				char ch = trans[ list[last] ][ list[last-1] ];
				list.erase(list.begin() + SZ(list) -1);
				list[SZ(list)-1] = ch;
			}

			char opuesto = op[list[SZ(list)-1]];
			for(int i=0 ; i<SZ(list)-1 ; i++) if(list[i] == opuesto) {
				list = "";
				break;
			}
		}

		printf("Case #%d: [", t+1);
		for(int i=0 ; i<SZ(list) ; i++) {
			printf("%c", list[i]);
			if(i!=SZ(list)-1) printf(", ");
		}
		printf("]\n");
	}

	return 0;	
}
