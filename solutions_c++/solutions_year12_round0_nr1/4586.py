#include <stdio.h>
#include <iostream>

using namespace std;

char dir[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main ()
{

int casos=0;
//char cadena[101];
char aux;
cin >> casos;
getchar();

for(int i=0; i<casos; i++){
  cout <<"Case #"<<(i+1)<<": ";
  while( (aux=getchar())!='\n' ){
    if(aux==' '){cout << ' ';}
    else{cout << dir[aux-97];}
  }
  cout<< endl;
}

}
