#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(v) (int(v.size()))

#include <iostream>
#include <string>

using namespace std;

typedef long long ll;

int col[10];
string s;

void solve() {
	int nm;
	memset(col,0,sizeof(col));
	for (int i=sz(s)-1; i>=0; i--) {
		for (char j=s[i]+1; j<='9'; j++) if (col[j-'0'] != 0) {
			for (int k=0; k<i; k++) putchar(s[k]);
			putchar(j);
			col[j-'0']--;col[s[i]-'0']++;
			for (char k='0'; k<='9'; k++)
				for (int k1=0; k1<col[k-'0']; k1++) putchar(k);
			return;
		}
		col[s[i]-'0']++;
	}
	for (int i=1; i<=9; i++) if (col[i] != 0) {
		putchar('0'+i);
		col[i]--;
		break;
	}
	col[0]++;
	for (int i=0; i<=9; i++) { 
		for (int j=0; j<col[i]; j++) putchar('0'+i);
	}
}

int main() {
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int nTest;
	scanf("%d\n",&nTest);
	for (int curTest = 1; curTest<=nTest; curTest++) {
		printf("Case #%d: ",curTest);
		getline(cin,s);memset(col,0,sizeof(col));
		solve(); putchar('\n');
		cerr << "test " << curTest << " passed\n";
	}
}
