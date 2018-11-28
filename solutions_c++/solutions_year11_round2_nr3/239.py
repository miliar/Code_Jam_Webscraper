#include <iostream>
#include <vector>

using namespace std;

bool paint(int N, int cur, int rooms[8], int nrooms, int colors[8], int mx)
{
  if (N == cur) return true;

  for (int c = 1; c <= mx; c++) {
    colors[cur] = c;

    for (int i = 0; i < nrooms; i++) {
      int r = rooms[i];
      int nc = 0;
      int cs = 0;
      for (int j = 0; j < N; j++) {
	if (r & (1 << j)) {
	  if (j <= cur) {
	    if (cs & (1 << colors[j])) continue;
	    cs |= 1 << colors[j];
	    nc++;
	  } else {
	    nc++;
	  }
	}
      }
      if (nc < mx) goto fail;
    }
    if (paint(N, cur+1, rooms, nrooms, colors, mx)) return true;
  fail:;
  }
  return false;
}

int main()
{
  int T;
  cin >> T;

  for (int cas = 1; cas <= T; cas++) {
    int M, N;
    cin >> N >> M;

    vector<int> U;
    vector<int> V;

    for (int i = 0; i < M; i++) {
      int p;
      cin >> p;
      U.push_back(p-1);
    }
    for (int i = 0; i < M; i++) {
      int p;
      cin >> p;
      V.push_back(p-1);
    }

    int rooms[8];
    int nrooms = 1;
    rooms[0] = (1 << N) - 1;
    for (int i = 0; i < M; i++) {
      int r0 = 0, r1 = (1 << N) - 1;
      int f = 1 << U[i];
      int t = 1 << V[i];
      r0 = t - f;
      r1 &= ~r0;
      r0 |= t;
      r0 |= f;
      r1 |= t;
      r1 |= f;

      for (int j = 0; j < nrooms; j++) {
	if ((rooms[j] & f) && (rooms[j] & t)) {
	  rooms[nrooms] = rooms[j] & r0;
	  rooms[j] &= r1;
	}
      }
      nrooms++;
    }
    int mx = 0;
    for (int i = 0; i < nrooms; i++) {
      int m = 0;
      for (int j = 0; j < N; j++) {
	if (rooms[i] & (1 << j)) m++;
      }
      if (m > mx) mx = m;
    }
    for (int j = mx; j >= 3; j--) {
      int colors[8];
      if (paint(N, 0, rooms, nrooms, colors, j)) {
	cout << "Case #" << cas << ": " << j << endl;
	const char *s = "";
	for (int k = 0; k < N; k++) {
	  cout << s << colors[k];
	  s = " ";
	}
	cout << endl;
	break;
      }
    }
  }

  return 0;
}
