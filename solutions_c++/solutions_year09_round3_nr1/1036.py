#include <iostream>
#include <cstdlib>
#include <string.h>
#include <math.h>
#include <stdio.h>

using namespace std;

int T;
#define MAXSTR 80
char str[MAXSTR];
int count[MAXSTR] = {0};
int bit[MAXSTR];
int map[MAXSTR];
int base;
int val=0;

int getNext(){
   if(val == 0){
      val = 2;
      return 0;
   }
   val ++;
   return val-1;
}

int main(int argc, char *argv[]){
   
   if(argc != 2){ 
      printf("Usage : executable inputFile");
   }
   
   FILE * in;
   FILE * out;
   in = fopen(argv[1],"r");
   out = fopen("output.txt","w");
   
   if( in == NULL || out == NULL ){
      printf("Unable to open files %s or %s",argv[1],"output.txt");
   }
      
   fscanf(in,"%d",&T);
   for(int i=0 ; i<T ; i++){
      val = 0;
      str[0] = '\0';
      fscanf(in,"%s",str);
//      printf("\n%s\n",str);
      for(int k=0 ; k< MAXSTR ; k++){
         count[k] =0 ;
      }
      int j=0;
      int l=1;
      count[str[j]-'0']++;
      bit[0] = 1;
      map[str[j]-'0'] = 1;
      j++;
      int s=1;
      while(str[j]!='\0'){
         count[str[j]-'0']++;
         if(count[str[j] -'0'] == 1){
            bit[l] = getNext();
            map[str[j]-'0']= bit[l];
            l++;
         }
         else{
            bit[l] = map[str[j]-'0'];
            l++;
         }
         j++;
      }
      int cnt=0;
      for(int k=0 ; k < MAXSTR ; k++){
         if(count[k] != 0){
            cnt ++;
         }
      }
      base = max(2,cnt);

      int len = strlen(str);
      long long ans=0;
      for(int h=len-1; h>=0 ; h--){
         ans = ans + (bit[h]*pow(base,len - h - 1));
         cnt++;
      }
 //     printf("\n%lld %d\n",ans,cnt);
     
      fprintf(out,"Case #%d: %lld\n",i+1,ans);
   }
   fclose(in);
   fclose(out);
   return 0;
   
}
