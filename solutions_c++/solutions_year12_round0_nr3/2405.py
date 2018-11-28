#include<cstdio>

#define maxN 2000005
#define maxLog 10

int T;
int A,B;
int n,m;
int used[maxLog],last;
int log,exp;
int sum;

int main(){
 scanf("%d",&T);
 int i,j,k;
 for(i=0;i<T;i++){
  sum = 0;
  scanf("%d%d",&A,&B);
  log = 0; j=A; exp=1;
  while(j>0){j/=10; log++; exp*=10; } exp/=10;
  for(n=A;n<B;n++){
   m = n;
   last = 0;
   for(j=0;j<log;j++){
    m = (m%10)*exp+m/10;
    if(m>B) continue;
    if(m>n){
     for(k=0;k<last;k++){
      if(used[k]==m) break;
     }
     if(k==last){ sum++; used[last++]=m; }
    }
   }
  }
  printf("Case #%d: %d\n",i+1,sum);
 }

 return 0;
}
