#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <math.h>
using namespace std;

int max1=0;

void recycle(int num, int B){
 int temp1,temp2,temp3,mul=1,digits=0,temp4;
 temp1=num;
 while(temp1){
  temp1=temp1/10;
  digits++;
 }
 temp1=num;
 for(int i=0;i<digits;i++){
  temp2=temp1/mul;
  temp3=temp1%mul;
  temp4=temp3*(int)pow(10,digits-i) + temp2;
  mul=mul*10;
  if((temp4<=B) && (num<temp4) && (temp4/(int)pow(10,digits-1)!=0)){
   max1++;
//   cout<<num<<" "<<temp4<<endl;
  }
 }
}

int main() {
 ifstream r1("C-small-attempt0.in");
 int T;
 
 r1>>T;
 for(int i=0;i<T;i++){
  int A,B;
  r1>>A;
  r1>>B;
  max1=0;
  for(int j=A;j<B;j++){
   recycle(j,B);
  }
  cout<<"Case #"<<(i+1)<<": "<<max1<<endl;
 }
 
 return 0;
}
