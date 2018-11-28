#include<cstdio>


void get_solution(){
  int t;
  int s, p, n;
  int i=0;

  scanf("%d", &t);

  for(i=1;i<=t;i++){
    printf("Case #%d: ", i);
    scanf("%d", &n);
    scanf("%d", &s);
    scanf("%d", &p);

    int j, number, no_of_sur = 0;
    int count=0;
    for(j=0;j<n;j++){
      scanf("%d", &number);

      if(number - p < 0) continue;
      
      if(number - p >= 2*p-2) count++;
      else if(( number - p >= 2*p -3 )|| (number - p >= 2*p -4)){
        if(no_of_sur == s) continue;
        count++; no_of_sur++;
      }
    }
    printf("%d\n", count);
  }
}

int main(){
  get_solution();
  return 0;
}
        
      
      

