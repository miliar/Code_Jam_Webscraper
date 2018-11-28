#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <cstring>
#include <cctype>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <fstream>

using namespace std;

#define s(n) scanf("%d",&n)
#define sc(n) scanf("%c",&n)
#define sl(n) scanf("%lld",&n)
#define sf(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)

#define pb push_back
#define mp make_pair
#define gcd __gcd
#define bitcount __builtin_popcount

#define rep(i, n) for(int i=0;i<(n);i++)
#define forall(i,a,b) for(int i=(a);i<(b);i++)
#define foreach(it,c) for(typeof((c).begin()) it=(c).begin() ;it!=(c).end();++it)
#define all(a) (a).begin(), (a).end()
#define in(a,b) ((b).find(a) != (b).end())
#define fill(a,v) memset((a), (v), sizeof (a))
#define sz(a) ((int)((a).size()))

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef vector<string> vs;
typedef pair<int,int> ii; 

char board[4][4];

int main(void)
{
  int t, p1, p2, w1, w2, dots;
  char c;
  ifstream fin;
  ofstream fout;
  fin.open("3.in");
  fout.open("3.out");
  fin >> t;
  rep(k, t){
    w1 = w2 = 0;
    dots = 0;
    rep(i, 4){
      rep(j, 4){
	fin >> board[i][j];
	if (board[i][j] == '.'){
	  dots++;
	}
      }
    }
    cout << endl;
    rep(i, 4){
      rep(j, 4)
	cout << board[i][j];
      cout << endl;
    }
    cout << endl;
    rep(i, 4){
      p1 = p2 = 0;
      rep(j, 4){
	if (board[i][j] == 'X')
	  p1++;
	else if (board[i][j] == 'O')
	  p2++;
	else if (board[i][j] == 'T'){
	  p1++;
	  p2++;
	}
      }
      if (p1 == 4)
	w1 = 1;
      if (p2 == 4)
	w2 = 1;
    }

    rep(i, 4){
      p1 = p2 = 0;
      rep(j, 4){
	if (board[j][i] == 'X')
	  p1++;
	else if (board[j][i] == 'O')
	  p2++;
	else if (board[j][i] == 'T'){
	  p1++;
	  p2++;
	}
      }
      if (p1 == 4)
	w1 = 1;
      if (p2 == 4)
	w2 = 1;
    }

    p1 = p2 = 0;
    rep(i, 4)
      if (board[i][i] == 'X')
	p1++;
      else if (board[i][i] == 'O')
	p2++;
      else if (board[i][i] == 'T'){
	p1++;
	p2++;
      }
      if (p1 == 4)
	w1 = 1;
      if (p2 == 4)
	w2 = 1;
      
    p1 = p2 = 0;
    rep(i, 4)
      if (board[i][3 - i] == 'X')
	p1++;
      else if (board[i][3 - i] == 'O')
	p2++;
      else if (board[i][3 - i] == 'T'){
	p1++;
	p2++;
      }
    
    if (p1 == 4)
      w1 = 1;
    if (p2 == 4)
      w2 = 1;

    fout << "Case #" << k + 1 << ": ";
    
    if (w1 && w2)
      fout << "Draw\n";
    else if (w1)
      fout << "X won\n";
    else if (w2)
      fout << "O won\n";
    else if (!dots)
      fout << "Draw\n";
    else
      fout << "Game has not completed\n";
      
  }
  fout.close();
  fin.close();
  return 0;
}
