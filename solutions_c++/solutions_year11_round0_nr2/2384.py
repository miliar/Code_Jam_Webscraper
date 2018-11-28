#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <iomanip>
#include <cstdio>

using namespace std;

#define PRINT(x) cout << "DEBUG " << #x << " = " << x <<  endl;

#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x).size())
#define pb push_back
#define mp make_pair
#define fr(i, n) for(i = 0; i < (n); i++)
#define frr(i, n) for(int i = 0; i < (n); i++)
#define _cl(x) memset(x, 0, sizeof(x))
#define _rs(x) memset(x, -1, sizeof(x))

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef istringstream ISS;
typedef ostringstream OSS;
typedef long long ll;

char _base[8] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};
int _baseIndex[26];
bool D[8][8];
map<string, char> C;
int oldbase[8];

bool isbase(char ch) { 
 frr (i, 8)
  if (ch == _base[i])
   return true;
 return false;
}

void init() {
 _baseIndex['Q'-'A'] = 0;
 _baseIndex['W'-'A'] = 1;
 _baseIndex['E'-'A'] = 2;
 _baseIndex['R'-'A'] = 3;
 _baseIndex['A'-'A'] = 4;
 _baseIndex['S'-'A'] = 5;
 _baseIndex['D'-'A'] = 6;
 _baseIndex['F'-'A'] = 7;
}

vector<char> read()
{ 
 int clen, dlen;
 string st, st2;
 _cl(D);
 C.clear();

 cin >> clen;
 frr (i, clen) {
  cin >> st;
  st2 = "  ";
  st2[0] = st[0]; st2[1] = st[1];
  C[st2] = st[2];
  st2[1] = st[0]; st2[0] = st[1];
  C[st2] = st[2];
 }
 
 cin >> dlen;
 frr (i, dlen) {
  cin >> st;
  D[_baseIndex[st[0]-'A']][_baseIndex[st[1]-'A']] = true;
  D[_baseIndex[st[1]-'A']][_baseIndex[st[0]-'A']] = true;
 }

 _cl(oldbase);
 vector<char> res;
 string st3;
 int N;
 cin >> N;
 cin >> st;
 frr (i, N) {
  if (sz(res)>0 && isbase(st[i])) {
   st2 = "  ";
   st2[0] = res[sz(res)-1]; st2[1] = st[i];

   if (C.find(st2) != C.end()) {
    res.pop_back();
    res.pb(C[st2]);
    oldbase[_baseIndex[st2[0]-'A']]--;
    continue;
   } else {
    bool found = false;
    frr (j,8)
     if (oldbase[j] && D[j][_baseIndex[st[i]-'A']]) {
      _cl(oldbase);
      res.clear();
      found = true;
      break;
     }
    if (found) continue;
   }
  }
  if (isbase(st[i])) {
    oldbase[_baseIndex[st[i]-'A']]++;
  }
  res.pb(st[i]);
 }
 return res;
}




int main()
{
	int T;

	
 init();
 cin >> T;

	frr(i, T)
	{
		vector<char> res = read();
  cout << "Case #" << i+1 << ": [";
  frr (i, sz(res)) {
   if (i!=0) cout << ", ";
   cout << res[i];
  }
  cout << "]" << endl;
	}

	return 0;
}

