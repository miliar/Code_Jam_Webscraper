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

int N, M;
string words[10010];
string lists[110];

vector<int> chars[10010][26];
int wsize[10010];

int used[2][10010];
int ulen[2];

void read()
{
 cin >> N >> M;
 frr (i, N) {
  cin >> words[i];
 }
 frr (i, M) {
  cin >> lists[i];
 }
}

bool compare(vector<int> &a, vector<int> &b) {
 if (sz(a) != sz(b))
  return false;
 frr (i, sz(a))
  if (a[i] != b[i])
   return false;
 return true;

}

int getPoints(int wordPos, string list) {
 int cur, tar;
 int points = 0;
 int p = 0;
 char ch;
 bool found;

 ulen[0] = 0;
 frr (i, N) {
  if (wsize[i] == wsize[wordPos]) {
   used[0][ulen[0]++] = i;
  }
 }

 cur = 0; tar = 1;
 while (ulen[cur] > 1) {

  ch = list[p++]-'a';
  found = false;

  ulen[tar] = 0;
  frr (i, ulen[cur]) {
   if (sz(chars[used[cur][i]][ch])) {
    found = true;
   }
  }
  if (!found)
   continue;

  if (sz(chars[wordPos][ch])) {
   frr (i, ulen[cur]) {
    if (compare(chars[used[cur][i]][ch], chars[wordPos][ch])) {
     used[tar][ulen[tar]++] = used[cur][i];
    }
   }
  } else {
   points++;
   frr (i, ulen[cur]) {
    if (sz(chars[used[cur][i]][ch]) == 0) {
     used[tar][ulen[tar]++] = used[cur][i];
    }
   }
  }

  tar = cur;
  cur = (cur+1)%2;
 }
 return points;
}

int getBestWord(string list) {
 int best = -1, bestPos = -1;
 frr (i, N) {
  int temp = getPoints(i, list);
  if (temp > best) {
   best = temp;
   bestPos = i;
  }
 }
 return bestPos;
}

void init() {
 _cl(chars);
 int len;
 frr (i, N) {
  wsize[i] = sz(words[i]);
  frr (j, wsize[i]) {
   chars[i][words[i][j]-'a'].pb(j);
  }
 }
}

void proc()
{
 init();
 frr (i, M) {
  cout << " " <<  words[getBestWord(lists[i])];
 }
 cout << endl;
}

int main()
{
	int T;

	cin >> T;

	frr(i, T)
	{
		read();
  cout << "Case #" << (i+1) << ":";
		proc();
	}

	return 0;
}

