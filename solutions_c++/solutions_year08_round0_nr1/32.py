// NigelTufnel
// start 20:26

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void chomp(char *s) {
  while(strlen(s)>0 && s[strlen(s)-1] < 32)
    s[strlen(s)-1] = 0;
}
	 
int sindex(vector<string> & engs, string & x) {
  int i;
  for(i=0;i<engs.size();i++)
    if (engs[i] == x ) return i;
  return -1;
}

void best(vector<int> & qi, int nengs, int from, int &b, int &ni) {
  vector<int> c;

  int i, left;

  b = 0;
  ni = from;

  for(i=0;i<nengs;i++)
    c.push_back(0);

  left = nengs;
  for(i=from;i<qi.size();i++) {

    if (qi[i] >= 0) c[qi[i]]++;
    if (c[qi[i]] == 1) left--;
    if (left == 0) {
      b = qi[i];
      ni = i;
      return;
    }
  }
  for(i=0;i<nengs;i++)
    if (c[i]==0) {
      b = i;
      ni = qi.size();
      return;
    }

}

void solve(int index) {
  vector<string> engs, qs;
  vector<int> sol, qi;
  char line[512];
  int i, ns, nq, w, s, b, ni;

  fgets(line,512,stdin); chomp(line); ns = atoi(line);

  for(i=0;i<ns;i++) {
    fgets(line,512,stdin);
    chomp(line);
    engs.push_back(string(line));
  }

  fgets(line,512,stdin); chomp(line); nq = atoi(line);
    
  for(i=0;i<nq;i++) {
    fgets(line,512,stdin);
    chomp(line);
    qs.push_back(string(line));
  }

  for(i=0;i<nq;i++)
    qi.push_back(sindex(engs, qs[i]));

  //  printf ("S=%d Q=%d\n",ns,nq);
  
  s = 0;
  w = 0;
  while(w<qi.size()) {
    best(qi,engs.size(),w,b,ni);
    w = ni;
    if (w!=qi.size()) s++; // switch;
  }

  printf("Case #%d: %d\n",index,s);
}

int main(int argc, char **argv) {
  char line[512];
  int i,n;

  fgets(line,512,stdin);
  chomp(line);
  
  n = atoi(line);
  for(i=0;i<n;i++) {
    solve(i+1);
  }


  return 0;
}
