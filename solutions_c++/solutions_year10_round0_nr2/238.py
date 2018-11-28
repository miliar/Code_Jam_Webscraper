#include <stdio.h>
#include <string.h>
#include <stdlib.h>

class TInt{
  char *number;
  int len;

  TInt mul10n(int N) const{
    TInt res(*this);
    int i;
    for( i = 0; i < N; i ++ ){
      res.number[res.len + i] = '0';
    }
    res.number[res.len + N] = 0;
    res.len += N;
    return res;
  }
public:
  friend int CompareTInt(const void *, const void *);

  TInt(){
      number = new char[100];
      number[0] = '0';
      number[1] = 0;
      len = 1;
  }
  TInt(const TInt& in){
    number = new char[100];
    strcpy(number, in.number);
    len = strlen(number);
  }
  TInt(char* str){
    number = new char[100];
    strcpy(number, str);
    len = strlen(number);
  }
  ~TInt(){
    delete[] number;
  };
  void Print(void){
    printf("%d:%s\n",len,number);
  }
  char* GetNumber(void){
    return number;
  }
  const TInt& operator=(const TInt& a){
    strcpy(number, a.number);
    len = strlen(number);
    return *this;
  }

  TInt operator+(const TInt& a){
    TInt res("0"), b("0");
    int penalty, i;

    if( *this >= a ){
      res = *this;
      b = a;
    }
    else{
      b = *this;
      res = a;
    }

    penalty = 0;
    for( i = 1; (i <= res.len) && (i <= b.len); i ++ ){
      if( (res.number[res.len - i] - '0') + (b.number[b.len - i] - '0') + penalty < 10 ){
        res.number[res.len - i] = '0' + (res.number[res.len - i] - '0') + (b.number[b.len - i] - '0') + penalty;
        penalty = 0;
      }
      else{
        res.number[res.len - i] = '0' - 10 + (res.number[res.len - i] - '0') + (b.number[b.len - i] - '0') + penalty;
        penalty = 1;
      }
    }
    for( i = b.len + 1; i <= res.len; i ++ ){
      if( res.number[res.len - i] - '0' + penalty < 10 ){
        res.number[res.len - i] = res.number[res.len - i] + penalty;
        penalty = 0;
      }
      else{
        res.number[res.len - i] = '0';
        penalty = 1;
      }
    }

    if( penalty ){
      for( i = res.len; i >= 0; i -- ){
        res.number[i+1] = res.number[i];
      }
      res.number[0] = '1';
      res.len ++;
    }
    return res;
  }

  TInt operator-(const TInt& a){
    TInt res(*this);
    int penalty, i;

    penalty = 0;
    for( i = 1; (i <= res.len) && (i <= a.len); i ++ ){
      if( res.number[res.len - i] >= a.number[a.len - i] + penalty ){
        res.number[res.len - i] = '0' + (res.number[res.len - i] - a.number[a.len - i] - penalty);
        penalty = 0;
      }
      else{
        res.number[res.len - i] = '0' + (res.number[res.len - i] + 10 - a.number[a.len - i] - penalty);
        penalty = 1;
      }
    }
    for( i = a.len + 1; i <= res.len; i ++ ){
      if( res.number[res.len - i] >= '0' + penalty ){
        res.number[res.len - i] = res.number[res.len - i] - penalty;
        penalty = 0;
      }
      else{
        res.number[res.len - i] = '9';
        penalty = 1;
      }
    }
    while( res.number[0] == '0' ){
      for( i = 0; i <= res.len; i ++ ){
        res.number[i] = res.number[i+1];
      }
      res.len --;
    }
    if( res.len == 0 ){
      res.len = 1;
      res.number[0] = '0';
      res.number[1] = 0;
    }
    return res;
  }

  TInt operator*(const TInt& a){
    return TInt("1");
  }

  TInt operator/(const TInt& a){
    TInt rest(*this), res("0");
    int i = this->len - a.len, j;

    if( i < 0 ){
      return res;
    }
    
    for( j = rest.len-1; j >= 0; j -- ){
      while( rest >= a.mul10n(j) ){
        rest = rest - a.mul10n(j);
        res = res + TInt("1").mul10n(j);
      }
    }

    return res;
  }

