#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;
#define pb push_back
#define forn(i,n) for(int i=0; i<(n); i++)

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int ncase; scanf("%d", &ncase);
    forn(icase, ncase) {
        int n; scanf("%d", &n);
        vector<int> seq; 
        vector<bool> isb;
        forn(i, n) {
            int p; char s[4];    
            scanf("%s%d", s, &p);
            seq.pb(p);
            isb.pb(s[0]=='B');
        }
        int opos = 1, bpos = 1;
        int otm = 0, btm = 0, ctm = 0;
        forn(i, n) {
            if(isb[i]) {
                  if(seq[i] >= bpos+btm) {
                      ctm += seq[i]-bpos-btm+1;
                      otm += seq[i]-bpos-btm+1;
                  } else if(seq[i] < bpos-btm) {
                      ctm += -seq[i]+bpos-btm+1;
                      otm += -seq[i]+bpos-btm+1;
                  } else {
                      ctm += 1;
                      otm += 1;
                  }   
                  bpos=seq[i]; 
                  btm = 0;
            } else {
                   if(seq[i] >= opos+otm) {
                      ctm += seq[i]-opos-otm+1;
                      btm += seq[i]-opos-otm+1;
                  } else if(seq[i] < opos-otm) {
                      ctm += -seq[i]+opos-otm+1;
                      btm += -seq[i]+opos-otm+1;
                  } else {
                      ctm += 1;
                      btm += 1;    
                  }
                  opos=seq[i];
                  otm = 0;
            }
           // printf("ctm %d\n",ctm);
        }
        printf("Case #%d: %d\n", icase+1, ctm);
    }
}        
        
            
