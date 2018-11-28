#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <map>
#include <set>
#include <tr1/unordered_map>
#include <tr1/unordered_set>
#include <stdlib.h>
#include <math.h>
#include <functional>
#include <iomanip>
#include <sstream>
#include <algorithm>

using namespace std;

struct Elem {
	int X;
	int Y;

	Elem() : X(-1), Y(-1) {}
	Elem(int x, int y) : X(x), Y(y) {}
};


class ProblemSolver {
public:
	ProblemSolver() : ist("input.txt"), ost("output.txt") {}
	void Run();
	void SolveOneTest();

private:
	std::ifstream ist;
	std::ofstream ost;

	bool findMatching();
	int getAnswer();
	void dfs2(int x, int y);
	vector<Elem> getCandidates(int x, int y);
	bool dfs(int x, int y);

	vector<string> mBels;
	vector<vector<Elem> > mChain;
	vector<vector<bool> > mVis;
	vector<Elem> mUsed;
	int mRes;
	int n,m;
	Elem mBase;
};

const int modulo = 1000003;

int ProblemSolver::getAnswer()
{
	mVis = vector<vector<bool> >(n, vector<bool>(m));
	mRes = 1;
	vector<vector<bool> > used(n, vector<bool>(m));
	for( int i = 0; i < n; i++ ) {
		for( int j = 0; j < m; j++ ) {
			mBase.X = i;
			mBase.Y = j;
			int prev = mRes;
			if( !used[i][j] ) {
				dfs2(i,j);
			}
			for( int i = 0; i < n; i++ ) {
				for( int j = 0; j < m; j++ ) {
					if( mVis[i][j] ) {
						if( mRes != prev ) {
							used[i][j] = true;
						}
						mVis[i][j] = false;
					}
				}
			}
		}
	}
	return mRes;
}

bool ProblemSolver::findMatching() {
	mChain = vector< vector<Elem> >(n, vector<Elem>(m));
	mVis = vector< vector<bool > >(n, vector<bool>(m));
	for( int i = 0; i < n; i++ ) {
		for( int j = 0; j < m; j++ ) {
			if( !dfs(i, j) ) {
				return false;
			}
			for( int k = 0; k < mUsed.size(); k++ ) {
				mVis[mUsed[k].X][mUsed[k].Y] = false;
			}
			mUsed.clear();
		}
	}
	for( int i = 0; i < n; i++ ) {
		for( int j = 0; j < m; j++ ) {
		//	cout << "(" << mChain[i][j].X << " " << mChain[i][j].Y << ") ";
		}
	//	cout << endl;
	}
	return true;
}

void ProblemSolver::dfs2(int x, int y) { 
	mVis[x][y] = true;
//	cout << "+ " << x << " " << y << endl;
	vector<Elem> candidate = getCandidates(x,y);
	for( int i = 0; i < candidate.size(); i++ ) {
		int nx = mChain[candidate[i].X][candidate[i].Y].X;
		int ny = mChain[candidate[i].X][candidate[i].Y].Y;
		if( nx == x && ny == y ) continue;
		if( mVis[nx][ny] ) {
			if( nx == mBase.X && ny == mBase.Y ) {
				mRes = (mRes * 2) % modulo;
//				cout << "FOUND!!" << endl;
			}
		} else {
			dfs2(nx, ny);
		}
	}
//	cout << "- " << x << " " << y << endl;
}

inline vector<Elem> ProblemSolver::getCandidates(int x, int y)
{
	vector<Elem> res;
	switch( mBels[x][y] ) {
		case '|':
			res.push_back(Elem((x-1+n) % n, y));
			res.push_back(Elem((x+1) % n, y));
			break;
		case '/':
			res.push_back(Elem((x-1+n) % n, (y+1) % m));
			res.push_back(Elem((x+1) % n, (y-1+m) % m));
			break;
		case '\\':
			res.push_back(Elem((x-1+n) % n, (y-1+m) % m));
			res.push_back(Elem((x+1) % n, (y+1) % m));
			break;
		case '-':
			res.push_back(Elem(x, (y-1+m) % m));
			res.push_back(Elem(x, (y+1) % m));
			break;
	}
	return res;
}

inline bool ProblemSolver::dfs(int x, int y) { 
	mVis[x][y] = true;
	mUsed.push_back(Elem(x,y));	
	vector<Elem> cands = getCandidates(x,y);
	for( int i = 0; i < cands.size(); i++ ) {
		if( mChain[cands[i].X][cands[i].Y].X == -1 ) {
			mChain[cands[i].X][cands[i].Y].X = x;
			mChain[cands[i].X][cands[i].Y].Y = y;
			return true;
		}
	}
	for( int i = 0; i < cands.size(); i++ ) {
		int nextX = mChain[cands[i].X][cands[i].Y].X;
		int nextY = mChain[cands[i].X][cands[i].Y].Y;
		if( mVis[nextX][nextY] ) continue;
		if( dfs(nextX, nextY) ) {
			mChain[cands[i].X][cands[i].Y].X = x;
			mChain[cands[i].X][cands[i].Y].Y = y;
			return true;
		}
	}
	return false;
}

inline void ProblemSolver::SolveOneTest() 
{
	ist >> n >> m;
	mBels.resize(n);
	for( int i = 0; i < n; i++ ) {
		ist >> mBels[i];
	}
	if( !findMatching() ) {
		ost << "0" << endl;
	} else {
		ost << getAnswer() << endl;
	}
}


inline void ProblemSolver::Run()
{
	int tn;
	ist >> tn;
	for( int i = 0; i < tn; i++ ) {
		ost << "Case #" << (i+1) << ": ";
		SolveOneTest();
	}
}

int main() 
{
	ProblemSolver solver;
	solver.Run();
	return 0;
}

