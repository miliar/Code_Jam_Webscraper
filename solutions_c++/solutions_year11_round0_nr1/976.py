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

int main()
{
  int tn;
  scanf("%d", &tn);
  for (int tt = 1; tt <= tn; tt++)
  {
    fprintf(stderr, "%d\n", tt);
    printf("Case #%d: ", tt);

	int d;
    scanf("%d ", &d);
    for(int i=0;i<d; i++)
      scanf("%c %d ", &r[i], &p[i]);

	int ot=0;
	int bt=0;
	int op=1;
	int bp=1;

	for(int i=0;i<d;i++){
		if(r[i]=='O'){
			ot+=abs(p[i]-op);
			ot=max(ot,bt);
			ot++;
			op=p[i];
		}else{
			bt+=abs(p[i]-bp);
			bt=max(ot,bt);
			bt++;
			bp=p[i];
		}
	}
	printf("%d\n", max(ot,bt));

  }
  return 0;
}

