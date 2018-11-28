#include <stdio.h>
#include <queue>

using namespace std;

typedef priority_queue<int,vector<int>,greater<int> > Q;

int readtime() {
  int h, m;
  scanf("%d:%d", &h, &m);
  return h * 60 + m;
}

int NA[100][2];
int NB[100][2];

void
sort(int a[100][2], int n) {
  for(int i = 0; i < n; i++) {
    for(int j = i+1; j < n; j++) {
      if (a[i][0] > a[j][0]) {
	int t = a[i][0];
	a[i][0] = a[j][0];
	a[j][0] = t;

	t = a[i][1];
	a[i][1] = a[j][1];
	a[j][1] = t;
      }
    }
  }
}

int
proc(int ot, int it, Q &from, Q &to) {
  int result = 0;
  if (from.empty() || from.top() > ot) {
    result = 1;
  } else {
    from.pop();
  }

  to.push(it);

  return result;
}

int
solve(int *ans) {
  int T =0, A=0, B=0;
  scanf("%d %d %d", &T, &A, &B);

  for (int i = 0; i < A; i++) {
    NA[i][0] = readtime();
    NA[i][1] = readtime();
  }

  for (int i = 0; i < B; i++) {
    NB[i][0] = readtime();
    NB[i][1] = readtime();
  }

  sort(NA, A);
  sort(NB, B);

  Q availA;
  Q availB;

  int ta = 0, tb = 0;

  while (ta < A || tb < B) {
    // departure times are earlier than arrival times
    if (ta >= A) {
      ans[1] += proc(NB[tb][0], NB[tb][1] + T, availB, availA);
      tb++;
    } else if (tb >= B) {
      ans[0] += proc(NA[ta][0], NA[ta][1] + T, availA, availB);
      ta++;
    } else if (NA[ta][0] <= NB[tb][0]) {
      ans[0] += proc(NA[ta][0], NA[ta][1] + T, availA, availB);
      ta++;
    } else {
      ans[1] += proc(NB[tb][0], NB[tb][1] + T, availB, availA);
      tb++;
    }
  }
}

int
main(int argc, char* argv[]) {
  int N;
  scanf("%d", &N);

  for( int i = 1; i <= N; i++ ) {
    int ans[] = {0,0};
    solve(ans);
    printf("Case #%d: %d %d\n", i, ans[0], ans[1]);
  }

  return 0;
}
