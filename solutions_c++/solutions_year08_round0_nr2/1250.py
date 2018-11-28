#include<iostream>
#include<map>
#include<string>

using namespace std;

int L[110][2];
int R[110][2];
int wait, Na, Nb;



inline int f(const string& s) {
	int h = (s[0] - '0') * 10 + (s[1]-'0');
	int m = (s[3] - '0') * 10 + (s[4]-'0');
	return h * 60 + m;
}

char mat[110][110];
int match[110];
char vis[110];


bool dfs(int index) {	
	for (int i=0; i<Nb; ++i) if(mat[index][i] && vis[i]==0 ){
		vis[i] = 1;
		if (match[i] == -1 || dfs(match[i]) ) {
			match[i] = index;
			return true;
		}
	}
	return false;
}

void solve(int id) {
	memset(mat, 0, sizeof mat);
	for (int i=0; i<Na; ++i) for (int j=0; j<Nb; ++j) {
		if (L[i][1] + wait <= R[j][0] )
			mat[i][j] = 1;
	}
	int cb = 0;
	memset(match, -1, sizeof match);
	for (int i=0; i<Na; ++i) {
		memset(vis, 0, sizeof vis);
		if (dfs(i) ) {
			++cb;
		}
	}


	memset(mat, 0, sizeof mat);
	for (int i=0; i<Na; ++i) for (int j=0; j<Nb; ++j) {
		if (R[j][1] + wait <= L[i][0])
			mat[i][j] = 1;
	}
	int ca = 0;
	memset(match, -1, sizeof match);
	for (int i=0; i<Na; ++i) {
		memset(vis, 0, sizeof vis);
		if (dfs(i) ) {
			++ca;
		}
	}

	cout << "Case #" << id << ": " << Na - ca << " " << Nb - cb << endl;
	
}

int main() {
	freopen("d:/input", "r", stdin);
	freopen("d:/output", "w", stdout);
	int T;
	cin >> T;
	for (int id=1; id<=T; ++id) {
		cin >> wait;
		cin >> Na >> Nb;
		string s1, s2;
		for (int i=0; i<Na; ++i) {
			cin >> s1 >> s2;
			L[i][0] = f(s1);
			L[i][1] = f(s2);
		}
		for (int i=0; i<Nb; ++i) {
			cin >> s1 >> s2;
			R[i][0] = f(s1);
			R[i][1] = f(s2);
		}
		solve(id);
	}

	return 0;
}