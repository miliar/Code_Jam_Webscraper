#include <iostream>
#include <fstream>
#include <cassert>
#include <vector>
#include <string>
#include <algorithm>
//download TTMath from http://www.ttmath.org/
//#include <ttmath/ttmath.h>

using namespace std;
//using namespace ttmath;

void rotate(size_t N, const vector<string> & board, vector<string> & result)
{
	for (size_t r = 0; r < N; ++r) {
	for (size_t c = 0; c < N; ++c) {
		result[c][N-1-r] = board[r][c];
	}
	}
}

// assume result inicialized with '.'
void left_gravity(size_t N, const vector<string> & board, vector<string> & result)
{
	for (size_t r = 0; r < N; ++r) {
		int c = N-1;
		int d = N-1;
		for (; c >= 0; --c)
			if (board[r][c] != '.') {
				result[r][d] = board[r][c];
				--d;
			}
	}
}

pair<bool,bool> findline_horiz(size_t N, size_t K, const vector<string> & board)
{
	bool Bdid = false, Rdid = false;
	size_t longR = 0, longB = 0;
	for (size_t r = 0; r < N; ++r) {
		for (size_t c = 0; c < N; ++c) {
			char prev = r == 0 ? '.' : board[r][c-1];
			switch (board[r][c])
			{
			case 'B':
				if (prev != 'B')
					longB = 1;
				else {
					++longB;
				}
				break;
			case 'R':
				if (prev != 'R')
					longR = 1;
				else {
					++longR;
				}
				break;
			case '.':
				//longB = longR = 0;
				break;
			default:
				assert(false);
			}
			if (longB == K) Bdid = true;
			if (longR == K) Rdid = true;
			if (Bdid && Rdid) return make_pair(Bdid,Rdid);
		}
	}
	return make_pair(Bdid,Rdid);
}

pair<bool,bool> findline_vert(size_t N, size_t K, const vector<string> & board)
{
	bool Bdid = false, Rdid = false;
	size_t longR = 0, longB = 0;
	for (size_t c = 0; c < N; ++c) {
		for (size_t r = 0; r < N; ++r) {
			char prev = r == 0 ? '.' : board[r-1][c];
			switch (board[r][c])
			{
			case 'B':
				if (prev != 'B')
					longB = 1;
				else {
					++longB;
				}
				break;
			case 'R':
				if (prev != 'R')
					longR = 1;
				else {
					++longR;
				}
				break;
			case '.':
				//longB = longR = 0;
				break;
			default:
				assert(false);
			}
			if (longB == K) Bdid = true;
			if (longR == K) Rdid = true;
			if (Bdid && Rdid) return make_pair(Bdid,Rdid);
		}
	}
	return make_pair(Bdid,Rdid);
}

pair<bool,bool> findline_diag(size_t N, size_t K, const vector<string> & board)
{
	bool Bdid = false, Rdid = false;
	for (size_t r = 0; r < N; ++r) {
		size_t longR = 0, longB = 0;
		for (size_t c = 0; c <= r; ++c) {
			char prev = c == 0 ? '.' : board[r-c+1][c-1];
			switch (board[r-c][c])
			{
			case 'B':
				if (prev != 'B')
					longB = 1;
				else {
					++longB;
				}
				break;
			case 'R':
				if (prev != 'R')
					longR = 1;
				else {
					++longR;
				}
				break;
			case '.':
				//longB = longR = 0;
				break;
			default:
				assert(false);
			}
			if (longB == K) Bdid = true;
			if (longR == K) Rdid = true;
			if (Bdid && Rdid) return make_pair(Bdid,Rdid);
		}
	}
	for (size_t c = 1; c < N; ++c) {
		size_t longR = 0, longB = 0;
		for (size_t i = 0; i <= N-1-c; ++i) {
			size_t r = N-1-i;
			char prev = r == N-1 ? '.' : board[r+1][c+i-1];
			switch (board[r][c+i])
			{
			case 'B':
				if (prev != 'B')
					longB = 1;
				else {
					++longB;
				}
				break;
			case 'R':
				if (prev != 'R')
					longR = 1;
				else {
					++longR;
				}
				break;
			case '.':
				//longB = longR = 0;
				break;
			default:
				assert(false);
			}
			if (longB == K) Bdid = true;
			if (longR == K) Rdid = true;
			if (Bdid && Rdid) return make_pair(Bdid,Rdid);
		}
	}
	return make_pair(Bdid,Rdid);
}

