#include <stdio.h>
#include <iostream>

using namespace std;

int main(){
  char letras[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't',  'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
  
  int t;
  string x;
  
  cin >> t;
  
  cin.ignore();
  
  for(unsigned int i = 0; i < t; i++){
    getline(cin, x);
    printf("Case #%d: ", i+1);
    for(unsigned int k = 0; k < x.length(); k++)
      printf("%c", x[k] == ' ' ? ' ' : letras[x[k]-97]);
    printf("\n");
  }
}