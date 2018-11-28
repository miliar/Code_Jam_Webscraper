#include <iostream>
#include <queue>
#include <vector>

using namespace std;

//square only
bool check(vector<deque<char> > &board, char val, int k) {
	
	for (int i=0;i<board.size();i++) {
		int num=0;
		for (int j=0;j<board.size();j++) {
			if (board[i][j]==val) num++;
			else num=0;
			if (num==k) return true;
		}	
	}
	//cout << "asdf" << endl;
	for (int i=0;i<board.size();i++) {
		int num=0;
		for (int j=0;j<board.size();j++) {
			if (board[j][i]==val) num++;
			else num=0;
			if (num==k) return true;
		}	
	}
	//cout << "a2323sdf" << endl;
	// diagonal...
	for (int i=0;i<board.size()*2-1;i++) {
		int ai,aj;
		if (i<board.size()) {
			ai=i;
			aj=0;
		}
		else {
			ai=board.size()-1;
			aj=i-(board.size()-1);
		}
		int num=0;
		for (;ai>=0 && aj<board.size();ai--,aj++) {
			if (board[ai][aj]==val) num++;
			else num=0;
			if (num==k) return true;
		}
	}
	//cout << "srr" << endl;
	for (int i=0;i<board.size()*2-1;i++) {
		int ai,aj;
		if (i<board.size()) {
			ai=i;
			aj=0;
		}
		else {
			ai=0;
			aj=i-(board.size()-1);
		}
		int num=0;
		for (;ai<board.size() && aj<board.size();ai++,aj++) {
			if (board[ai][aj]==val) num++;
			else num=0;
			if (num==k) return true;
		}
	}
	return false;
}

int main() {
	int T;
	
	cin >> T;
	//cout << "hi2" << endl;
	for (int i=1;i<=T;i++) {
		int N, K;
		cin >> N >> K;
		//cout << "hi3" << endl;
		vector<deque<char> > board;
		for (int j=0;j<N;j++) {
			board.push_back(deque<char>());
			//cout << "hi" << endl;
			char ch;
			cin.get(ch); // remove newline
			//cout << "ch" << ch;
			for (int k=0;k<N;k++) {
				char ch;
				cin.get(ch);
				if (ch=='.') board[j].push_back('.');
				else board[j].push_front(ch);
			}
		}
		//cout << "Got all" << endl;
		// now check if each has it
		bool red = check(board,'R',K);
		bool blue = check(board,'B',K);
		cout << "Case #" << i << ": ";
		if (red&&blue) cout << "Both";
		else if (red) cout << "Red";
		else if (blue) cout << "Blue";
		else cout << "Neither";
		cout << endl;
	}
	
	
	return 0;	
}
