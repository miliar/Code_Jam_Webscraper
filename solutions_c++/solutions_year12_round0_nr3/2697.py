#include <iostream>
#include <string>
#include <cstdlib>
#include<cstdio>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int countDigit(int num){
 int counter=0,divider=10;
 while(num/divider){
    divider=divider*10;
    counter++;
 }
return counter;
}



int main(){
  int a,b,r,digit,q,c,rep=0,counter=0;
scanf("%d",&c);
for(int k=0;k<c;k++){
  counter=0;
  scanf("%d %d",&a,&b);
  digit=countDigit(a);
  int* arrar=(int*)calloc(digit,sizeof(int));
  for(int i=a;i<=b;i++){
     q=i;
     for(int j=0;j<digit;j++){
     r=q%10;
     q=q/10;
     q=r*pow(10,digit)+q;
     for(int l=0;l<digit;l++){
        if(arrar[l]==q)
	rep=1;}    arrar[j]=q;
     if(q<b+1 && q>i && rep==0){
	++counter;}rep=0;
     }
  }
free(arrar);
cout<<"Case #"<<k+1<<": "<<counter<<endl;
}
return 0;
}
