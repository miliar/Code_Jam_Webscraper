#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

int placeappeared[256];
char alfabet[256];
int size_alphabet;
char linha[100];
int ncases;

void gen_alphabet() {

  for(int i=0;linha[i]!='\0';i++) {
    if(placeappeared[linha[i]]<0) {
      if(size_alphabet==0) {
        placeappeared[linha[i]]=1;
      }else if(size_alphabet==1) {
        placeappeared[linha[i]]=0;
      } else {
        placeappeared[linha[i]]=size_alphabet;
      }
      size_alphabet++;
    }
  }
  if(size_alphabet<2) {
    size_alphabet=2;
  }

}

typedef unsigned long long uint64;

unsigned long long calc_num() {
  unsigned long long res=0;
  for(int i=0;linha[i]!='\0';i++) {
    res=res*size_alphabet;
    res=res+placeappeared[linha[i]];
  }
  return res;
}

int main() {
  scanf(" %d",&ncases);
  for(int i=0;i<ncases;i++) {
    scanf("%s",linha);
    size_alphabet=0;
    for(int k=0;k<256;k++) {
      placeappeared[k]=-1;
    }
    gen_alphabet();
    unsigned long long res=calc_num();
    printf("Case #%d: ",i+1);
    cout << res <<endl;
  }




}
