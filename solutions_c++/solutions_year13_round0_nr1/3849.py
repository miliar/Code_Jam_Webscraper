#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

string check(vector<string> board);
string helper(char a, char b, char c, char d);

int main()
{
	ifstream cin;
	cin.open("A-large.in");
	ofstream cout;
	cout.open("result.txt");

	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		vector<string> board;
		board.clear();
		string row;
		for(int i = 0; i < 4; i++)
		{
			cin >> row;
			board.push_back(row);
		}
		cout << "Case #" << t << ": " << check(board) << endl;
	}

	cin.close();
	cout.close();

	return 0;
}

string check(vector<string> board)
{
	string ans;
	for(int row = 0; row < 4; row++)
	{
		char a = board[row][0];
		char b = board[row][1];
		char c = board[row][2];
		char d = board[row][3];
		ans = helper(a,b,c,d);
		if(ans != "") return ans;
	}
	for(int col = 0; col < 4; col++)
	{
		string ans;
		char a = board[0][col];
		char b = board[1][col];
		char c = board[2][col];
		char d = board[3][col];
		ans = helper(a,b,c,d);
		if(ans != "") return ans;
	}

	char a = board[0][0];
	char b = board[1][1];
	char c = board[2][2];
	char d = board[3][3];
	ans = helper(a,b,c,d);
	if(ans != "") return ans;

	a = board[0][3];
	b = board[1][2];
	c = board[2][1];
	d = board[3][0];
	ans = helper(a,b,c,d);
	if(ans != "") return ans;

	for(int i = 0; i < 4; i++)
	{
		for(int j = 0; j < 4; j++)
		{
			if(board[i][j] == '.')
				return "Game has not completed";
		}
	}

	return "Draw";

}

string helper(char a, char b, char c, char d)
{
	string ans;
	if(a == 'X')
	{
		if((b == a || b == 'T') && (c == a || c == 'T') && (d == a || d == 'T'))
			return "X won";
	}
	else if(a == 'O')
	{
		if((b == a || b == 'T') && (c == a || c == 'T') && (d == a || d == 'T'))
			return "O won";
	}
	else if(a == 'T')
	{
		if(b == c && b == d && b != '.')
		{
			if(b == 'X') return "X won";
			else return "O won";
		}
	}

	return "";
}
