#include <iostream>
#include <cstring>
using namespace std;

const int ALPHS = 'Z' - 'A' +1;
int spells[1000+1];
int spells_len;
bool opposed[ALPHS][ALPHS];
int combine[ALPHS][ALPHS];

void clean(){
  spells_len=0;
  for(int i=0; i<ALPHS; ++i){
    for(int j=0; j<ALPHS; ++j){
      opposed[i][j]=false;
      combine[i][j]=-1;
    }
  }
}

int toDigit(char c){
  return toupper(c) - 'A';
}

char toAlph(int i){
  return 'A' + i;
}


void push(int i){
  spells[spells_len++]=i;
}

int pop(){
  return spells[--spells_len];
}


void doCombine(){
  if(spells_len<2)
    return;
  int i1=spells[spells_len-1];
  int i2=spells[spells_len-2];
  int c=combine[i1][i2];
  if(c>=0){
    pop();pop();
    push(c);
  }
}

void doOpposed(){
  int last = spells[spells_len-1];
  for(int i=0; i<spells_len; ++i)
    if(opposed[spells[i]][last]){
      spells_len = 0;
      return;
    }
}

void print(){
  cout << '[';
  if(spells_len)
    cout << toAlph(spells[0]);
  for(int i=1; i<spells_len; ++i)
    cout << ", " << toAlph(spells[i]);
  cout << ']' << endl;
}

int main(){
  int T;
  cin >> T;
  for(int Case=1; Case <= T; ++Case){
    clean();
    
    int C;
    cin >> C;
    while(C--){
      char b1,b2,nb;
      cin >> b1 >> b2 >> nb;
      combine[toDigit(b2)][toDigit(b1)]=combine[toDigit(b1)][toDigit(b2)]=toDigit(nb);
    }

    int D;
    cin >> D;
    while(D--){
      char b1,b2;
      cin >> b1 >> b2;
      opposed[toDigit(b2)][toDigit(b1)]=opposed[toDigit(b1)][toDigit(b2)]=true;;
    }

    int N;
    cin >> N;
    while(N--){
      char b;
      cin >> b;
      push(toDigit(b));
      doCombine();
      doOpposed();
    }

    cout << "Case #" << Case <<": ";
    print();
  }
  return 0;
}