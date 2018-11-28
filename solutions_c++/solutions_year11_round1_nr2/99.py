#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <climits>
#include <algorithm>

using namespace std;

const int MAXN = 10000;

string L,D[MAXN];
bool ok[MAXN];
int n,m,co[26];

/*
int calc(int x) {
  memset(ok,1,sizeof(ok));
  memset(co,0,sizeof(co));
  int ret = 0,del = 0;
  int l = D[x].size();
  for (int i = 0; i<n; i++)
    if (D[i].size()!=l) {
      ok[i] = 0;
      del++;
    }
    else {
      for (int j = 0; j<l; j++)
        co[D[i][j]-'a']++;
    }
  if (del==n-1) return ret;
  for (int _k = 0; _k<26; _k++) {
    int k = L[_k]-'a';
    if (co[k]>0) {
      bool have = 0;
      for (int i = 0; i<l; i++)
        if (D[x][i]==k+'a') {
          have = 1;
          break;
        }
      if (!have) ret--;
      for (int i = 0; i<n; i++)
        if (ok[i]) {
          for (int j = 0; j<l; j++)
            if (D[x][j]==k+'a' && D[i][j]!=k+'a' || D[x][j]!=k+'a' && D[i][j]==k+'a') {
              ok[i] = 0;
              del++;
              for (int u = 0; u<l; u++)
                co[D[i][u]-'a']--;
              break;
            }
        }
      if (del==n-1) return ret;
    }
  }
}
*/

struct node {
  bool del;
  int id;
  string md,st;
};

bool cmp(const node &p,const node &q) {
  if (p.del!=q.del) return !p.del;
  if (p.st.size()!=q.st.size()) return p.st.size()<q.st.size();
  return p.md<q.md;
}

node dic[MAXN];
int val[MAXN];

void solve() {
  for (int i = 0; i<n; i++) {
    dic[i].del = 0;
    dic[i].md = "";
    for (int j = 0; j<D[i].size(); j++)
      dic[i].md += ' ';
    dic[i].st = D[i];
    dic[i].id = i;
  }
  memset(val,0,sizeof(val));
  for (int g = 0; g<26; g++) {
    int G = L[g];
    sort(dic,dic+n,cmp);
    /*for (int i = 0; i<n; i++) {
        printf("%d %d %s %s\n",val[dic[i].id],dic[i].del,dic[i].md.c_str(),dic[i].st.c_str());
    }*/
    for (int i = 0; i<n && !dic[i].del; ) {
      int j = i;
      while (j+1<n && dic[j+1].md==dic[i].md) j++;
      if (i==j) {
        dic[i].del = 1;
        i = j+1;
        continue;
      }
      bool have = 0;
      for (int k = i; k<=j && !have; k++) {
        for (int l = 0; l<dic[k].st.size() && !have; l++)
          if (G==dic[k].st[l])
            have = 1;
      }
      if (!have) {
        i = j+1;
        continue;
      }
      for (int k = i; k<=j; k++) {
        bool have = 0;
        for (int l = 0; l<dic[k].st.size(); l++)
          if (dic[k].st[l]==G) {
            have = 1;
            dic[k].md[l] = G;
          }
        if (!have) val[dic[k].id]--;
      }
      i = j+1;
    }
  }
  int mmin = INT_MAX,k;
  for (int i = 0; i<n; i++)
    if (val[i]<mmin) {
      mmin = val[i];
      k = i;
    }
  printf(" %s",D[k].c_str());
}

int main() {
  freopen("B.in","r",stdin);
  freopen("B.out","w",stdout);
  int ntest;
  cin>>ntest;
  for (int loop = 1; loop<=ntest; loop++) {
    printf("Case #%d:",loop);
    cin>>n>>m;
    for (int i = 0; i<n; i++)
      cin>>D[i];
    for (int j = 0; j<m; j++) {
      cin>>L;
      solve();
    }
    printf("\n");
  }
  return 0;
}
