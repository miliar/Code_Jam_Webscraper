#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <math.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> ii;
typedef vector<ii> vii;
#define sz(a) int((a).size())
#define all(c) (c).begin(),(c).end()
#define loop(i,n) for(int i=0; i<(n); i++)
#define tr(it,c) for(it=(c).begin(); it!=(c).end(); it++)
#define tr2(it1,c,it2,d) for(it1=(c).begin(),it2=(d).begin(); it1!=(c).end(); it1++,it2++)

bool isWon(const vs &board, char letter)
{
	bool win = false;
	int count;
	loop(i, 4) {
		count = 0;
		loop(j, 4) {
			if(board[i][j] == letter || board[i][j] == 'T')
				count ++;
		}
		if (count == 4)
			win = true;
	}

	loop(j, 4) {
		count = 0;
		loop(i, 4) {
			if(board[i][j] == letter || board[i][j] == 'T')
				count ++;
		}
		if (count == 4)
			win = true;
	}

	loop(k, 2) {
		count = 0;
		loop(i, 4) {
			char c = board[i][3*(1-k) + (2*k-1)*i];
			if(c == letter || c == 'T')
				count ++;
		}
		if (count == 4)
			win = true;
	}
	return win;
}

bool isFinish(const vs &board)
{
	bool finish = true;
	loop(i, 4) loop(j, 4)
		if(board[i][j] == '.')
			finish = false;
	return finish;
}

string solve(const vs &board)
{
	bool xwon = isWon(board, 'X');
	bool owon = isWon(board, 'O');
	bool finish = isFinish(board);
	string answer;
	if (xwon)
		answer = "X won";
	else if(owon)
		answer = "O won";
	else if(finish)
		answer = "Draw";
	else
		answer = "Game has not completed";
	return answer;
}

void preprocess(){}

void readinput(vs &board)
{
	loop(i, 4)
		cin>>board[i];
}

vs getoutput()
{
	vs board(4);
	readinput(board);
	string answer = solve(board);
	return vs(1, answer);
}

void main()
{
//	freopen("in.txt", "r", stdin); freopen("out.txt", "w", stdout);
//	freopen("test\\A-small-attempt0.in", "r", stdin);freopen("test\\A-small-attempt0.out", "w", stdout);
	freopen("test\\A-large.in", "r", stdin);freopen("test\\A-large.out", "w", stdout);
	int testcase;
	cin>>testcase;
	preprocess();
	for(int i=1; i<=testcase; i++)
	{
		cout<<"Case #"<<i<<": ";
		vs answer = getoutput();
		loop(j, sz(answer))
			cout<<answer[j]<<endl;
	}
	fclose(stdin);
	fclose(stdout);
}