#include <iostream>
#include <fstream>
#include <cassert>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
//download TTMath from http://www.ttmath.org/
//#include <ttmath/ttmath.h>

using namespace std;
//using namespace ttmath;

#define metafor(iter,container) \
	for ((iter) = (container).begin(); (iter) != (container).end(); ++(iter))
#define FOR(i,n) for (size_t i = 0; i < (n); ++i)

//typedef vector< vector<char> > Board;
typedef char Board[4][4];

//const Board empty(4,vector<char>(4,'.'));

inline is(char a, char ref)
{
	return a == ref || a == 'T';
}

inline bool check_row(const Board & b, int i, char c)
{
	return (is(b[i][0],c) && is(b[i][1],c) && is(b[i][2],c) && is(b[i][3],c));
}

inline bool check_col(const Board & b, int j, char c)
{
	return (is(b[0][j],c) && is(b[1][j],c) && is(b[2][j],c) && is(b[3][j],c));
}

inline bool check_diag(const Board & b, char c)
{
	return (is(b[0][0],c) && is(b[1][1],c) && is(b[2][2],c) && is(b[3][3],c));
}

inline bool check_rdiag(const Board & b, char c)
{
	return (is(b[0][3],c) && is(b[1][2],c) && is(b[2][1],c) && is(b[3][0],c));
}


const string Xw = "X won";
const string Ow = "O won";
const string Drw = "Draw";
const string NOY = "Game has not completed";

string solve_case(const Board & b)
{
	//check rows
	for (int i = 0; i < 4; ++i)
		if (check_row(b,i,'X')) return Xw;
		else if (check_row(b,i,'O')) return Ow;
	//check cols
	for (int j = 0; j < 4; ++j)
		if (check_col(b,j,'X')) return Xw;
		else if (check_col(b,j,'O')) return Ow;
	//check diags
	if (check_diag(b,'X')) return Xw;
	else if (check_diag(b,'O')) return Ow;
	if (check_rdiag(b,'X')) return Xw;
	else if (check_rdiag(b,'O')) return Ow;

	//find '.'
	for (int i = 0; i < 4; ++i)
	for (int j = 0; j < 4; ++j)
		if (b[i][j] == '.') return NOY;

	return Drw;
}

void solve(istream & in, ostream & out)
{
	int TC_NCases;
	in >> TC_NCases;
	out.precision(18);
	out.setf(std::ios_base::fixed, std::ios_base::floatfield);
	for (int t = 1; t <= TC_NCases; ++t)
	{
		Board b; //(empty);
		for (int i = 0; i < 4; ++i)
		for (int j = 0; j < 4; ++j)
			in >> b[i][j];

		string result = solve_case(b);
		out << "Case #" << t << ": " << result << endl;
	}
}


int main()
{
	//ifstream in("A-sample.in");
	//ofstream out("A-sample-out.txt");

	//ifstream in("A-small-attempt0.in");
	//ofstream out("A-small-out.txt");

	ifstream in("A-large.in");
	ofstream out("A-large-out.txt");

	solve(in,out);

	return 0;
}
