#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <conio.h>
#include <string>
#include <list>
#include <vector>

using namespace std;

FILE *out, *in;  
list<char> v;

void muestra(){     
  for (list<char>::iterator it=v.begin(); it!=v.end(); ++it){
      printf("%c",*it);    
      fprintf(out,"%c",*it);    
      }
  }

int main(void){
//  in=fopen("testa.in","r");
//  out=fopen("testa.out","w");    
//  in=fopen("bsmall.in","r");
//  out=fopen("bsmall.out","w");
  in=fopen("blarge.in","r");
  out=fopen("blarge.out","w");    

    int t;
    char car;

    fscanf(in,"%d\n",&t);
    for (int i=1;i<=t;i++){
        v.clear();
        do{
            fscanf(in,"%c",&car);
            if (car>='0'&&car<='9'&&!feof(in))
               v.push_back(car);             
            }while((car>='0'&&car<='9')&&!feof(in));
           
        while (!next_permutation (v.begin(),v.end())){
              prev_permutation (v.begin(),v.end()); 
              v.push_front('0');             
              }
        fprintf(out,"Case #%d: ",i);
        muestra();
        fprintf(out,"\n");
        }
    fclose(in);
    fclose(out);  
    printf("listo");  
    getch();
    }
