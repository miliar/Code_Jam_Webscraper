#include <iostream>
#include <string>
using namespace std;
string codejam,aux = "welcome to code jam";
int solve(int cur, int lcur);
int main() {
  int N,i;
  scanf("%d",&N);
  getchar();
  for (i = 1 ; i <= N ; i++) {
    getline(cin,codejam);
    printf("Case #%d: %04d\n",i,solve(0,0)%10000);
  }
}
int solve(int cur, int lcur) {
  if (cur == codejam.size()) return 0;
  int i;
  for (i = cur ; i < codejam.size() ; i++) {
    if (aux[lcur] == codejam[i]) break;
  }
  if (i == codejam.size()) return 0;
  //printf("Eu tenho um %c em %d\n",aux[lcur],i);
  //  getchar();
  int aux1, aux2;
  cur = i;
  aux1 = solve(cur+1,lcur);
  if (lcur+1 == aux.size()) {
    return aux1+1;
  }
  aux2 = solve(cur+1,lcur+1);
  if (aux2 == 0) return 0;
  else return aux1+aux2;  
}
