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

int vv[1000];
double mem[1000] = {0};

double calc(int c){
	if(mem[c]!=0) return mem[c];
	double res;
	if(c==2) res = 2.0;
	else if(c==3) res = 3.0;
	else res = 2.0 * calc(c-2);
	
	mem[c]=res;
	return res;
}

int main()
{
  int tn;
  scanf("%d", &tn);
  for (int tt = 1; tt <= tn; tt++)
  {
    fprintf(stderr, "%d\n", tt);
    printf("Case #%d: ", tt);

	int c;
	scanf("%d", &c);
	int wrong = 0;
    for(int i=0;i<c; i++){
      scanf("%d ", &vv[i]);
	  if(vv[i]!=(i+1)){
		  wrong ++;
	  }
	}
	
	double res = wrong;
	//calc(wrong);
	printf("%f\n", res);
	
  }
  return 0;
}

