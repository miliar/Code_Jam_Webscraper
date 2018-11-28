#include <cstdio>
#include <map>
#include <set>
#include <cstring>

using namespace std;

#define pcc pair<char,char>
#define mp(A,B) make_pair(A,B)

int main(){
  int t, c, d, n;
  map< pcc,char> comb;
  set< pcc> opp;
  char pilha[111];
  int tp;
  int freq[30];
  char invoke[111];

  scanf("%d", &t);
  for (int ka = 1; ka <= t; ka++){
    comb.clear();
    opp.clear();
    tp = 0;
    memset(freq, 0, sizeof(freq));
    
    scanf("%d", &c);
    for (int i = 0; i < c; i++){
      char s[10];
      scanf("%s", s);
      comb.insert(mp(mp(s[0],s[1]),s[2]));
      comb.insert(mp(mp(s[1],s[0]),s[2]));
    }

    scanf("%d", &d);
    for (int i = 0; i < d; i++){
      char s[10];
      scanf("%s", s);
      opp.insert(mp(s[0],s[1]));
      opp.insert(mp(s[1],s[0]));
    }
    
    scanf("%d", &n);
    scanf("%s", invoke);
    for (int i = 0; i < n; i++){
      pilha[tp++] = invoke[i];
      freq[invoke[i]-'A']++;
      //printf("in %c\n", invoke[i]);
      while (tp > 1 && comb.count(mp(pilha[tp-1],pilha[tp-2])) > 0){
	//printf("comb %c %c -> %c\n", pilha[tp-1],pilha[tp-2],comb[mp(pilha[tp-1],pilha[tp-2])]);
	freq[pilha[tp-1]-'A']--;
	freq[pilha[tp-2]-'A']--;
	pilha[tp-2] = comb[mp(pilha[tp-1],pilha[tp-2])];
	tp--;
	freq[pilha[tp-1]-'A']++;
      }
      if (tp > 1){
	for (char pres = 'A'; pres <= 'Z'; pres++){
	  if (freq[pres-'A'] > 0 && opp.count(mp(pilha[tp-1],pres)) > 0){
	    //printf("clear\n");
	    tp = 0;
	    memset(freq,0,sizeof(freq));
	    break;
	  }
	}
      }
      
    }
    printf("Case #%d: [", ka);
    if (tp > 0)
      printf("%c", pilha[0]);
    for (int i = 1; i < tp; i++){
      printf(", %c", pilha[i]);
    }
    printf("]\n");
  }

  return 0;
}
