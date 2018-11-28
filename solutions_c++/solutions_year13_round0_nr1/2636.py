#include <algorithm>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <memory.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<double,double> pdd;

typedef vector<int> vi;
typedef vector<pair<int, int > > vii;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef vector<ld> vld;

typedef vector<vi> vvi;
typedef vector<vii> vvii;
typedef vector<vll> vvll;
typedef vector<vs> vvs;

typedef map<int, int> mii;
typedef map<int, string> mis;
typedef map<string, int> msi;
typedef map<string, string> mss;

#define sz(a) (int)((a).size())
#define len(a) (int)((a).length())

#define all(a) (a).begin(),(a).end()
#define rall(a) (a).rbegin(),(a).rend()
#define Sort(x) sort(x.begin(),x.end())
#define Reverse(x) reverse(x.begin(),x.end())

#define forr(i,n) for (int i = 0; i < (n); ++i)
#define fori(n) forr(i,n)
#define forj(n) forr(j,n)
#define fork(n) forr(k,n)
#define forjn forj(n)
#define forjm forj(m)
#define forkm fork(m)
#define foria(a) fori(sz(a))
#define foriv foria(v)
#define foris fori(len(s))
#define forja(a) forj(sz(a))
#define forjv forj(v)
#define forjs forj(len(s))
#define FOREACH(it,x) for(__typeof((x).begin()) it=(x.begin()); it!=(x).end(); ++it)

#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)

#define read cin>>
#define write cout<<
#define writeln write endl

#define readt int aaa; read aaa;
#define gett (bbb+1)
#define fort forr(bbb,aaa)

#define issa(a,s) istringstream a(s);
#define iss(s) issa(ss,s);

ld dis(ld x, ld y) {return sqrt(x*x+y*y);}
const ld PI = acos(ld(0.0))*2;
const int INF = 1<<30;

bool is_palindrome(const string &s, int start, int end) {
  int siz = end - start + 1;
  if (siz % 2 == 0) {
    int middle = start + siz/2;
    int i;
    for (i = 0; middle - 1 - i >= 0 && middle+i <= end && s[middle-1-i] == s[middle+i]; i++);
    if (middle - i - 1 < 0 || middle+i > end)
      return true;
  } else {
    int middle = start + siz/2;
    int i;
    for (i = 1; middle - i >= 0 && middle+i <= end && s[middle-i]==s[middle+i]; i++);
    if (middle - i < 0 || middle+i > end)
      return true;
  }
  return false;
}
//Polya-Burnside theory : (n^6+3n^4+12n^3+8n^2)/24
int euclidd,euclidx,euclidy;
void extendedeuclid(int a,int b)
{
  if(b==0)
  {
    euclidd=a;
    euclidx=1;
    euclidy=0;
    return ;
  }
  extendedeuclid(b,a%b);
  int d1,x1,y1;
  d1=euclidd;
  x1=euclidx;
  y1=euclidy;
  euclidx=y1;
  euclidy=x1-((a/b)*y1);
}
double dist_2point(double x1,double y1,double x2,double y2)
{
  double d;
  d=sqrt(((x1-x2)*(x1-x2))+((y1-y2)*(y1-y2)));
  return d;
}
int binary_search(int a[],int n,int l,int u)
{
  int mid;
  if(l>u)
    return 0;
  mid=floor(l+u)/2;
  if(a[mid]==n)
    return mid;
  else if(a[mid]>n)
    return binary_search(a,n,l,mid-1);
  else
    return binary_search(a,n,mid+1,u);
}
long gcd(long a,long b)
{
  while(b>0) {
    a=a%b;
    a=a^b;
    b=b^a;
    a=a^b;
  }
  return a;
}
long lcm(long a,long b)
{
  long x=(a*b)/gcd(a,b);
  return x;
}
long is_prime(long n)
{
  long ii;
  if (n == 1)
    return 0;
  if (n == 2)
    return 1;
  if (n%2 == 0)
    return 0;
  for (ii=3;ii*ii<=n;ii=ii+2)
    if (n%ii == 0)
      return 0;
  return 1;
}
long long bigmod(long long b,long long p,long long m)
{
  if(b==0) return 0;
  long long x,power;
  x=1;
  power=b%m;
  while(p)
  {
    if(p%2==1)
      x=(x*power)%m;
    power=(power*power)%m;
    p=p/2;
  }
  return x;
}
void assert(bool b)
{
  if (!b)
    throw 0;
}
template <int n>
struct nbest
{
  vector<pair<ll, int> > p;
  nbest():p(n+1)
  {
    foria(p) p[i].first = p[i].second = -1;
  }
  void add(ll value, int key)
  {
    p[n] = make_pair(value, key);
    sort(rall(p));
  }
  ll getValue(int pos, int exceptKey = -2)
  {
    if (exceptKey == -1)
      exceptKey = -2;
    if (p[pos].second == exceptKey)
      ++pos;
    return p[pos].first;
  }
  int getKey(int pos, int exceptKey = -2)
  {
    if (exceptKey == -1)
      exceptKey = -2;
    if (p[pos].second == exceptKey)
      ++pos;
    return p[pos].second;
  }
  bool has(int pos, int exceptKey = -2)
  {
    if (exceptKey == -1)
      exceptKey = -2;
    if (p[pos].second == exceptKey)
      ++pos;
    return p[pos].second != -1;
  }
};

