#include <cstdlib>
#include <iostream>
#include <fstream>
#include <list>

using namespace std;

typedef unsigned int nat;

void traducir(char* googlerese, char* english, nat n){
  for(nat i=0; i<n; i++){
         if(googlerese[i] == 'a') english[i] = 'y';
    else if(googlerese[i] == 'b') english[i] = 'h';
    else if(googlerese[i] == 'c') english[i] = 'e';
    else if(googlerese[i] == 'd') english[i] = 's';
    else if(googlerese[i] == 'e') english[i] = 'o';
    else if(googlerese[i] == 'f') english[i] = 'c';
    else if(googlerese[i] == 'g') english[i] = 'v';
    else if(googlerese[i] == 'h') english[i] = 'x';
    else if(googlerese[i] == 'i') english[i] = 'd';
    else if(googlerese[i] == 'j') english[i] = 'u';
    else if(googlerese[i] == 'k') english[i] = 'i';
    else if(googlerese[i] == 'l') english[i] = 'g';
    else if(googlerese[i] == 'm') english[i] = 'l';
    else if(googlerese[i] == 'n') english[i] = 'b';
    else if(googlerese[i] == 'o') english[i] = 'k';
    else if(googlerese[i] == 'p') english[i] = 'r';
    else if(googlerese[i] == 'q') english[i] = 'z';
    else if(googlerese[i] == 'r') english[i] = 't';
    else if(googlerese[i] == 's') english[i] = 'n';
    else if(googlerese[i] == 't') english[i] = 'w';
    else if(googlerese[i] == 'u') english[i] = 'j';
    else if(googlerese[i] == 'v') english[i] = 'p';
    else if(googlerese[i] == 'w') english[i] = 'f';
    else if(googlerese[i] == 'x') english[i] = 'm';
    else if(googlerese[i] == 'y') english[i] = 'a';
    else if(googlerese[i] == 'z') english[i] = 'q';
    else english[i] = googlerese[i];
  }
  for(nat j=n; j<101; j++){
    english[j] = '\0';
  }
}

int main(int argc, char *argv[]){

  nat T;
  char* s;

  FILE * origen;
  FILE *destino;

  nat tamanio = 101;

  char english [tamanio];
  char googlerese [tamanio];
  origen = fopen ("A-small-attempt1.in" , "r");
  if (origen == NULL){
    perror ("Error opening in file");
  } else {
    destino= fopen("A-small-attempt1.out","w");
    if (destino == NULL){
      perror ("Error opening out file");
    } else {
      fscanf (origen, "%d", &T);
      fgets(googlerese , tamanio , origen);
      for(int tt=1; tt<=T; tt++){
        fgets(googlerese , tamanio , origen);
        nat n = strlen(googlerese);
        fprintf(destino,"Case #%d: ", tt);
        traducir(googlerese, english, n);
        fputs(english,destino);
        if (n==100) {
          fprintf(destino,"\n");
          fgets(googlerese , tamanio , origen);
        }
      }
    }
  }

  fclose(origen);
  fclose(destino);

  return EXIT_SUCCESS;
}
