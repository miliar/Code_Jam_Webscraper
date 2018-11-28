#include <cstdio>

int begin;
int end;
int factor;

int result;

int matrix[1001][1001];
int primes[1001];
int numOfPrimes;

void findPrimes() {
  numOfPrimes = 0;
  int isPrime = 1;
  for (int c = factor; c <= end; c++) {
    isPrime = 1;
    for (int d = 2; d < c; d++) {
      if (c%d == 0) {
        isPrime = 0;
        break;
      }
    }
    if (isPrime == 1){
      primes[numOfPrimes] = c;
      numOfPrimes++;
    }    
  }
}

void read() {
  scanf("%d %d %d",&begin, &end, &factor);
  for (int c = 0; c < 1001; c++) {
    for (int d = 0; d < 1001; d++) {
      matrix[c][d] = 0;
    }
  }
  for (int c = begin; c <= end; c++) {
    matrix[c][c] = 1;
  }
}

void solve(){
  findPrimes();
  int choosen[1001];
  for (int c = begin; c <= end; c ++) {
    choosen[c] = 0;
    for (int d = c +1; d <= end; d++) {
      for (int e = 0; e < numOfPrimes; e ++) {
        if ((c%primes[e] == 0)&& (d%primes[e] == 0)) {
          matrix[c][d] = 1;
          matrix[d][c] = 1;
          break;
        }
      }
    }
  }
  int elementStack[1001];
  int stackTop;
  int actual;
  
  result = 0;

  for (int c = begin; c <= end; c ++) {
    if (choosen[c] == 0){
      choosen[c] = 1;
      result++;
      stackTop = 1;
      elementStack[0] = c;
      while (stackTop > 0) {
        stackTop--;
        actual = elementStack[stackTop];
        for (int d = begin; d <= end; d++) {
          if (choosen[d] == 0){
            if ((matrix[actual][d] == 1) || (matrix[d][actual] == 1)) {
              elementStack[stackTop] = d;
              stackTop++;
              choosen[d] = 1;
            }                      
          }
        }
      }
      
    }
  }

  
  
}

int main() {
  int numOfTest;
  scanf("%d", &numOfTest);
  for (int c = 1;c <= numOfTest; c++) {
    read();
    solve();
    printf("Case #%d: %d\n", c, result);
  }
}
