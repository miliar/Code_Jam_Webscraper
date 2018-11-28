#include <stdio.h>
#define NUM_LEN 9 
#define MAX_NUM 20001
#define MAX_numberS 31

int  comput(int number[],int snoper[],int Power[],int N, int K);

void init(int snoper[],int Power[]);
int main(int argc, char **argv)
{
    FILE *fp;
    int number[MAX_NUM];
    int snumber[NUM_LEN];
    int snoper[MAX_numberS]; //if 1 means ON, if 0 means OFF
    int Power[MAX_numberS];   //if 1 means power, if 0 means no 
    char c;
    int i=0;
    int j=0;    
    int k=0;
    int line;
    int account=0;
    int N,K;
    FILE *f1;
    f1 = fopen ("result.txt", "wt");
    
    
    init(snoper,Power); 
    if(argc < 2)        {
        printf("No input file!\n");
        return 0;
    }
    if((fp = fopen(*++argv,"r")) == NULL){
        printf("Open the file %s failed!\n", *argv);
        return 1;
    }
    
    while((c = getc(fp)) != EOF){          
       if(c == ' '||c =='\n'){
            number[j] = 0;
            k = 0;
            while(k < i){
                number[j] *=10;
                number[j] +=snumber[k++];
            }
            account++;
            j++;
            i=0;
        }else{
            snumber[i++]=c - 48;
        }
     }
    
   // printf("%d\n",account);
    
    
    line = number[0];
    i=0;
       while(i<line){
         N = number[i*2+1];
         K = number[i*2+2];
         init(snoper,Power);
         if(comput(number,snoper,Power,N,K)==0){
         fprintf (f1, "Case #%d: OFF\n",i+1);
         }else{
         fprintf (f1, "Case #%d: ON\n",i+1);
          }    
         i++;            
       } 
    return 0;
}

int  comput(int number[],int snoper[],int Power[],int N, int K){

      int i=0;
      int j=0;  
      for(j=0;j<K;j++){
         for (i=0;i<N;i++){
             if (Power[i]==1){
                 snoper[i]=(snoper[i]+1)%2;
              }
          }
          for(i=0;i<N;i++){
              if(snoper[i]==1&&Power[i]==1){
                      Power[i+1]=1;
              }else{
                    Power[i+1]=0;
              }
          }                  
      }
      
     // printf("Submit\n");
      if(Power[N]==1){
      return 1;
      }else{
      return 0;
      }
         
}

void init(int snoper[],int Power[]){
     int i;
     for(i=0;i<MAX_numberS;i++){
            snoper[i]=0;
             Power[i]=0;              
          }
        Power[0]=1; 
     }



