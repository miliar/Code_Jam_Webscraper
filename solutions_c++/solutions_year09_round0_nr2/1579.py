#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int _a;

#define FOR(i , n) for(int i = 0 ; i < n ; i++)
#define FOT(i , a , b) for(int i = a ; i < b ; i++)
#define GETINT (scanf("%d" , &_a) , _a)
#define pb push_back
#define mp make_pair
#define s(a) (int(a.size()))
#define PRINT(a) cerr << #a << " = " << a << endl

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int , int> PII;

int x[] = {-1, 0, 0, 1};
int y[] = {0, -1, 1, 0};

int main() {
  int board[100][100];
  int label[100][100];
  int tests;
  tests = GETINT;
  FOT(tt, 1, tests + 1) {
    int h = GETINT;
    int w = GETINT;
#define good(a,b) ((a) >= 0 && (a) < h && (b) >= 0 && (b) < w)
    FOR(i, h) FOR(j, w) board[i][j] = GETINT;
    FOR(i, h) FOR(j, w) label[i][j] = -1;
    int nums = 0;
    FOR(i, h) FOR(j, w) {
      bool sink = true;
      FOR(k, 4) if(good(i-x[k], j-y[k]) && board[i-x[k]][j-y[k]] < board[i][j]) sink = false;
      if(sink) {
        queue< PII > q;
        q.push(PII(i, j));
        label[i][j] = nums;
        while(!q.empty()) {
          PII cur = q.front(); q.pop();
          FOR(k, 4) {
            int nf, ns;
            nf = cur.first - x[k];
            ns = cur.second - y[k];
            if(good(nf, ns) && label[nf][ns] == -1 && board[nf][ns] > board[cur.first][cur.second]) {
              bool add = true;
              FOR(l, 4) {
                int nnf, nns;
                nnf = nf + x[l];
                nns = ns + y[l];
                if(good(nnf, nns) && (board[nnf][nns] < board[cur.first][cur.second] || (board[nnf][nns] == board[cur.first][cur.second] && l < k))) add = false;
                
              }
              if(add) {
                q.push(PII(nf, ns));
                label[nf][ns] = nums;
              }
            }
          }
        }
        nums++;
      }
    }
    map<int, char> m;
    char ccc = 'a';
    FOR(i, h) FOR(j, w) if(m.count(label[i][j]) == 0) {
      m[label[i][j]] = ccc++;
    }
    printf("Case #%d:\n", tt);
    FOR(i, h) FOR(j, w) printf("%c%c", m[label[i][j]], (j == w - 1 ? '\n' : ' '));
  }
  return 0;
}
