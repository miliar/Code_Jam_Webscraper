#include "stdio.h"
#include "stdlib.h"
#include "conio.h"

int c,d,t,n,i,j,k,z;
char nc,nd,nn;
char s[101];
char comb[36][4];
char opp[28][3];
int combStart;
int combEnd;
int oppStart[100];
char oppEnd[100];
int oppPos;
char list[100];
int count;

bool inComb(){
     for(k = 0; k < c; k++){
           if(comb[k][0] == s[j]){
                   if(comb[k][1] == s[j+1]){
                        list[count] = comb[k][2];
                        count++;    
                        return true;    
                   }                  
           } else if(comb[k][1] == s[j]){
                   if(comb[k][0] == s[j+1]){
                        list[count] = comb[k][2];
                        count++;
                        return true;
                   } 
           }      
     }     
     
     return false;
}

bool isOppEnd(){
     for(k = 0; k < oppPos; k++){
           if(oppEnd[k] == s[j]){     
                return true;
           } else if(oppEnd[k] == s[j]){                
                return true;
           }      
     }      
     return false;
}

void isOppStart(){
     for(k = 0; k < d; k++){
           if(opp[k][0] == s[j]){     
                oppEnd[oppPos] = opp[k][1];
                oppPos++;
           } else if(opp[k][1] == s[j]){
                oppEnd[oppPos] = opp[k][0];
                oppPos++;  
           }      
     }     
}

int main(){
    FILE * file;
    file = fopen("output2.txt","w");
    scanf("%d", &t);
    for(i = 0 ; i < t; i++){
          count = 0;        
          oppPos = 0;
          
          scanf("%d ", &c);
          for(j = 0; j < c; j++){
                scanf("%s ", comb[j]);               
          }
          
          scanf("%d ", &d);
          for(j = 0; j < d; j++){
                scanf("%s ", opp[j]);
          }
          
          scanf("%d ", &n);
          scanf("%[^\n]", s);
          for(j = 0 ; j < n; j++ ){
                 if(!isOppEnd()){                    
                    if(inComb()){
                      j++;
                      continue;
                    } else {
                      list[count] = s[j];
                      count++;
                      isOppStart();       
                    }
                 } else {
                    count = 0; 
                    oppPos = 0;       
                 }
          }         
          fprintf(file,"Case #%d: [", i+1);
          if(count > 0){
            fprintf(file,"%c", list[0]);
          }
          for(j = 1;j < count; j++){    
                fprintf(file,", %c",list[j]);
          }
          fprintf(file,"]\n");
    }
    fclose(file);
    return 0;    
}
