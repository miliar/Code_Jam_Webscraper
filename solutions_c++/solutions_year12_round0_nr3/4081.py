#include<cstdio>
#include<cmath>
#include<map>

using namespace std;



int 
get_no_of_d(int n){
  int count=0;
  while(n){
    n=n/10;
    count++;
  }
  return count;
}

int get_number_of_pair(int n, int B){
  int temp =n;
  int no_of_digit = get_no_of_d(n);
  int div=10;
  int q;
  int count=0;
  int i=0;
  map<int, int> m;

  while(temp){
    int q = n % div; 
    temp = n/div;
    int number = q*pow(10, no_of_digit - i -1) + temp;
    if(number <=B && number > n){
      if(m.find(number) == m.end()){
        m[number] =n;
        count++;
      } else {
        //printf("dup:%d %d\n", number, n);
      }
    }
    i++;
    div = div*10;
  }
  return count;

}

void get_solution(){
  int t;
  int a, b;
  
  scanf("%d", &t);
  for(int i=1; i<=t;i++){
    printf("Case #%d: ", i);
    scanf("%d", &a); scanf("%d", &b);
    int count=0;
    while(a<=b){
      count+=get_number_of_pair(a, b);
      a++;
    }
    printf("%d\n", count);
      
  }

}

int main(){
  get_solution();
  return 0;
}


    
  
