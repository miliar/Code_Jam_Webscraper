#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib> 
using namespace std;
 
#define FOR(i,n) for (long (i)=0; (i)<(n); (i)++)
#define pb push_back 
#define SET(a,k) memset((a),(k),sizeof((a)))
 
struct Paint
{
  int A, B;
  int C;
  
  Paint(int _a, int _b, int _c):A(_a), B(_b), C(_c){} 
  friend bool operator<(const Paint &a, const Paint &b)
  {
    return a.A < b.A;
  }
};
 
const long MaxN = 305; 
 
FILE *fin, *fout; 
 
int dp[MaxN][MaxN][MaxN];
bool flag[MaxN][MaxN][MaxN];
long n;

map<string, int> name;
int nameCnt;

vector<Paint> boja;

int memoiz(int prev, int c1, int c2)
{
  if (boja[prev].B + 1 == 10001) return 0;
  else if (flag[prev][c1][c2]) return dp[prev][c1][c2];
  else
  {
    int best = -1;
    for (int i = prev + 1; i < boja.size(); i++)
    {
      if (boja[i].A > boja[prev].B + 1) break;
      
      if (boja[i].B > boja[prev].B)
      {
        int novo = -1;
        if (boja[i].C == boja[prev].C) novo = memoiz(i, c1, c2);
        else if (boja[i].C == c1 || c1 == 0) novo = memoiz(i, boja[prev].C, c2);
        else if (boja[i].C == c2 || c2 == 0) novo = memoiz(i, c1, boja[prev].C);
                  
        if (novo == -1) continue;
        novo++;
        if (novo < best || best == -1) best = novo;
      }      
    }
    
    flag[prev][c1][c2] = true;
    dp[prev][c1][c2] = best;
    return best;
  }
}

void solve(int t)
{  
  cout << t << endl;
  sort(boja.begin(), boja.end()); 
  SET(flag, 0);
  int best = -1;
  for (int i = 0; i < boja.size(); i++)
  {
    if (boja[i].A == 1)
    {
      int ajde = memoiz(i, 0, 0);
      if (ajde != -1)
      {
        ajde++;
        if (ajde < best || best == -1) best = ajde;
      }
    }
  }
  
  if (best == -1) fprintf(fout, "Case #%d: IMPOSSIBLE\n", t);
  else fprintf(fout, "Case #%d: %d\n", t, best);
}

void input()
{
  nameCnt = 0;
  name.clear();
  boja.clear();
  
  fscanf(fin, "%ld\n", &n);
  for (int i = 0; i < n; i++)
  {
    char str[15];
    int a, b;
    
    fscanf(fin, "%s %d %d\n", &str, &a, &b);
    string s = str;        
    
    int myb = 0;
    if (name[str] == 0)
    {
      nameCnt++;
      name[str] = nameCnt;
      myb = nameCnt;
    }
    else
      myb = name[str];
    
    boja.push_back(Paint(a, b, myb));
  }
}

int main()
{
  fin = fopen("B-large.in", "r");
  fout = fopen("B_large.out", "w");
  
  long test;
  fscanf(fin, "%ld", &test);
  
  for (long t = 1; t <= test; t++)
  {
    input();
    solve(t);        
  }  
  
  fclose(fin);
  fclose(fout);
  
  system("pause");
  return 0;
  
}
