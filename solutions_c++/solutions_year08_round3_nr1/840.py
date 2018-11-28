#include<stdio.h>
void sort(int n,int data[]){
  int i,j;
  int x;
  for(i=0;i<n-1;i++)
    for(j=i+1;j<n;j++)
      if(data[i]<data[j]){
        x=data[i];
        data[i]=data[j];
        data[j]=x;
      }
}

int main(){
  int n;
  int p,k,l,L[1000],press;
  int i,j,h;
  
  scanf("%i",&n);
  for(i=0;i<n;i++){
    press=0;
    scanf("%i%i%i",&p,&k,&l);
    for(j=0;j<l;j++) scanf("%i",&L[j]);
    sort(l,L);
    for(j=h=0;h<p;h++){
      while(j<k*(h+1)){
        if(j>=l) goto a;
        press+=(h+1)*L[j];
        j++;
      }
    }  
    a:
    printf("Case #%i: %i\n",i+1,press);   
  }
  return 1;
}
