#include <iostream>
#include <fstream>

using namespace std;

int* readFile(const char*);
int getN(const char*);
void printBinary(int);
int getState(int);
void output(const char*,int*,int);

int main(int argc, char const *argv[])
{
  int n = getN("sample.txt");
  int* fields = readFile("sample.txt");
  for(int i=0;i<n;i++){
    fields[i]= getState(fields[i]);
  }
  output("output.txt",fields,n);
  return 0;
}

int* readFile(const char* filename){
  ifstream file(filename);
  if(!file.is_open()) return NULL;
  int length;
  file>>length;
  int* data = new int[length];
  char* line = new char[4];
  for(int i=0;i<length;i++){
    int d=0;
    for(int j=0;j<4;j++){
      file>>line;
      for(int k=0;k<4;k++){
        int shift = 8*j+2*k;
        switch((int)line[k]){
          case 'X':
            d=d|(1<<shift);
            break;
          case 'O':
            d=d|(2<<shift);
            break;
          case 'T':
            d=d|(3<<shift);
            break;
        }
      }
    }
    data[i]=d;
  }
  file.close();
  return data;
}

int getN(const char* filename){
  ifstream file(filename);
  if(!file.is_open()) return 0;
  int length;
  file>>length;
  file.close();
  return length;
}


void printBinary(int x){
  for(int i=0;i<32;i++){
    if(i%2==0) cout<<" ";
    int a=(x>>(31-i)) & 1;
    cout<<a;
  }
}

int getState(int x){
  int check1[10] = {
    0x00000055,
    0x00005500,
    0x00550000,
    0x55000000,
    0x01010101,
    0x04040404,
    0x10101010,
    0x40404040,
    0x40100401,
    0x01041040
  };
  int check2[10] = {
    0x000000AA,
    0x0000AA00,
    0x00AA0000,
    0xAA000000,
    0x02020202,
    0x08080808,
    0x20202020,
    0x80808080,
    0x80200802,
    0x02082080
  };
  for(int i=0;i<10;i++){
    if((check1[i]&x)==check1[i]) return 1;
    if((check2[i]&x)==check2[i]) return 2;
  }
  for(int i=0;i<16;i++){
    if(((x>>(2*i)) & 3) == 0) return 0;
  }
  return 3;
}

void output(const char* filename,int* res,int n){
  ofstream file;
  file.open(filename,ios::out);
  for(int i=0;i<n;i++){
    file<<"Case #"<<(i+1)<<": ";
    switch(res[i]){
      case 0:
        file<<"Game has not completed"<<endl;
        break;
      case 1:
        file<<"X won"<<endl;
        break;
      case 2:
        file<<"O won"<<endl;
        break;
      case 3:
        file<<"Draw"<<endl;
        break;
    }
  }
  file.close();
}


