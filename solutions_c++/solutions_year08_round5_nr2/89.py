#include <vector>
#include <map>
#include <set>
#include <stack>
#include <string>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <queue>
#include <fstream>
#include <iomanip>

using namespace std;

#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x).size())
#define pb push_back
#define fr(i, n) for(i = 0; i < (n); i++)
#define fr2(i, s, n) for(i = (s); i < (n); i++)

typedef long long ll;
#define mp make_pair
typedef vector<int> VI;
typedef vector<string> VS;
typedef istringstream ISS;
typedef ostringstream OSS;
#define _cl(x) memset(x, 0, sizeof(x))
#define _rs(x) memset(x, -1, sizeof(x))

#define rng(x, b) (0 <= (x) && (x) < (b))
int _mx[] = {0, 1, 0, -1};
int _my[] = {-1, 0, 1, 0};

struct POINT { int r, c; };
struct QUEUE {
 POINT p, y, b;
 int c; // cost
 int prev; //debug
};

const int MAX = 15 * 15 * 15 * 15 * 15 * 15;
const int MAXR = 16;

int R, C;
int Q;
QUEUE q[MAX];
bool v[MAXR][MAXR][MAXR][MAXR][MAXR][MAXR];
char a[20][20];
POINT portals[20][20][4];

void read(ifstream &fin)
{
 int r, c;
 string s;

 fin >> R >> C;

 fr(r, R)
 {
  fin >> s;

  fr(c, C)
   a[r][c] = s[c];
 }
}

inline bool move(POINT &p, int d)
{
 p.r += _my[d];
 p.c += _mx[d];

 if(rng(p.r, R) && rng(p.c, C) && a[p.r][p.c] != '#')
  return true;
 else
  return false;
}

inline bool tele(POINT &p, POINT &y, POINT &b)
{
 if(y.r == p.r && y.c == p.c)
 {
  p = b;
  return true;
 }
 else
  return false;
}

inline void set_portal(POINT &p, POINT &x, int i)
{
 if(i >= 4)
  return;

 x = portals[p.r][p.c][i];
}

inline void add_queue(QUEUE x)
{
 if(v[x.p.r][x.p.c][x.y.r][x.y.c][x.b.r][x.b.c])
  return;

 v[x.p.r][x.p.c][x.y.r][x.y.c][x.b.r][x.b.c] = true;

 q[Q] = x;
 Q++;
}

void init()
{
 int r, c, i, j;

 fr(r, R) fr(c, C) fr(i, 4) fr(j, 20)
 {
  int rr = r + _my[i] * j;
  int cc = c + _mx[i] * j;

  if(rng(rr, R) && rng(cc, C) && a[rr][cc] != '#')
   portals[r][c][i].r = rr, portals[r][c][i].c = cc;
  else
   break;
 }
}

inline void move_add_queue(QUEUE &cur)
{
 int i;
 QUEUE n;

 fr(i, 4)
 {
  n = cur;
  if(move(n.p, i))
  {
   n.c++;
   add_queue(n);
  }
 }

 n = cur;
 if(tele(n.p, n.y, n.b))
 {
  n.c++;
  add_queue(n);
 }

 n = cur;
 if(tele(n.p, n.b, n.y))
 {
  n.c++;
  add_queue(n);
 }
}

void proc(ofstream &fout)
{
 int r, c;
 int i, j;
 int qp;
 QUEUE cur, n;
 POINT cake;

 init();
 _cl(v);

 fr(r, R) fr(c, C)
  if(a[r][c] == 'O')
   q[0].p.r = r, q[0].p.c = c;
  else if(a[r][c] == 'X')
   cake.r = r, cake.c = c;

 q[0].b = q[0].y = portals[q[0].p.r][q[0].p.c][0];
 Q = 1;

 for(qp = 0; qp < Q; qp++)
 {
  cur = q[qp];

  if(cur.p.r == cake.r && cur.p.c == cake.c)
   break;

  fr(i, 5) fr(j, 5)
  {
   n = cur;
   set_portal(n.p, n.y, i);
   set_portal(n.p, n.b, j);
   n.prev = qp;
   move_add_queue(n);
//   add_queue(n);
  }
 }

 cout << qp << " " << Q << endl;

 if(qp < Q)
  fout << cur.c << endl;
 else
  fout << "THE CAKE IS A LIE" << endl;
}

int main()
{
 int i;
 int NT;

 ifstream fin("input.txt");
 ofstream fout("output.txt");
 string ln;

 getline(fin, ln);
 istringstream is(ln);
 is >> NT;

 fr(i, NT)
 {
  read(fin);
  fout << "Case #" << i + 1 << ": ";
  cout << "Case #" << i + 1 << endl;
  proc(fout);
 }

 return 0;
}
