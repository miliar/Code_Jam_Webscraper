#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

int recycled(char *num, int A, int B, int size);
void add_one(char *num, int size);

int main(int argc, char *argv[]) {

  int T, A, B;
  char nA[8], nB[8], aux[8];

  //Read number of test cases
  scanf("%d", &T);
  for(int t=1; t<=T; t++) {

    //Read numbers in string format
    scanf("%s %s", nA, nB);

    A = atoi(nA);
    B = atoi(nB);
    int size=strlen(nA);

    //Compute recycled numbers
    int res=0;
    for(int i=A; i<B; i++) {
      res += recycled(nA,i,B,size);
      add_one(nA,size);
    }

    //Print solution
    printf("Case #%d: %d\n", t, res);
  }

  return 0;
}

void add_one(char *num, int size) {
  for(int i=size-1; i>=0; i--) {
    if( num[i] == '9' )
      num[i] = '0';
    else {
      num[i]++;
      break;
    }
  }
}

int recycled(char *num, int A, int B, int size) {
  vector<int> recy;
  char aux[8];

  for(int i=1; i<size; i++) {
    if( num[i] == '0' ) continue;
    for(int j=0; j<size; j++)
      aux[j] = num[(i+j)%size];
    aux[size] = 0;

    int x = atoi(aux);
    if( x > A && x <= B ) {
      //printf("%s %s OK\n", num, aux);
      recy.push_back(x);
    }
    //else printf("%s %s\n", num, aux);
  }

  sort(recy.begin(),recy.end());
  vector<int>::iterator it = unique(recy.begin(), recy.end());

  recy.resize( it - recy.begin() );

  return (int)recy.size();
}
