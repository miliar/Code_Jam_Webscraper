#include <iostream>
#include <string>
#include <vector>
using namespace std;
#define fu(i,m,n) for(int i=m; i<n; i++)
#define fd(i,m,n) for(int i=n-1; i>=m; i--)

int N,K;

void scan(vector<string>& board, int r, int c, int dr, int dc, bool& R, bool& B) {
	int cnt=0;
	char x=0;
	while(r<N && c<N) {
		if(board[r][c]==x) cnt++;
		else {
			x=board[r][c];
			cnt=1;
		}
		if(cnt>=K) {
			if(x=='R') R=true;
			else if(x=='B') B=true;
		}
		r+=dr;
		c+=dc;
	}
}

int main(void) {
	int T;
	cin >> T;
	fu(tc,1,T+1) {
		cin >> N >> K;
		vector<string> board(N);
		fu(i,0,N) cin >> board[i];
		fu(i,0,N) {
			for(int j=N-1, k=N-2; j>=0&&k>=0;) {
				if(board[i][k]=='.') k--;
				else if(board[i][j]=='.') {
					board[i][j]=board[i][k];
					board[i][k]='.';
					j--, k--;
				} else {
					j--;
					if(j==k) k--;
				}
			}
		}
		//fu(i,0,N) cout << board[i] << endl;
		bool R=false,B=false;
		fu(i,0,N) scan(board,i,0,0,1,R,B);
		fu(i,0,N) scan(board,0,i,1,0,R,B);
		fu(i,0,N) scan(board,i,0,1,1,R,B);
		fu(i,1,N) scan(board,0,i,1,1,R,B);
		reverse(board.begin(), board.end());
		fu(i,0,N) scan(board,i,0,1,1,R,B);
		fu(i,1,N) scan(board,0,i,1,1,R,B);
		cout << "Case #" << tc << ": ";
		if(R) {
			if(B) cout << "Both" << endl;
			else cout << "Red" << endl;
		} else {
			if(B) cout << "Blue" << endl;
			else cout << "Neither" << endl;
		}
	}
}
