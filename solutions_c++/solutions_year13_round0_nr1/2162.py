#include <iostream>
#include <string>

using namespace std;

#define	For(i, a, b)	for(int i = (a) ; i < (b) ; ++i)
#define	rep(i, n)		For(i, 0, (n))

bool check(const char table[][10], const char c)
{
	rep(j, 4) {
		bool	f = true;
		rep(i, 4) {
			if(table[i][j] != c && table[i][j] != 'T') {
				f = false;
				break;
			}
		}
		if(f)
			return true;
	}
	rep(i, 4) {
		bool	f = true;
		rep(j, 4) {
			if(table[i][j] != c && table[i][j] != 'T') {
				f = false;
				break;
			}
		}
		if(f)
			return true;
	}
	rep(i, 4)
		if(table[i][i] != c && table[i][i] != 'T')
			goto Next;
	return true;

Next:
	rep(i, 4)
		if(table[3-i][i] != c && table[3-i][i] != 'T')
			return false;
	return true;
}

string solve()
{
	char	table[10][10];
	string	dummy;

	getline(cin, dummy);
	rep(i, 4)
		cin.getline(table[i], sizeof(table[0]));

	if(check(table, 'X'))
		return "X won";
	if(check(table, 'O'))
		return "O won";
	rep(i, 4)
		rep(j, 4)
			if(table[i][j] == '.')
				return "Game has not completed";
	return "Draw";
}

int main()
{
	int		T;
	cin >> T;
	rep(i, T)
		cout << "Case #" << (i + 1) << ": " << solve() << endl;
}

