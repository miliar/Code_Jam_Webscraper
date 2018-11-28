#include <stdio.h>
#include <string.h>
#include <iostream.h>
using namespace std;

int tabel[40];
int mark[40];
int hasil[100];

int main() {
   int t,i, counter,len,base,res,temp;
   unsigned long long value,pengali;
   char input[100];
   
   scanf("%d",&t);
   for(counter= 1; counter<=t;counter++) {
      scanf("%s",input);
      for(i=0;i<40;i++) {
         tabel[i] = 0;
         mark[i]=-1;
      }
      for(i=0;i<100;i++) hasil[i] = 0;
      len = strlen(input);
      base = 0;
      for(i=0;i<len;i++) {
         if((int)input[i] >= 48 && (int)input[i] <=57) {
            if(tabel[(int)input[i]-48] != 1) {
               tabel[(int)input[i]-48] =1 ;
               base++;
            }            
         } else {
            if(tabel[(int)input[i]-87] != 1) {
               tabel[(int)input[i]-87] =1 ;
               base++;
            }  
         }
      }
      
      if(base==1) base = 2;
          
      res = 1;
      i = 0;
         if((int)input[i] >= 48 && (int)input[i] <=57) {
            if(mark[(int)input[i]-48] == -1) {
               mark[(int)input[i]-48] = res;
               hasil[i] = res;
            } else {
               hasil[i] =  mark[(int)input[i]-48];
            }
         }else {
            if(mark[(int)input[i]-87] == -1) {
               mark[(int)input[i]-87] = res;
               hasil[i] = res;
            } else {
               hasil[i] =  mark[(int)input[i]-87];
            }
         }
      temp = input[i];
         
      i = 1;
      res = 1;
      while(i<len && temp == input[i]) {
         hasil[i] = res;
         i++;
      }   
      res = 0;
      if(i<len){
         if((int)input[i] >= 48 && (int)input[i] <=57) {
            if(mark[(int)input[i]-48] == -1) {
               mark[(int)input[i]-48] = res;
               hasil[i] = res;
            } else {
               hasil[i] =  mark[(int)input[i]-48];
            }
         }else {
            if(mark[(int)input[i]-87] == -1) {
               mark[(int)input[i]-87] = res;
               hasil[i] = res;
            } else {
               hasil[i] =  mark[(int)input[i]-87];
            }
         }  
         i++;
      }
         
      res = 2;
       
      
      for(;i<len;i++) {
         if((int)input[i] >= 48 && (int)input[i] <=57) {
            if(mark[(int)input[i]-48] == -1) {
               mark[(int)input[i]-48] = res;
               hasil[i] = res;
               res++;
            } else {
               hasil[i] =  mark[(int)input[i]-48];
            }
         }else {
            if(mark[(int)input[i]-87] == -1) {
               mark[(int)input[i]-87] = res;
               hasil[i] = res;
               res++;
            } else {
               hasil[i] =  mark[(int)input[i]-87];
            }
         }
      }
      
      value = 0;
      pengali = 1;
      for (i = len-1; i>=0; i--) {
         value += hasil[i]*pengali;
         pengali = pengali * base;
      }
      
      printf("Case #%d: ",counter);
      cout << value <<endl;
   }
   
   while(getchar()!=EOF);
   return 0;
}