  TInt operator%(const TInt& a){
    TInt rest(*this), res("0");
    int i = this->len - a.len, j;

    if( i < 0 ){
      return rest;
    }
    
    for( j = rest.len-1; j >= 0; j -- ){
      while( rest >= a.mul10n(j) ){
        rest = rest - a.mul10n(j);
        res = res + TInt("1").mul10n(j);
      }
    }

    return rest;
  }

  bool operator!=(const TInt& a){
    if( *this == a ){
      return false;
    }
    else{
      return true;
    }
  }

  bool operator==(const TInt& a){
    if( this->len != a.len ){
      return false;
    }
    if( strcmp(this->number, a.number) == 0 ){
      return true;
    }
    else{
      return false;
    }
  }

  bool operator>=(const TInt& a){
    if( this->len > a.len ){
      return true;
    }
    if( this->len < a.len ){
      return false;
    }
    if( strcmp(this->number, a.number) < 0 ){
      return false;
    }
    else{
      return true;
    }
  }

};

int CompareTInt(const void* a, const void* b){
  if( *(TInt*)(a) == *(TInt*)(b) ){
    return 0;
  }
  if( *(TInt*)(a) >= *(TInt*)(b) ){
    return 1;
  }
  return -1;
}

TInt Solver(int N, TInt T[]){
  TInt TDiff[1000];
  int i,j,NN=N;
  TInt GCD, tmp, tmp1;

  qsort(T, N, sizeof(TInt), CompareTInt);
  j = 0;
  for( i = 1; i < N; i ++ ){
    TDiff[j] = T[i] - T[0];
    if( TDiff[j] != TInt("0") ){
      j++;
    }
    else{
      NN--;
    }
//    TDiff[i-1] = T[i] - T[0];
  }
  qsort(TDiff, NN - 1, sizeof(TInt), CompareTInt);
/*
for( i = 0; i < NN - 1; i++ ){
    TDiff[i].Print();
  }
*/
  GCD = TDiff[0];
  for( i = 1; i < NN - 1; i ++ ){
    tmp = TDiff[i] % GCD;
    while( tmp != TInt("0") ){
      tmp1 = GCD;
      GCD = TDiff[i] % GCD;
      TDiff[i] = tmp1;
      tmp = TDiff[i] % GCD;
    }
  }

/*
  GCD.Print();
*/

  tmp = T[0] % GCD;
  if( tmp == TInt("0") ){
    return TInt("0");
  }
  else{
    tmp = GCD - tmp;
    return tmp;
  }
}

int main(int argc, char *argv[]){
  FILE* filein;
  FILE* fileout;
  int C, N;
  char t[100];
  TInt T[1000];
  int c, i;

  if( argc < 3 ){
    printf("Usage is: task2 filein fileout\n");
    return 0;
  }

  /* Input */

  filein = fopen(argv[1], "r");
  if( filein == NULL ){
    printf("Error open(); filein\n");
    return 0;
  }
  fileout = fopen(argv[2], "w");
  if( fileout == NULL ){
    printf("Error open(); fileout\n");
    return 0;
  }

  fscanf(filein, "%d\n", &C);
  printf("%d\n", C);
  for( c = 0; c < C; c ++ ){
    fscanf(filein, "%d ", &N);
    printf("-------------\n");
    printf("%d ", N);
    for( i = 0; i < N - 1; i ++ ){
      fscanf(filein, "%s ", t);
      T[i] = TInt(t);
    }
    fscanf(filein, "%s\n", t);
    T[N-1] = TInt(t);
    for( i = 0; i < N; i ++ ){
      printf(" | %s", T[i].GetNumber());
    }
    printf("\n");

    /* Solve & Output*/
    fprintf(fileout, "Case #%d: %s\n", c+1, Solver(N, T).GetNumber() );
//    printf("Case #%d: %s\n", c+1, Solver(N, T).GetNumber() );
  }


  fclose(fileout);
  fclose(filein);

  return 0;
}
