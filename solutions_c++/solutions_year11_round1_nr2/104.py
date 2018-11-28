#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>

#define _ << ", " <<
#define db(x) 1//cout << #x " == " << x << endl
#define fr(a,b,c) for( int a = b ; a < c ; ++a )

typedef long long ll;
using namespace std;
typedef pair<int,int> pii;

int n,m;
string pal[20000];
int letra[20000][300];
//bool ok[20000];
int passos[20000];
char ordem[50];

char l;
bool comp(const int & a, const int & b) {
	return letra[a][l] < letra[b][l];
}

void go(int k, vector<int> conj, int niv) {
	char at = ordem[k];
	if( conj.size() == 1 ) {
		passos[ conj[0] ] = niv;
		return;
	}
	fr(i,0,conj.size()) if( letra[conj[i]][at] ) goto pula;
	///db( conj[0] _ pal[conj[0]] _ conj.size() _ k _ at );
	go(k+1, conj, niv);
	return;
	pula:;
	l = at;
	sort(conj.begin(), conj.end(), comp);
	vector<int> novo;
	novo.push_back(conj[0]);
	fr(i,1,conj.size()) {
		if( letra[conj[i]][at] == letra[novo[0]][at] ) novo.push_back(conj[i]);
		else {
			//db( letra[novo[0]][at] _ novo.size());
			go(k+1, novo, niv+!letra[novo[0]][at]);
			novo.clear();
			novo.push_back(conj[i]);
		}
	}
	go(k+1, novo, niv+!letra[novo[0]][at]);
}

bool read() {
	cin >> n >> m;
	fr(i,0,n) cin >> pal[i];
	memset(letra, 0, sizeof letra);
	fr(i,0,n) for( int j = 0 ; pal[i][j] ; ++j ) letra[i][ pal[i][j] ] |= 1<<j;
	vector<int> comtam[15];
	fr(i,0,n) comtam[ pal[i].size() ].push_back(i);
	static int caso = 1;
	cout << "Case #" << caso++ << ":";
	while( m-- ) {
		cin >> ordem;
		//memset(passos,false,sizeof passos);
		fr(i,0,15) if( comtam[i].size() ) go(0,comtam[i],0);
		int meo = 0;
		//fr(i,0,n) db( pal[i] _ passos[i] );
		fr(i,0,n) if( passos[meo] < passos[i] ) meo = i;
		cout << " " << pal[meo];
	}
	cout << endl;
	return true;
}

int main() {
	int t = -1;
	cin >> t;
	while( t-- && read() );
	return 0;
}
