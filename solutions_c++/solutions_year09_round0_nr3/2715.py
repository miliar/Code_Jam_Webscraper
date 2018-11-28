#include <iostream>
#include <iomanip>
using namespace std;


int contador = 0;
char welcome[50] = "welcome to code jam";
char line[510];
int wlen;
int len;

void probar(int letra, int posicion){
  
  if(letra > wlen){
    contador++;
    return;
  }
  for(int i = posicion; i <=len; i++){
    if(line[i] == welcome[letra]){
      probar(letra+1, i+1);
    }
  }
}

int main(){

  
  int num;
  cin.getline(line, 500);
  num = atoi(line);
  wlen = strlen(welcome);
  
  for(int i = 0; i < num; i++){
    
    cin.getline(line, 500);
    len = strlen(line);
    probar(0, 0);
    cout  << "Case #" << i+1 << ": ";
    cout << setfill('0') << setw(4)<<  contador << endl;
    contador = 0;
  }

}
