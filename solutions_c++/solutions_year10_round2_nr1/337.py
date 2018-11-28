/* 
 * File:   main.cpp
 * Author: tanaeem
 *
 * Created on May 22, 2010, 10:33 PM
 */

#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <string.h>
#include <map>
using namespace std;

map<string, int> mp;

int trie[5100][5100];
int sz;
char buf[100000];

int create()
{
  memset(trie[sz], -1, sizeof (trie[sz]));
  sz++;
  return sz - 1;
}

int insert(int ps, int cr=0)
{
  if (buf[ps] == 0)return 0;
  ps++;
  string s="";
  while (buf[ps] && buf[ps] != '/')
  {
    s+=buf[ps];
    ps++;
  }
  if (mp.find(s) == mp.end())
  {
    int k=mp.size();
    mp[s]=k;
  }
  int r=0;
  int n=mp[s];
  if (trie[cr][n] == -1)
  {
    r++;
    trie[cr][n]=create();
  }
  return r + insert(ps, trie[cr][n]);
}

int main()
{
  freopen("A.in", "r", stdin);
  freopen("A1.op", "w", stdout);
  int t;
  scanf("%d", &t);
  for (int cs=1; cs <= t; cs++)
  {
    mp.clear();
    sz=1;
    memset(trie[0], -1, sizeof (trie[0]));
    int n, m;
    scanf("%d%d", &n, &m);
    for (int i=0; i < n; i++)
    {
      scanf("%s", buf);
      insert(0);
    }
    int sln=0;
    for (int i=0; i < m; i++)
    {
      scanf("%s", buf);
      sln+=insert(0);
    }
    printf("Case #%d: %d\n", cs, sln);
  }

  return (0);
}

