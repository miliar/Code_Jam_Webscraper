#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

#define MAX 1
#define INF 0x3f3f3f3f
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) (a).begin(),a.end()
#define SORT(a) sort(ALL(a))
#define SZ(a) ((int) a.size())
#define pb push_back
#define sb substr
#define wr(a) cout << (a) << endl
#define Abs(x) (((x)< 0) ? (-(x)) : (x))
#define CMP(a, b) (a).compare((b))


char linha[150];
int i;
vector<int> vet;
int main (void){
  int n;
  int teste = 1;
  gets(linha);
  sscanf(linha, "%d", &n);
  while(n--){
    gets(linha);
    vet.clear();
    for(i=0;i<strlen(linha);i++){
      vet.pb(linha[i]-'0');
    }
    vector<int> temp = vet;
    SORT(temp);
    int ind;
    for(i=0;i<SZ(temp);i++){
      if(temp[i] > 0 ){
	ind = i;
	break;
      }
    }
    printf("Case #%d: ", teste++);
    if( next_permutation(vet.begin(), vet.end())){
      FOR(i,0,SZ(vet)){
	printf("%d", vet[i]);
      }
      printf("\n");
    }
    else{
      printf("%d", temp[ind]);
      FOR(i,0,SZ(temp)){
	if(i==ind) {
	  printf("0");
	  continue;
	}
	printf("%d", temp[i]);
      }
      printf("\n");
    }
  }
   return 0;
}