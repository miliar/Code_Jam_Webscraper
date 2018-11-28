//
//  main.cpp
//  SpeakinginTongues
//
//  Created by Maxim Grossu on 4/14/12.
//  Copyright (c) 2012 Maxim Grossu. All rights reserved.
//

#include <iostream>
#include <stdio.h>

char *transforRule = "yhesocvxduiglbkrztnwjpfmaq---";
inline char* transfor(char *input){
  char *result;
  int append = 1;
  result = (char *)malloc(sizeof(char));
  strcpy (result,input);
  for (int i = 0; i<strlen(input); i++) {
    if (input[i]==' ') {
      result[i]=' ';
    }else if (input[i]=='\n') {
      result[i]='\0';
      append = 0;
    }else{
      result[i]=transforRule[input[i]-'a'];
    }
  }
  if (append) {
//    strncat(result, "\n", 1);
  }
  return result;
}

int main(int argc, const char * argv[]){
  int size;
  char **inputs;
  FILE *fr = stdin;
//    cout<<"ad:";
//fr = fopen ("/Volumes/Info/Downloads/_web/A-small-attempt5.in.txt", "rt");
//  scanf("%i\n",&size);
  fscanf(fr,"%i\n",&size);

  inputs = (char **)malloc(size*sizeof(char*));
  for (int i = 0; i<size; i++) {
    inputs[i]=(char *)malloc(1000*sizeof(char));
//    fgets(inputs[i], 100, fr);
    fgets(inputs[i], 1000, fr);
  }
  
  for (int i = 0; i<size; i++) {
    printf("Case #%i: %s",i+1,transfor(inputs[i]));
    if (i!=size-1) {
      printf("\n");
    }
  }
  for (int i = 0; i<size; i++) {
    free(inputs[i]);
  }
  free(inputs);
  return 0;
}

