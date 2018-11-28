/* 
Google Codejam 2010 - Round 1A
A. Rotate

C++ Solution by:
 Marco Chiesi
 chiesi@gmail.com
*/

#include <string>
#include <sstream>
#include <fstream>
#include <iostream>

using namespace std;

/**
 * Class for a single instance of the problem
 */
class Instance {
    private:
        int N, K;
        char grid[51][51];
        string solution;

    public:
	void readInput(istream &in) {
        in >> N >> K;
		for (int i = 0; i < N ; i++) {
                in >> grid[i];
        }
	}

	void solve() {
		for (int i = 0; i < N ; i++) {
    		for (int j = 0; j < N ; j++) {
               cout << grid[i][j];
            }
            cout << endl;
        }
        // Apply gravity to the right
		for (int i = 0; i < N ; i++) {
		    for (int j = N-1; j >=0 ; j--) {
                if (grid[i][j] == '.') {
                    for (int k=j-1; k>=0; k--) {
                        if(grid[i][k] != '.') {
                            char tmp = grid[i][k];
                            grid[i][k] = grid[i][j];
                            grid[i][j] = tmp;
                            break;
                        }
                    }
                }
            }
        }
		for (int i = 0; i < N ; i++) {
    		for (int j = 0; j < N ; j++) {
               cout << grid[i][j];
            }
            cout << endl;
        }
        // Check for K-lines
        bool rwin = false;
        bool bwin = false;
        int bvlines, rvlines, bhlines, rhlines, bdlines, rdlines;
        // Horizontal
        for (int i=N-1; i>=0; i--) {
            bvlines = grid[i][N-1] == 'B'? 1:0;
            rvlines = grid[i][N-1] == 'R'? 1:0;
            for (int j=N-2; j>=0; j--) {
                if(grid[i][j] == 'R' && !rwin) {
                    rvlines++;
                    bvlines=0;
                }
                else if(grid[i][j] == 'B' && !bwin) {
                    bvlines++;
                    rvlines=0;
                }
                else if(grid[i][j] == '.') {
                    break;
                }
                else {
                    rvlines=0;
                    bvlines=0;
                }
                if (rvlines == K) {
                    rwin = true;
                }
                if (bvlines == K) {
                    bwin = true;
                }
            }
        }
        // Vertical
        for (int j=N-1; j>=0; j--) {
            bhlines = grid[N-1][j] == 'B'? 1:0;
            rhlines = grid[N-1][j] == 'R'? 1:0;
            for (int i=N-2; i>=0; i--) {
                if(grid[i][j] == 'R' && !rwin) {
                    rhlines++;
                    bhlines=0;
                }
                else if(grid[i][j] == 'B' && !bwin) {
                    bhlines++;
                    rhlines=0;
                }
                else if(grid[i][j] == '.') {
                    break;
                }
                else {
                    rhlines=0;
                    bhlines=0;
                }
                if (rhlines == K) {
                    rwin = true;
                }
                if (bhlines == K) {
                    bwin = true;
                }
            }
        }
        // Diagonal
        for (int i=N-1; i>=0; i--) {
            for (int j=N-1; j>=0; j--) {
                bdlines = grid[i][j] == 'B'? 1:0;
                rdlines = grid[i][j] == 'R'? 1:0;
                for (int k=1; k<K && i-k>=0 && j-k>=0; k++) {
                    if(grid[i-k][j-k] == 'R' && !rwin) {
                        rdlines++;
                        bdlines=0;
                    }
                    else if(grid[i-k][j-k] == 'B' && !bwin) {
                        bdlines++;
                        rdlines=0;
                    }
                    else if(grid[i-k][j-k] == '.') {
                        break;
                    }
                    else {
                        rdlines=0;
                        bdlines=0;
                    }
                    if (rdlines == K) {
                        rwin = true;
                    }
                    if (bdlines == K) {
                        bwin = true;
                    }
                }
            }
        }
        // Diagonal
        for (int i=N-1; i>=0; i--) {
            for (int j=N-1; j>=0; j--) {
                bdlines = grid[i][j] == 'B'? 1:0;
                rdlines = grid[i][j] == 'R'? 1:0;
                for (int k=1; k<K && i-k>=0 && j+k<N; k++) {
                    if(grid[i-k][j+k] == 'R' && !rwin) {
                        rdlines++;
                        bdlines=0;
                    }
                    else if(grid[i-k][j+k] == 'B' && !bwin) {
                        bdlines++;
                        rdlines=0;
                    }
                    else if(grid[i-k][j+k] == '.') {
                        break;
                    }
                    else {
                        rdlines=0;
                        bdlines=0;
                    }
                    if (rdlines == K) {
                        rwin = true;
                    }
                    if (bdlines == K) {
                        bwin = true;
                    }
                }
            }
        }


        if (bwin && rwin) {
            solution = "Both";
        }
        else if (rwin) {
            solution = "Red";
        }
        else if (bwin) {
            solution = "Blue";
        }
        else {
            solution = "Neither";
        }
	}

	string getSolution() {
    	stringstream ss;
        ss << solution;
		return ss.str();
	}
};

/**
 * Class for a problem
 */
class Problem {
	private:
        Instance *instances;
	    int cases;
	
	public:
	void readInput(istream &in) {
		in >> cases;
		instances = new Instance[cases];
		for (int i = 0; i < cases; i++) {
			instances[i].readInput(in);
		}
	}
	
	void solve() {
		for (int i = 0; i < cases; i++) {
			instances[i].solve();
		}
	}
	
	void writeOutput(ostream &out) {
		for (int i = 0; i < cases; i++) {
			out << "Case #" << i+1 << ": " << instances[i].getSolution() << endl;
		}
	}
};

/**
 * Main function
 */
int main(int argc, char *argv[]) {
    istream *in;
    ostream *out;
    if (argc > 1) {
        in = new fstream(argv[1], fstream::in);
    }
    else {
        in = &cin;
    }
    if (argc > 2) {
        out = new fstream(argv[2], fstream::out);
    }
    else {
        out = &cout;
    }
    Problem *problem = new Problem();
    problem->readInput(*in);
    problem->solve();
    problem->writeOutput(*out);
    return 0;
}
