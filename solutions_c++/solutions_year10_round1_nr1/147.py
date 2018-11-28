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
#include <cstring>

using namespace std;

#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x).size())
#define pb push_back
#define fr(i, n) for(i = 0; i < (n); i++)
#define frr(i, n) for(int i = 0; i < (n); i++)

typedef long long ll;
#define mp make_pair
typedef vector<int> VI;
typedef vector<string> VS;
typedef istringstream ISS;
typedef ostringstream OSS;
#define _cl(x) memset(x, 0, sizeof(x))
#define _rs(x) memset(x, -1, sizeof(x))

int _mx[] = {0, 1, 1, -1};
int _my[] = {1, 0, 1, 1};

int N, K;
string a[100];

void read(ifstream &fin)
{
 fin >> N >> K;

 frr(r, N)
  fin >> a[r];
}

char getrc(int r, int c) {
 if(r < 0 || c < 0 || r >= N || c >= N)
  return '.';

 return a[r][c];
}

bool win(char w) {
 frr(r, N) frr(c, N) {
  frr(d, 4) {
   int k;

   for(k = 0; k < K; ++k)
    if(getrc(r + _my[d] * k, c + _mx[d] * k) != w)
     break;

   if(k == K)
    return true;
  }
 }

 return false;
}

void proc(ofstream &fout)
{
 frr(r, N) frr(i, N) frr(c, N - 1)
  if(a[r][c] != '.' && a[r][c + 1] == '.') {
    a[r][c + 1] = a[r][c];
    a[r][c] = '.';
  }

 bool red = win('R');
 bool blue = win('B');

 if(red && blue)
  fout << "Both";
 else if(red)
  fout << "Red";
 else if(blue)
  fout << "Blue";
 else
  fout << "Neither";

 fout << endl;
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
