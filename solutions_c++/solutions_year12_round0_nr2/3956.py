#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define sz(x) ((int) (x).size())
#define forn(var, lim) for(int var=0; var<lim; var++)
#define all(x) (x).begin(), (x).end()
#define abs(x) ((x)>=0 ? (x) : -(x))
#define inf64 1000000000000000001LL
#define min(a,b) (a<b)? a:b

using namespace std;



int main(int argc, char **argv) {
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w+", stdout);
 // freopen("dance.in", "r", stdin);
 // freopen("dance.out", "w+", stdout);
  int tt;
  int* t = new int[110];
  int m=0, n, p, s, sum=0, s4et=0;
  scanf("%d\n", &tt);
    for(int i=0; i<tt; i++){
      scanf("%d%d%d", &n, &s, &p);
      if (p>1) 	m=3*p-4;
      //else if (p==1) m=1;
        forn (j, n)  scanf ("%d", &t[j]);
	switch (p) {
	  case 0: sum=n; break;
	  case 1: forn (j, n)  if (t[j]!=0) sum++; break;
	  default:
	    forn (j, n){
	      if((t[j]==m)||(t[j]==m+1)) s4et++;
	      else if(t[j]>m) sum++;
	    }
	    sum+=min(s4et,s);
	  break;
	}
    
      printf("Case #%d: %d\n", i+1, sum);
	sum=0; s4et=0; m=0;
    }
    
	
    
  return 0;
}

 
