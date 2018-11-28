#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<cstring>
#include<cstdlib>
#include<cassert>

using namespace std;

typedef long long ll;
typedef pair<int,int> pint;

#define mp make_pair
#define pb push_back

#define repp(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define rep(i,n) repp(i,0,(n)-1)

char m[10][10];

bool chk(char c){
	rep(i,4){
		rep(j,4){
			if(m[i][j] != c && m[i][j] != 'T') goto tugi;
		}
		return true;
tugi:;
	}
	rep(i,4){
		rep(j,4){
			if(m[j][i] != c && m[j][i] != 'T') goto tugi2;
		}
		return true;
tugi2:;
	}
	rep(i,4){
		if(m[i][i] != c && m[i][i] != 'T') goto tugi3;
	}
	return true;
tugi3:;
	rep(i,4){
		if(m[i][3-i] != c && m[i][3-i] != 'T') goto tugi4;
	}
	return true;
tugi4:;
	return false;
}
bool finish(){
	rep(i,4) rep(j,4) if(m[i][j] == '.') return false;
	return true;
}
void output(int cas, char *s){
	printf("Case #%d: %s\n", cas+1, s);
}

int main(){
	int casenum; cin >> casenum;
	rep(casee, casenum){
		rep(i,4) scanf("%s", m[i]);
//rep(i,4) cout << m[i] << endl;
		bool xwin = chk('X');
		bool owin = chk('O');
		if(xwin && owin) assert(0);
		if(xwin) output(casee, "X won");
		else if(owin) output(casee, "O won");
		else if(finish()) output(casee, "Draw");
		else output(casee, "Game has not completed");
	}
	return 0;
}

