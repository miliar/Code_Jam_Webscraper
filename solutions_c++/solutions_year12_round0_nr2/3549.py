#include<stdio.h>
#include<stdlib.h>
#include<algorithm>

using namespace std;
int number;
int amount;
int surprise;
int p;
int result;
int googlers[100];

int main(){
  scanf("%d", &number);
  for(int i=0; i<number; ++i){
    scanf("%d", &amount);
    scanf("%d", &surprise);
    scanf("%d", &p);
    for(int j=0; j<amount; ++j){
      scanf("%d", &googlers[j]);
    }
    int bonus = 0;
    result=0;
    p--;
    for(int j=0; j<amount; ++j){
      if(googlers[j]%3==0){
        if(googlers[j]/3>p){
          result++;
        }
        if(googlers[j]/3==p && googlers[j]!=0){
          bonus++;
        }
      }
      if(googlers[j]%3==1){
        if((googlers[j]/3)+1>p){
          result++;
        }
      }
      if(googlers[j]%3==2){
        if((googlers[j]/3)+1>p){
          result++;
        }
        if((googlers[j]/3)+1==p && googlers[j]!=29){
          bonus++;
        }
      }
    }
    bonus = min(bonus, surprise);
    result = result+bonus;
    printf("Case #%d: %d\n", i+1, result);
  }
  return 0;
}