template <typename T>
void dumpContents(const vector<T>& v,
                  const string& msg="")
{
  cerr << "### " << msg << " ###\n";
  if (v.empty())
    return;

  for (typename vector<T>::const_iterator it=v.begin();
       it != v.end(); ++it) {
    cerr << *it << " ";
  }
  cerr << endl;
}

void printBit(ull S, int n=64){
  for(int i=n-1; i>=0; i--){
    if(S>>i & 1) cout << 1;
    else cout << 0;
  }
  cout << endl;
}

void subsetCombination(int n, int k){
  ull S = (1ULL << k) - 1ULL;
  ull E = ~((1ULL << n) - 1ULL);
  while(!(S & E)){
    printBit(S, n);
    ull smallest = S & -S;
    ull ripple = S + smallest;
    ull nsmallest = ripple & -ripple;
    S = ripple | (((nsmallest / smallest) >> 1) - 1);
  }
}

void grayCode(int n){
  int N = 1 << n;
  ull G = 0;
  for(int i=0; i<N; i++){
    G = i ^ (i >> 1ULL);
    printBit(G, n);
  }
}

int bitCount(ull n)
{
  int cnt = 0;
  while(n != 0) {
    cnt += 1;
    n &= (n-1); // the lowest 1 is turned to 0.
  }
  return cnt;
}

// ========== end of template ==========

// === global variables

int T;

typedef vector<char> Line;
typedef vector<Line> Board;


// === functions

Line lineToChars(const string& line)
{
  assert(line.size() == 4);

  Line ret;
  ret.reserve(line.size());
  fori(4) {
    ret.push_back(line[i]);
  }
  return ret;
}

Board constructBoard(const string& l1, const string& l2, const string& l3, const string& l4)
{
  Board ret;
  ret.reserve(4);
  ret.push_back(lineToChars(l1));
  ret.push_back(lineToChars(l2));
  ret.push_back(lineToChars(l3));
  ret.push_back(lineToChars(l4));

  return ret;
}


bool hasEmpty(const Board& board)
{
  bool ret = false;
  fori(4) {
    forj(4) {
      if (board[i][j] == '.') {
        return true;
      }
    }
  }
  return ret;
}

bool hasT(const Line& line)
{
  bool ret = false;
  FOREACH(it, line) {
    if (*it == 'T') {
      return true;
    }
  }
  return ret;
}

bool checkLine(const Line& line, const char& player)
{
  int count = 0;
  FOREACH(it, line) {
    if (*it == player)
      count += 1;
  }
  if (count == (hasT(line) ? 3 : 4)) {
    return true;
  } else {
    return false;
  }
}

const Line getRow(const Board& board, const int i)
{
  assert(i<=3);
  return board[i];
}

const Line getColumn(const Board& board, const int c)
{
  assert(c<=3);
  Line ret;
  ret.reserve(4);

  fori(4) {
    ret.push_back(board[i][c]);
  }
  return ret;
}

const Line getDiagonal(const Board& board, const int d)
{
  assert(d<=1);
  Line ret;
  ret.reserve(4);

  if (d==0) {
    fori(4) {
      ret.push_back(board[i][i]);
    }
  } else {
    fori(4) {
      ret.push_back(board[i][3-i]);
    }
  }
  return ret;
}

void solve(const int k, const Board& board)
{
  vector<char> players;
  players.push_back('X');
  players.push_back('O');

  FOREACH(p, players) {
    fori(4) {
      const Line line = getRow(board, i);
      if (checkLine(line, *p)) {
        cout << "Case #" << k << ": " << string(&*p, 1) << " won\n";
        return;
      }
    }
    fori(4) {
      const Line line = getColumn(board, i);
      if (checkLine(line, *p)) {
        cout << "Case #" << k << ": " << string(&*p, 1) << " won\n";
        return;
      }
    }
    fori(2) {
      const Line line = getDiagonal(board, i);
      if (checkLine(line, *p)) {
        cout << "Case #" << k << ": " << string(&*p, 1) << " won\n";
        return;
      }
    }
  }
  if (hasEmpty(board)) {
    cout << "Case #" << k << ": Game has not completed\n";
    return;
  } else {
    cout << "Case #" << k << ": Draw\n";
    return;
  }
}

int main(int argc, char** argv)
{
  ios::sync_with_stdio(false);

  {
    cin >> T;
    fori(T) {
      cin.ignore(); // skip carriage return
      string l1,l2,l3,l4;
      cin >> l1;
      cin.ignore();
      cin >> l2;
      cin.ignore();
      cin >> l3;
      cin.ignore();
      cin >> l4;
      cin.ignore();

      const Board board = constructBoard(l1,l2,l3,l4);
      solve(i+1, board);
    }
  }

  return 0;
}
