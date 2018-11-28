#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <cctype>

using namespace std; 

const int MAX_LEN = 110; 

map<char, char> haha; 

void load_mapping(){
  FILE *f = fopen("a.dat", "r"); 
  int T; 
  fscanf(f, "%d\n", &T); 
  char cipher[MAX_LEN]; 
  char text[MAX_LEN]; 
  for (int i = 0; i<T; ++i) {
    fgets(cipher, MAX_LEN, f); 
    fgets(text, MAX_LEN, f); 
    for (int i = 0; cipher[i]; ++i)
      if (isalpha(text[i])) haha[cipher[i]] = text[i]; 
  }
  fclose(f); 
}

int main(){
  
  load_mapping(); 
  int T; 
  scanf("%d\n", &T); 
  for (int i = 1; i<=T; ++i){
    char line[MAX_LEN]; 
    gets(line); 
    printf("Case #%d: ", i); 
    for (int j = 0; line[j];  ++j) 
      if (isalpha(line[j])) printf("%c", haha[line[j]]);  
      else printf("%c", line[j]); 
    puts(""); 
  }
  
  return 0; 
}
