#include <iostream>
#include <string>
#include <math.h>
using namespace std;
unsigned long long solve (string num) {
  int j,i;
   int vetor[10];
  unsigned long long value[100];
  int vetor2[150];
  for (i = 0 ; i < 150 ; i++) vetor2[i] = -1;
  for (i = 0 ; i < 10 ; i++) vetor[i] = 0;
     for (i = 0 ; i < num.size() ; i++) {
      /*Se nao for numero*/
	if (vetor2[num[i]] != -1) { 
	  num[i] = (vetor2[num[i]]+'0');
	}
	else {
	  for (j = 0 ; j < 10 ; j++) {
	    if (vetor[j] == 0) {
	      if (j == 0 && i == 0) continue;
	      vetor[j] = 1;
	      vetor2[num[i]] = j;
	      num[i] = j+'0';
	      break;
	    }
	  }
	}
    }
  unsigned long long base,sum = num[num.size()-1]-'0';
  value[0] = 1;
  base = 0;
  for (i = 0 ; i < num.size() ; i++) {
    if (num[i]-'0' > base)
      base = num[i]-'0';
  }
  base++;
  for (i = num.size()-2 ; i >= 0 ; i--) {
    value[num.size()-1-i] = base*value[num.size()-2-i];
    sum += (unsigned long long)(num[i]-'0')*value[num.size()-1-i];
  }
  return sum;
}
  
int main() {
  int N;
  int i;
  scanf("%d",&N);
  string num;
  for (i = 1 ; i <= N ; i++) {
    cin >> num;
    cout << "Case #" << i << ": " << solve(num) << "\n";
  }
  return 0;
}
