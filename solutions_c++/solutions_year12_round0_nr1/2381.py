#include <iostream>
#include <map>
#include <cstring>

using namespace std;

map<char,char> hash;

void inicializar(){
  int casos;
  cin >> casos;
  char linea1[256];
  char linea2[256];
  char linea3[256];
  char linea4[256];
  char linea5[256];
  char linea6[256];
  memset(linea1, 0 , 256);
  memset(linea2, 0 , 256);
  memset(linea3, 0 , 256);
  memset(linea4, 0 , 256);
  memset(linea5, 0 , 256);
  memset(linea6, 0 , 256);
  cin.getline(linea1,256);
  cin.getline(linea1,256);
  cin.getline(linea2,256);
  cin.getline(linea3,256);
  cin.getline(linea4,256);
  cin.getline(linea5,256);
  cin.getline(linea6,256);
  
  for(int i = 0 ; i <= 101 ; ++i){
    if(linea1[i] != 0){
//       cout << "linea 1 caracter " << i << endl;
      hash[linea1[i]] = linea4[i+9];
    }
    if(linea2[i] != 0){
//       cout << "linea 2 caracter " << i << endl;
      hash[linea2[i]] = linea5[i+9];
    }
    if(linea3[i] != 0){
//       cout << "linea 3 caracter " << i << endl;
      hash[linea3[i]] = linea6[i+9];
    }
  }
  hash['q'] = 'z';
  hash['e'] = 'o';
  hash['y'] = 'a';
  hash['g'] = 'v';
  hash['o'] = 'k';
  hash['u'] = 'j';
  hash['z'] = 'q';
}

void verificar(){
  for(char c = 'a' ; c <= 'z' ; ++c){
    if(hash.count(c) == 0){
      cout << "Falta el caracter " << c << endl;
    }else{
      cout << c << " -> " << hash[c] << endl;
    }
  }

}

void leer(){
  int casos;
  cin >> casos;
  char linea[256];
  cin.getline(linea,1);
//   cout << "Hay " << casos << " casos" << endl;
//   return;
  for(int i = 1; i <= casos ; ++i){
    char linea[256];
    memset(linea, 0 , 256);
    cin.getline(linea, 256);
    cout << "Case #" << i << ": ";
    for(int j = 0; j <= 100 ; ++j){
      if(linea[j] != 0 ){
        cout << hash[linea[j]];
      }
    }
    cout << endl;
  }
}

int main(){
 
  inicializar();
//   verificar();
  leer();
}