pair<bool,bool> findline_diag2(size_t N, size_t K, const vector<string> & board)
{
	bool Bdid = false, Rdid = false;
	for (size_t r = 0; r < N; ++r) {
		size_t longR = 0, longB = 0;
		for (size_t c = 0; c <= N-1-r; ++c) {
			char prev = c == 0 ? '.' : board[r+c-1][c-1];
			switch (board[r+c][c])
			{
			case 'B':
				if (prev != 'B')
					longB = 1;
				else {
					++longB;
				}
				break;
			case 'R':
				if (prev != 'R')
					longR = 1;
				else {
					++longR;
				}
				break;
			case '.':
				//longB = longR = 0;
				break;
			default:
				assert(false);
			}
			if (longB == K) Bdid = true;
			if (longR == K) Rdid = true;
			if (Bdid && Rdid) return make_pair(Bdid,Rdid);
		}
	}
	for (size_t c = 1; c < N; ++c) {
		size_t longR = 0, longB = 0;
		for (size_t r = 0; r <= N-1-c; ++r) {
			char prev = r == 0 ? '.' : board[r-1][c+r-1];
			switch (board[r][c+r])
			{
			case 'B':
				if (prev != 'B')
					longB = 1;
				else {
					++longB;
				}
				break;
			case 'R':
				if (prev != 'R')
					longR = 1;
				else {
					++longR;
				}
				break;
			case '.':
				//longB = longR = 0;
				break;
			default:
				assert(false);
			}
			if (longB == K) Bdid = true;
			if (longR == K) Rdid = true;
			if (Bdid && Rdid) return make_pair(Bdid,Rdid);
		}
	}
	return make_pair(Bdid,Rdid);
}

string solve_rotate_case(size_t N, size_t K, const vector<string> & board)
{
	vector<string> moved(N, string(N,'.'));
	//vector<string> rotated(N, string(N,'.'));
	left_gravity(N,board,moved);
	//rotate(N,moved,rotated);

	pair<bool,bool> horiz = findline_horiz(N,K,moved);
	pair<bool,bool> vert = findline_vert(N,K,moved);
	pair<bool,bool> diag1 = findline_diag(N,K,moved);
	pair<bool,bool> diag2 = findline_diag2(N,K,moved);
	pair<bool,bool> all(
		horiz.first || vert.first || diag1.first || diag2.first, 
		horiz.second|| vert.second || diag1.second || diag2.second
		);

	if (all.first && all.second)
		return "Both";
	else if (all.first)
		return "Blue";
	else if (all.second)
		return "Red";
	else
		return "Neither";

	//string result;
	//result += '\n';
	//for (size_t r = 0; r < N; ++r) {
	//	result += rotated[r];
	//	result += '\n';
	//}
	//return result;

	//string result;
	//result += '\n';
	//for (size_t r = 0; r < N; ++r) {
	//	result += moved[r];
	//	result += '\n';
	//}
	//return result;
}

void solve_rotate(istream & in, ostream & out)
{
	int C;
	in >> C;
	for (int t = 1; t <= C; ++t)
	{
		size_t K, N;
		in >> N >> K;
		vector<string> board(N);
		for (size_t i = 0; i < N; ++i) {
			in >> board[i];
			assert(board[i].size() == N);
		}
		string result = solve_rotate_case(N, K, board);
		out << "Case #" << t << ": " << result << "\n";
	}
}


int main()
{
	//test_gcd();

	assert(sizeof(long long) == 8);
	//ifstream in("A-sample.in");
	//ofstream out("A-sample.txt");

	//ifstream in("A-small-attempt0.in");
	//ofstream out("A-small-out.txt");

	ifstream in("A-large.in");
	ofstream out("A-large-out-DEBUG.txt");

	solve_rotate(in,out);

	return 0;
}