
#include <iostream>

using namespace std;

int K, N, T, k[100];
char A[100][100], B[100][100];

int main() {
  cin >> T;
  for (int z = 1; z <= T; z++) {
    cin >> N >> K;
    for (int i = 0; i < N; i++)
      for (int j = 0; j < N; j++)
	cin >> A[i][j];

    for (int i = 0; i < N; i++) {
      k[N-1-i] = N-1;
      for (int j = N-1; j >= 0; j--)
	if (A[i][j] != '.')
	  B[k[N-1-i]--][N-1-i] = A[i][j];
    }

    //for (int i = 0; i < N; i++) {
    //  for (int j = 0; j < N; j++)
    //	if (k[j] < i) cout << B[i][j];
    //	else cout << '.';
    //  cout << "\n";
    //}

    bool a = 0, b = 0;
    for (int i = 0; i < N; i++) {
      int c = '.', d = 0;
      for (int j = 0; j < N; j++) {
	if (k[j] < i) {
	  if (B[i][j] == c) {
	    d++;
	    if (d == K) {
	      if (B[i][j] == 'R') a = true;
	      else b = true;
	    }
	  }
	  else {
	    c = B[i][j];
	    d = 1;
	  }
	}
	else {
	  c = '.';
	  d = 0;
	}
      }
    }

    for (int j = 0; j < N; j++) {
      int c = '.', d = 0;
      for (int i = N-1; k[j] < i; i--) {
	//if (z == 2) cout << i << "," << j << "," << B[i][j] << "\n";
	if (B[i][j] == c) {
	  d++;
	  if (d == K) {
	    if (B[i][j] == 'R') a = true;
	    else b = true;
	  }
	}
	else {
	  c = B[i][j];
	  d = 1;
	}
      }
    }

    for (int i = 0; i < N; i++) {
      int c = '.', d = 0;
      for (int j = i; j >= 0; j--)
	if (k[j] < j) {
	  if (B[j][j] == c) {
	    d++;
	    if (d == K) {
	      if (B[j][j] == 'R') a = true;
	      else b = true;
	    }
	  }
	  else {
	    c = B[j][j];
	    d = 1;
	  }
	}
	else {
	  c = '.';
	  d = 0;
	}
    }

    for (int j = 1; j < N; j++) {
      int c = '.', d = 0;
      for (int i = N; i > j; i--)
	if (k[j+N-i] < i-1) {
	  if (B[i-1][j+N-i] == c) {
	    d++;
	    if (d == K) {
	      if (B[i-1][j+N-i] == 'R') a = true;
	      else b = true;
	    }
	  }
	  else {
	    c = B[i-1][j+N-i];
	    d = 1;
	  }
	}
	else {
	  c = '.';
	  d = 0;
	}
    }

    for (int i = 0; i < N; i++) {
      int c = '.', d = 0;
      for (int j = i; j >= 0; j--)
	if (k[j] < N-1-j) {
	  if (B[N-1-j][j] == c) {
	    d++;
	    if (d == K) {
	      if (B[N-1-j][j] == 'R') a = true;
	      else b = true;
	    }
	  }
	  else {
	    c = B[N-1-j][j];
	    d = 1;
	  }
	}
	else {
	  c = '.';
	  d = 0;
	}
    }

    for (int j = 1; j < N; j++) {
      int c = '.', d = 0;
      for (int i = N; i > j; i--)
	if (k[i-j-1] < i-1) {
	  if (B[i-1][i-j-1] == c) {
	    d++;
	    if (d == K) {
	      if (B[i-1][i-j-1] == 'R') a = true;
	      else b = true;
	    }
	  }
	  else {
	    c = B[i-1][i-j-1];
	    d = 1;
	  }
	}
	else {
	  c = '.';
	  d = 0;
	}
    }

    cout << "Case #" << z << ": ";
    if (a && b) cout << "Both\n";
    else if (a) cout << "Red\n";
    else if (b) cout << "Blue\n";
    else cout << "Neither\n";
  }
}
