#include "stdafx.h"
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>

#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <functional>
#include <map>
#include <set>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define pb push_back
#define mp make_pair

char r[100];
int p[100];

bool pop(std::vector<char>& s, map<char, map<char, char>>& cc, char c){
	if(s.empty())
		return false;
	if(cc.find(c)==cc.end())
		return false;
	map<char, char>& x = cc[c];
	char b = s[s.size()-1];
	if(x.find(b)==x.end())
		return false;
	return true;
}

int main()
{
  int tn;
  scanf("%d", &tn);
  for (int tt = 1; tt <= tn; tt++)
  {
    fprintf(stderr, "%d\n", tt);
    printf("Case #%d: ", tt);

	map<char, map<char, char>> cc;
	int c;
    scanf("%d ", &c);
    for(int i=0;i<c; i++){
		char c1, c2, c3;
      scanf("%c%c%c ", &c1, &c2, &c3);
	  cc[c1][c2]=c3;
	  cc[c2][c1]=c3;
	}

	map<char, map<char, bool>> dd;
	int d;
	scanf("%d ", &d);
    for(int i=0;i<d; i++){
		char d1, d2;
      scanf("%c%c ", &d1, &d2);
	  dd[d1][d2] = true;
	  dd[d2][d1] = true;
	}

	std::vector<char> s;
	int n;
	scanf("%d ", &n);
    for(int i=0;i<n; i++){
      char c;
      scanf("%c", &c);
	  while(pop(s, cc, c)){
		  c=cc[c][s.back()];
		  s.pop_back();
	  }
	  bool explode=false;
	  for(int j=0;j<s.size();j++){
		  if(dd[c][s[j]]){
			  explode=true;
			  break;
		  }
	  }
	  if(explode){
		  s.clear();
	  }else{
		s.push_back(c);
	  }
	}

	printf("[");
	for(int i=0;i<s.size();i++){
		if(i!=0) printf(", ");
		printf("%c", s[i]);
	}
	printf("]\n");

  }
  return 0;
}

