#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

int main(int argc, char** argv){
  int T;
  cin>>T;
  int cas = 1;
  while(T--){  
    int A,B;
    cin>>A>>B;
    int y = 0;
    int num = A;
    int numdigit = (int)floor(log10(A))+1;
    while(num<=B){
      int nums[8];
      for(int i=1; i<numdigit; i++){
        int div = pow(10,i);
        int mul = pow(10,numdigit-i);
        int a = ((int)(num%div))*mul;
        int b = (int)(num/div);
        int newnum = a+b;
        nums[i] = newnum;
        if(newnum>num && newnum<=B && ((int)floor(log10(newnum))+1 == numdigit)){
          for(int j=0;j<i;j++){
            if(nums[j] == newnum){
              y--;
              break;
            }
          }
          y++;
        }
      }
      num++;
    }
    if(A<10)
      y=0;
    cout<<"Case #"<<cas<<": "<<y<<endl;
    cas++;
  }
  return 0;
}
