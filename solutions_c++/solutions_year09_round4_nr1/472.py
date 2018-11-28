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
#define fr2(i, s, n) for(i = (s); i < (n); i++)

typedef long long ll;
#define mp make_pair
typedef vector<int> VI;
typedef vector<string> VS;
typedef istringstream ISS;
typedef ostringstream OSS;
#define _cl(x) memset(x, 0, sizeof(x))
#define _rs(x) memset(x, -1, sizeof(x))

int N;
int a[100];

void read(ifstream &fin)
{
 int i, j;
 string s;

 fin >> N;

 fr(i, N)
 {
  fin >> s;

  a[i] = 0;

  fr(j, N)
   if(s[j] == '1')
    a[i] = j;
 }
}

void proc(ofstream &fout)
{
 int res = 0;
 int i, j, k;

 fr(i, N)
 {
  for(j = i; j < N; j++)
   if(a[j] <= i)
    break;

  res += j - i;
  
  for(k = j - 1; k >= i; --k)
   swap(a[k], a[k + 1]);
 }

 fout << res << endl;
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
