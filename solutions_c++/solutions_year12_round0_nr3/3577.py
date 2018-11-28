#include<stdio.h>
#include<stdlib.h>
#include<set>

using namespace std;
int number;
int first, second;
int result=0;
int array[6];
set<int> myset;

int count(int num, int first, int second, int digits){
  myset.clear();
  for(int j=0; j<digits; ++j){
    num = (num/10) + array[digits-1]*(num%10);
    if(num<=second && num>=first){
      myset.insert(num);
    }
  }
  return myset.size()-1;
}

int main(){
  for(int i=0; i<6; ++i){
    if(i==0){
      array[i]=1;
    }
    else{
      array[i]=array[i-1]*10;
    }
  }
  scanf("%d", &number);
  for(int i=0; i<number; ++i){
    scanf("%d", &first);
    scanf("%d", &second);
    result=0;
    int j=1;
    int k=0;
    while(j<=first){
      j=10*j;
      k++;
    }
    if(k!=1 && k!=7){
      for(int t=first; t<=second; ++t){
        result+=count(t, first, second, k);
      }
    }
    printf("Case #%d: %d\n", i+1, result/2);
  }
  return 0;
}
