#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#include <iostream>
#include <algorithm>
#include <map>
#include <string>
#include <vector>

using namespace std;

#define _ << ", " <<
#define db(x) 1//cout << #x " == " << x << endl
#define fr(a,b,c) for(int a = b ; a < c ; ++a )

char str[200], rule[200][10], del[200][10];
bool mark[256];
char res[200];
int c,d,n,t;

char regra(char a, char b) {
	fr(i,0,c) {
		if( a == rule[i][0] && b == rule[i][1] || a == rule[i][1] && b == rule[i][0] )
			return rule[i][2];
	}
	return 0;
}

bool opp() {
	memset(mark,0,sizeof mark);
	fr(i,0,t) mark[res[i]] = true;
	fr(i,0,d) {
		if( mark[del[i][0]] && mark[del[i][1]] ) return true;
	}
	return false;
}

bool read() {
	cin >> c;
	fr(i,0,c) {
		cin >> rule[i];
	}
	
	cin >> d;
	fr(i,0,d) {
		cin >> del[i];
	}
	
	cin >> n;
	cin >> str;
	
	memset(mark,0,sizeof mark);
	
	t = 0;
	fr(i,0,n) {
		char p = str[i];
		if( t ) {
			char x = regra(res[t-1],p);
			if( x ) res[t-1] = x, db(1);
			else {
				res[t++] = p, db(3);
				if( opp() ) t = 0, db(2);
			}
		} else res[t++] = p, db(0);
	}
	
	static int caso = 1;
	cout << "Case #" << caso++ << ": [";
	if( t ) cout << res[0];
	fr(i,1,t) cout << ", " << res[i];
	cout << "]" << endl;
	
	return true;	
}

int main() {
	int t = -1;
	cin >> t;
	while( t-- && read() );
	return 0;
}
