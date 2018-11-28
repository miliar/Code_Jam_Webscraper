#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>
//#include <algorithm>
#include <conio.h>
#include <string>
#include <list>
#include <vector>

using namespace std;

FILE *out, *in;  

vector<char> cad;
vector<char> cad2;

void muestra(){     
  for (vector<char>::iterator it=cad2.begin(); it!=cad2.end(); ++it){
      printf("%c",*it);    
//      fprintf(out,"%c",*it);    
      }
  }

void muestra2(){     
  for (vector<char>::iterator it=cad.begin(); it!=cad.end(); ++it){
      printf("%c",*it);    
//      fprintf(out,"%c",*it);    
      }
  }

void replace(char c,char c2, int s){
     for (int j=s;j<cad2.size();j++){
         if (cad2[j]==c&&cad[j]!='@'){
            cad2[j]=c2;
            cad[j]='@';
            }
         
         }
     
     }

__int64 basetodec(int b){
     __int64 l;
     l=0;
     for (int j=0;j<cad2.size();j++){
         l+=pow(b,cad2.size()-j-1)*(cad2[j]-48);
         }
     return l;     
     }

int main(void){
//  in=fopen("testa.in","r");
//  out=fopen("testa.out","w");    
  in=fopen("asmall.in","r");
  out=fopen("asmall.out","w");
//  in=fopen("blarge.in","r");
//  out=fopen("blarge.out","w");    

    int t,b;
    char c,c2,c3;
    __int64 l;
    fscanf(in,"%d\n",&t);
    for (int i=1;i<=t;i++){
        fscanf(in,"%c",&c);
        cad.clear();
        cad2.clear();        
        do{
           cad.push_back(c);
           cad2.push_back(c);           
           fscanf(in,"%c",&c);
           }while (c!='\n'&&!feof(in));
/*           muestra();
           printf("\t");  
            muestra2();
           printf("\n");*/
        b=1;
        for (int j=0;j<cad.size();j++){
            if (cad[j]!='@'){
                c=cad[j];             
//                c2=cad2[j];
                if (b==1){
                   replace (c, '1',j);                
                   }
                else if (b==2){
                   replace (c, '0',j);                
                   }               
                else {
                   c3=b-1+48;
                   replace (c, c3,j);                
                   }               
                b++;
                }
/*            muestra();
           printf("\t");  
            muestra2();
           printf("\n");
           getch();       */
        }
        b--;
        if (b<2)
           b=2;
        l=basetodec(b);
/*           muestra();
           printf("\t");  
            muestra2();
           printf("\n");*/
        printf("Case #%d: %I64d\n",i,l);     
        fprintf(out,"Case #%d: %I64d\n",i,l);             
        }
    fclose(in);
    fclose(out);  
    printf("listo");  
    getch();
    }
