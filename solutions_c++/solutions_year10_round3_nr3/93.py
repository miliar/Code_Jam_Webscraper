#include <iostream>
#include <vector>
#include <string>
using namespace std;

typedef unsigned char uch;

uch lines[512][512];

uch boards[512][512][512];

int distances[513][513];

void dumpdist(int m, int n) {
  for (int i = 0; i < m; ++i) {
    for (int j = 0; j < n; ++j) {
      cout << distances[i][j] << '\t';
    }
    cout << endl;
  }
}


#define BAD 3

void buildBoards(int m, int n, int k) {
  int mk1 = m - k + 1;
  int nk1 = n - k + 1;

  if (k % 2 == 0) {
    int half = k / 2;
    bool swap = (half % 2 != 0);
    for (int i = 0; i < mk1; ++i) {
      for (int j = 0; j < nk1; ++j) {
	int color = boards[half][i][j];
	int swapcolor = swap ? (!color) : color;
	if (color != BAD && boards[half][i+half][j] == swapcolor && boards[half][i][j+half] == swapcolor && boards[half][i+half][j+half] == color) {
	  boards[k][i][j] = color;
	} else {
	  boards[k][i][j] = BAD;
	}
      }
    }
  } else {
    int half = 1 + (k / 2);
    bool swap = (half % 2 == 0);
    for (int i = 0; i < mk1; ++i) {
      for (int j = 0; j < nk1; ++j) {
	int color = boards[half][i][j];
	int swapcolor = swap ? (!color) : color;
	if (color != BAD && boards[half][i+half-1][j] == swapcolor && boards[half][i][j+half-1] == swapcolor && boards[half][i+half-1][j+half-1] == color) {
	  boards[k][i][j] = color;
	} else {
	  boards[k][i][j] = BAD;
	}
      }
    }
  }
}

int cutholes(int m, int n, int k) {
  int numcuts = 0;
  int mk1 = m - k + 1;
  int nk1 = n - k + 1;
  for (int i = 0; i < mk1; ++i) {
    for (int j = 0; j < nk1; ++j) {
      if (distances[i][j] >= k && boards[k][i][j] != BAD) {
	//	if (k > 4) {
	  //	  cout << "distances " << i << " " << j << endl;
	  //	  dumpdist(m, n);
	  //	}
	// do cut hole
	numcuts ++;

	for (int p = 0; p < k; ++p) {
	  for (int q = 0; q < k; ++q) {
	    distances[i+p][j+q] = 0;
	  }
	}

	for (int p = i+k-1; p >= 0 && p > i-k; --p) {
	  for (int q = j+k-1; q >= 0 && q > j-k; --q) {
	    distances[p][q] = distances[p][q] == 0 ? 0 : (1 + min(distances[p+1][q], min(distances[p][q+1], distances[p+1][q+1])));
	  }
	}
      }
    }
  }

  return numcuts;
}

int main() {
  int t;
  cin >> t;
  for (int casenum = 1; casenum <= t; ++casenum) {
    int m, n;
    cin >> m;
    cin >> n;
    int ndiv4 = n / 4;

    for (int i = 0; i < m; ++i) {
      int j = 0;
      while (j < n) {
	char c;
	cin >> c;
	int tmp = 0;
	if ('0' <= c && c <= '9') {
	  tmp = c - '0';
	} else {
	  tmp = 10 + (c - 'A');
	}

	lines[i][j++] = ((tmp & 8) > 0);
	lines[i][j++] = ((tmp & 4) > 0);
	lines[i][j++] = ((tmp & 2) > 0);
	lines[i][j++] = ((tmp & 1) > 0);
      }
    }

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
	boards[1][i][j] = lines[i][j];
      }
    }

    int lesser = m < n ? m : n;
    for (int k = 2; k <= lesser; ++k) {
      buildBoards(m, n, k);
    }
    
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
	distances[i][j] = 520;
      }
    }

    for (int i = 0; i < m+1; ++i) {
      distances[i][n] = 0;
    }
    for (int j = 0; j < n; ++j) {
      distances[m][j] = 0;
    }


    vector< pair<int, int> > outs;

    for (int k = lesser; k >= 1; --k) {
      int filled = cutholes(m, n, k);
      if (filled > 0) {
	outs.push_back(make_pair(k, filled));
      }
    }
				 


    
    cout << "Case #" << casenum << ": ";
    cout << outs.size();
    cout << endl;
    for (int k = 0; k < outs.size(); ++k) {
      cout << outs[k].first << ' ' << outs[k].second << endl;
    }
  }
}
