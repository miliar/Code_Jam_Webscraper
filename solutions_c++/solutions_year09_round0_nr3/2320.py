#include <stdio.h>
#include <iostream>
#include <conio.h>
#include <string>
#include <vector>

using namespace std;

string p;
string c;
int k;

int eval(int z,int y){
     if (y==c.size())
        k++;
     if (z>p.size()){     
        return 0;
        }     
        else{
          do{  
               if (p[z]==c[y]){  
                  eval(z+1,y+1); 
                  }                          
               z++;
              }while(z<p.size());
          }                 
     }

int main(void){
    int n;
    char t;
    FILE *out;
    out=fopen("3.out","w");
    c="welcome to code jam";
    scanf("%d\n",&n);
    for (int i=0;i<n;i++){
        k=0;
        p.clear();
      	scanf("%c",&t);
        while (t!='\n'){
          p.push_back(t);
		  scanf("%c",&t);
		  }
        eval(0,0);        
             printf("Case #%d: %04d\n",i+1,k);
        fprintf(out,"Case #%d: %04d\n",i+1,k);
        }
    getch();
    }
