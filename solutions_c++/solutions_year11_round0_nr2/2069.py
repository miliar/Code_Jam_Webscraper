#include<cstdio>
#include<deque>

using namespace std;

int main()
{
  int T;
  scanf("%d", &T);
  for(int C=1; C<=T; ++C) {
    int cb[26][26] = {{0}};
    int op[26][26] = {{0}};
    int c, d, n;
    scanf("%d", &c);
    while(c--) {
      char t[8];
      scanf("%s", t);
      cb[t[0]-'A'][t[1]-'A'] = cb[t[1]-'A'][t[0]-'A'] = t[2];
    }
    scanf("%d", &d);
    while(d--) {
      char t[8];
      scanf("%s", t);
      op[t[0]-'A'][t[1]-'A'] = op[t[1]-'A'][t[0]-'A'] = 1;
    }
    scanf("%d", &n);
    char s[128];
    scanf("%s", s);
    deque<char> q;
    for(int i=0; i<n; ++i) {
      if(q.empty()) q.push_back(s[i]);
      else {
	char ch;
	if((ch = cb[q.back()-'A'][s[i]-'A']) != 0) {
	  q.pop_back();
	  q.push_back(ch);
	} else {
	  for(int j=0; j<(int)q.size(); ++j)
	    if(op[q[j]-'A'][s[i]-'A'] == 1)
	      q.clear();
	  if(!q.empty()) q.push_back(s[i]);
	}
      }
    }
    printf("Case #%d: [", C);
    for(int i=0; i<(int)q.size(); ++i) {
      putchar(q[i]);
      if(i != (int)q.size()-1) printf(", ");
    }
    puts("]");
  }
  return 0;
}
