/*
ID: Plagapong
LANG: C++
TASK: B
*/

#include<iostream>
#include<fstream>
#include<algorithm>
#define INF 999999999
#define SUMMER(A, XI, XF, YI, YF) (A[XF][YF] - A[XI-1][YF] - A[XF][YI-1] + A[XI-1][YI-1])

using namespace std;
ifstream fin;
ofstream fout;

int r, c, d;
char pam[504][504];
int coco[504][504];
int roro[504][504];
int soso[504][504];

void clearVars() {
  // Clear variables
  for (int i = 0; i < 504; i++) {
	fill(pam[i], pam[i] + 504, 0);
	fill(coco[i], coco[i] + 504, 0);
	fill(roro[i], roro[i] + 504, 0);
	fill(soso[i], soso[i] + 504, 0);
  }
}

bool ok(int si, int sj, int ss) {
  int cx = 0, cy = 0;
  int dx, dy, dd = (ss - 1);
  for (int i = si; i < si + ss; i++) {
	for (int j = sj; j < sj + ss; j++) {
	  dx = 2*(i - si) - dd; dy = 2*(j - sj) - dd;
	  if (abs(dx) == dd && abs(dy) == dd)
		continue;
	  cx += (dx * (pam[i][j] - '0'));
	  cy += (dy * (pam[i][j] - '0'));
	}
  }
  cout << si << sj << ss << " " << cx << " " << cy << endl;
  return (!cx && !cy);
}

bool oker(int si, int sj, int ss) {
  int cx = 0, cy = 0;
  
  cx = 2 * SUMMER(roro, si, si+ss-1, sj, sj+ss-1);
  cx -= (2 * sj + ss - 1) * SUMMER(soso, si, si+ss-1, sj, sj+ss-1);
  
  cy = 2 * SUMMER(coco, si, si+ss-1, sj, sj+ss-1);
  cy -= (2 * si + ss - 1) * SUMMER(soso, si, si+ss-1, sj, sj+ss-1);

  //cout << cx << "!" << cy << endl;

  cx -= (ss-1) * (int) (- pam[si][sj] + pam[si][sj+ss-1]
						- pam[si+ss-1][sj] + pam[si+ss-1][sj+ss-1]);
  cy -= (ss-1) * (int) (- pam[si][sj] - pam[si][sj+ss-1]
						+ pam[si+ss-1][sj] + pam[si+ss-1][sj+ss-1]);

  //cout << (ss-1) * (int) (- pam[si][sj] + pam[si][sj+ss-1]
  //						  - pam[si+ss-1][sj] + pam[si+ss-1][sj+ss-1]) << endl;
  
  //cout << si << sj << ss << " " << cx << " " << cy << endl;
  return (!cx && !cy);
}

void process() {
  // Code here!
  fin >> r >> c >> d;
  for (int i = 1; i <= r; i++) {
	fin >> &pam[i][1];
  }
  
  for (int i = 1; i <= r; i++) {
	for (int j = 1; j <= c; j++) {
	  soso[i][j] = soso[i][j-1] + soso[i-1][j] - soso[i-1][j-1] 
		+ (pam[i][j] - '0');
	  roro[i][j] = roro[i][j-1] + roro[i-1][j] - roro[i-1][j-1]
		+ (pam[i][j] - '0') * j;
	  coco[i][j] = coco[i][j-1] + coco[i-1][j] - coco[i-1][j-1]
		+ (pam[i][j] - '0') * i;
	}
  }

  int maxS = 0;
  for (int i = 1; i <= r; i++) {
	for (int j = 1; j <= c; j++) {
	  for (int s = 3; i+s-1 <= r && j+s-1 <= c; s++) {
		if (s < maxS) continue;
		//ok(i,j,s);
		if (oker(i,j,s))
		  maxS = max(maxS, s);
	  }
	}
  }
  if (maxS)
	fout << maxS;
  else
	fout << "IMPOSSIBLE";
}

int main(int argc, const char* argv[]) {
  if (argc != 3) {
	cout << "Please indicate input and output" << endl;
	exit(0);
  }
  fin.open(argv[1]);
  fout.open(argv[2]);
  int times;
  fin >> times;
  for (int i = 1; i <= times; i++) {
	fout << "Case #" << i << ": ";
	clearVars();
	process();
	fout << endl;
  }
  fin.close();
  fout.close();
  return 0;
}
