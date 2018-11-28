#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <utility>
#include <set>
#include <algorithm>
#include <list>
#include <queue>
//#include <fstream>

using namespace std;

int getln(string &s)
{
	int res=0;
	for(int i = 0; i < s.length(); i++)
		if( s[i] == '1' ) res = i;
	return res;
}

bool good( vector<string> &board )
{
	for(int i = 0; i < board.size(); i++) {
		if( getln( board[i] ) > i ) return false;
	}
	return true;
}

void solve()
{
	int res;
	int N;
	cin >> N;
	vector<string> board(N,string());
	vector<int> ln(N);
	for(int i = 0; i < N; i++) {
		cin >> board[i];
		ln[i] = getln( board[i] );
	}

	if( N == 1 ){
		cout << 0 ;
		return;
	}



	set < vector <string> > status;

	queue< vector <string> > que;
	queue< int > num;

	status.insert( board );
	que.push( board );
	num.push( 0 );
	while(true) {
		vector <string> cur = que.front();
		int curnum = num.front();

		que.pop();
		num.pop();

		//cout << curnum << " " << que.size() << " " << status.size() << endl;

		if( good( cur ) ) {
			res = curnum;
			break;
		}

		//cout << "#" << endl;

		for(int i = 0; i < N-1; i++) {
			swap(cur[i], cur[i+1]);
			if( status.count( cur ) == 0 ) {
				status.insert( cur );
				que.push( cur );
				num.push( curnum + 1 );
			}
			swap(cur[i], cur[i+1]);
		}
	}
	cout << res;
}

int main()
{
    int N;
    string Buffer;
    getline(cin, Buffer);
    N = atoi(Buffer.c_str());
    for(int i = 0; i < N; i++) {
        cout << "Case #" << i+1 << ": ";
        solve();
        cout << endl;
    }
    return 0;
}
