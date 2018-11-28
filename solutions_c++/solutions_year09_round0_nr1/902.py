#include<iostream>
#include<cstring>
using namespace std;

const int maxd = 5000;
const int maxn = 500;
int l;
int n;
int d;

string cand[maxn+4];
int stk[18][28];
int stk1[18];
int trie[maxd*15+3][3];
int tn;
int ans;

void insrt(string st)
{
  int t = 0;
  int t1 = 0;
  int r = 2;
  t = trie[t][2];
  for (int i = 0; i < l; ++i) {
    while ((t != -1) && (trie[t][0] < st[i]-'a')) {
      t1 = t;
      r = 1;
      t = trie[t][1];
    }
    if ((t == -1) || (trie[t][0] != st[i]-'a')) {
      trie[tn][0] = st[i]-'a';
      trie[tn][1] = t;
      trie[tn][2] = -1;
      trie[t1][r] = tn;
      t = tn;
      ++tn;      
    }
    t1 = t;
    t = trie[t][2];
    r = 2;
  }
}

void init()
{
  string st;
  tn = 1;
  trie[0][0] = -1;
  trie[0][1] = -1;
  trie[0][2] = -1;
  for (int i = 0; i < d; ++i) {
    cin >> st;
    insrt(st);
  }
  //for (int i = 0; i < tn; ++i) {
  //  cout << trie[i][0] << ' ' << trie[i][1] << ' ' << trie[i][2] << endl;
  //}
  //cout << tn << endl;
}

void dfs(int k, int pre)
{
  int cur;
  int pt;
  for (int i = 0; i < stk[k][0]; ++i) {
    cur = stk[k][i+1];
    pt = trie[pre][2];
    while (pt != -1) {
      if (trie[pt][0] == cur) break;
      pt = trie[pt][1];
    }
    if (pt != -1) {
      if (k == l-1) ++ans;
      else dfs(k+1, pt);
    }
  }
  //cout << k;
}

void proc()
{
  string st;
  cin >> st;
  int t = 0;
  for (int i = 0; i < l; ++i) {
    if (st[t] != '(') {
      stk[i][0] = 1;
      stk[i][1] = st[t]-'a';
    } else {
      ++t;
      stk[i][0] = 0;
      while (st[t] != ')') {
	++stk[i][0];
	stk[i][stk[i][0]] = st[t]-'a';
	++t;
      }
    }
    ++t;
  }
  ans = 0;
  dfs(0, 0);
}

int main()
{
  cin >> l >> d >> n;
  init();
  for (int i = 0; i < n; ++i) {
    cout << "Case #" << i+1 << ": ";
    proc();
    cout << ans << endl;
  }
  return 0;
}
