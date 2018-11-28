#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int swap(char* in,int n){
    int len = strlen(in);
    char rs[len];
    for(int i = 0; i < n; i++) rs[i] = in[len-n+i];
    for(int j = n; j < len; j++) rs[j] = in[j-n];
    
    return atoi(rs);
}   

int genall(int i,int b){
    int r = 0;
    int k;
    char buff[100];
    int check[100];
    int count = 0;
    bool c = true;
    int len = strlen(itoa(i,buff,10));
    
    for(int j = 1; j <= len; j++){
            k = swap(itoa(i,buff,10),j);
            if(k <= b && k > i) {
                 c = true;
               for(int ii = 0; ii < count; ii++) if(k == check[ii]) c = false;   
                  if(c){
                        check[count] = k;
                        count++;
                      r++;
                      //printf("%d re %d\n",i,k);  
                  }    
            }
    }
    
    return r;
}

int main(){
    FILE *fr,*fw;
    fr = fopen("C:\\in.in","r");
    fw = fopen("C:\\out.out","w+");
    int t,k=0;
    fscanf(fr,"%d",&t);
    
    while(k++<t){
         int a,b,count=0;
         fscanf(fr,"%d %d",&a,&b);
         
         for(int i = a; i < b; i++) count+=genall(i,b);
         
         //printf("Case #%d: %d\n",k,count); 
         fprintf(fw,"Case #%d: %d\n",k,count);     
    }
    
    fclose(fr);
    fclose(fw);
    
    //system("pause");
    
    
    return 0;   
}
