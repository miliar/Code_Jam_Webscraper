#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cstring>
#include <map>
#include <queue>
#include <string>
#include <sstream>

using namespace std;

#define FOR(i,a,b) for (int (i)=(a);(i)<(b);++(i))
#define FORE(i,a,b) for (int (i)=(a);(i)<=(b);++(i))
#define FOREACH(it,v) for (typeof((v).begin()) it=(v).begin();(it)!=(v).end();++(it))
#define ALL(v) v.begin(),v.end()
#define MSET(v,x) memset((v),(x),sizeof((v)))

typedef double D;
typedef pair<int,int> PII;
typedef pair<double,double> PDD;
typedef set<int> SI;
typedef vector<int> VI;
typedef vector<double> VD;
typedef map<int,int> MII;
typedef long long ll;
typedef vector<PII> VP;
typedef queue<PII> QP;

int M,N;
int board1[512][512];
int board2[512][512];

int hex(char c) {
	if (c>='0'&&c<='9') return c-'0';
	return c-'A'+10;
}

int min3(int a, int b, int c) {
	return min(min(a,b),c);
}

void update(int board[512][512], int i, int j) {
	QP q;
	q.push(PII(i,j));
	while (!q.empty()) {
		i=q.front().first;
		j=q.front().second;
		q.pop();
		if (i<1||i>M||j<1||j>N) continue;
		if (board[i][j]==0) continue; 
		int me=min3(board[i-1][j],board[i-1][j-1],board[i][j-1])+1;
		if (board[i][j]!=me) {
			board[i][j]=me;
			q.push(PII(i+1,j));
			q.push(PII(i,j+1));
			q.push(PII(i+1,j+1));
		}
	}
}

void kill(int board[512][512], int i, int j, int k) {
	FORE (ii,i-k+1,i) {
		FORE (jj,j-k+1,j) {
			board[ii][jj]=0;
		}
	}
	FORE (ii,i-k+1,i) {
		update(board,ii,j+1);
	}
	FORE (jj,j-k+1,j) {
		update(board,i+1,jj);
	}
	update(board,i+1,j+1);
}

void print() {
	FOR (i,0,M) {
		FOR (j,0,N) {
			cerr << board1[i][j];
		}
		cerr << endl;
	}
	cerr << endl;
	FOR (i,0,M) {
		FOR (j,0,N) {
			cerr << board2[i][j];
		}
		cerr << endl;
	}
	cerr << endl;
}

int main () {
	int T;
	cin >> T;
	for (int t=1;t<=T;++t) {
		cin >> M >> N;
		FOR (i,0,M) {
			string s;
			cin >> s;
			FOR (j,0,s.length()) {
				int c=hex(s[j]);
				FOR (k,0,4) {
					bool bit=c&(1<<(3-k));
//					cerr << bit;
					board1[i][j*4+k]=(((i&1)==(k&1))==bit)?1:0;
					board2[i][j*4+k]=(((i&1)==(k&1))==bit)?0:1;
				}
			}
//			cerr << endl;
		}
//		cerr << endl;
		FOR (i,0,M) {
			FOR (j,0,N) {
				update(board1,i,j);
				update(board2,i,j);
			}
		}
//		print();
		VP v;
		for (int k=min(M,N);k>=1;--k) {
			int count=0;
			FOR (i,k-1,M) {
				FOR (j,k-1,N) {
					if (board1[i][j]==k || board2[i][j]==k) {
						kill(board1,i,j,k);
						kill(board2,i,j,k);
						count++;
//						if (k==6) print();
					}
				}
			}
			if (count) v.push_back(PII(k,count));
		}
		cout << "Case #"<<t<<": "<< v.size() << endl;
		FOR (i,0,v.size()) cout << v[i].first << " " << v[i].second << endl;
	}
}
