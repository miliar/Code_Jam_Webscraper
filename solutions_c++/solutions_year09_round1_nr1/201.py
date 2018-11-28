#include <string>
#include <vector>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <numeric>
#include <complex>

using namespace std;

int iterate(int n, int b) {
	int ret = 0;
  while(n > 0) {
		ret += (n % b) * (n % b);
    n /= b;
	}
	return ret;
}

bool happy(int n, int b) {
	int r = n;
  set<int> hits;

  while(r = iterate(r,b)) {
     if(hits.find(r) != hits.end()) break;
     hits.insert(r);
  }

  return (r == 1);
}

int main(void)
{
  int N;
  cin >> N;
  string line;
  getline(cin, line);
  int bases[10];
  char* cstr;
  int l,b;
  for (int c = 1; c <= N; c++) {
    getline(cin, line);
    cstr = (char*) line.c_str();
    l = strlen(cstr);
    b = (l+1)/2; //hack
    for(int i = 0; i < b; i++) {
      bases[i] = atoi(cstr);
      cstr++;
      while(*cstr == ' ' && *cstr != '0') {
        cstr++;
			}
    }

    /*for(int j = 2; j < 200; j++) {
      int s = 0;
      for(int i = 0; i < b; i++) {
        s += (happy(j,bases[i]) ? 1 : 0);
      }
      printf("%d ", s);
    }
    printf("\n");*/

		int h = 2;
    bool happiness=false;
		while(!happiness) {	
      for(int j = 0; j < b; j++) {
        happiness=true;
        if(!happy(h,bases[j])) { h++; happiness=false; break;}
			}
    }
    printf("Case #%d: %d\n", c, h);
    /*for(int i = 0; i < b; i++) {
	    printf("%d ", bases[i]);
		}
		printf("\n");*/
  }
}
