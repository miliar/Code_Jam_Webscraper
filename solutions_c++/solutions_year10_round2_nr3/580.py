#include<stdio.h>
#include<string.h>
#include<conio.h>

#define max(a,b) a>b ? a : b

int calcPossis(int numbers,int len){
  if(len==1)
    return numbers;
  int count=0;
  for(int h=0;h<(numbers-len+1);h++){
    count=count+calcPossis(numbers-h-1,len-1);
  }   
  return count;
}

int getPossibles(int size,int number){
  if(size==1){
    return 1;
  }
  int count=0,vahe;
  for(int h=max((2*size-number),1);h<size;h++){
    vahe=getPossibles(h,size);
    if(size-h-1>0)
      vahe=vahe*calcPossis(number-size-1,size-h-1);
    count=count+vahe;
    count=count%100003;  
  }
  return count;
}

int main(){
  FILE *fin;
  FILE *fout;
  int numberOfInputs;
  fin=fopen("D:\\task.in","r");
  fout=fopen("D:\\task.out","w");  
  fscanf(fin,"%d\n",&numberOfInputs);
  
  int n,count,tmp;
  
  for(int h=0;h<numberOfInputs;h++){
    fscanf(fin,"%d\n",&n);
    
    count=0;
    for(int h=1;h<n;h++){
      tmp=getPossibles(h,n);
      count+=tmp;
      count=count%100003;  
    }
    
    
    fprintf(fout,"Case #%d: %d\n",h+1,count);
  }
  
  //Global things
  fclose(fin);
  fclose(fout);   
}
