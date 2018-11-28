#include <iostream>
#include <cstdio>
#include <cstring>
#define MAXN 10000005
using namespace std;

typedef long long int ll;
int testcase,L,A,B,D[7]={1,10,100,1000,10000,100000,1000000},tmp;
ll ans,t1;
char input1[10],input2[10];
bool visit[MAXN];

int main(){
  freopen("C-large.in","r",stdin);
  freopen("ans.out","w",stdout);
  scanf("%d",&testcase);
  for(int TC=1;TC<=testcase;++TC){
    scanf(" %s %s",input1,input2);
    L = strlen(input1);
    sscanf(input1,"%d",&A);
    sscanf(input2,"%d",&B);
    ans = 0;
    for(int i=A;i<=B;++i){
    //  printf("i = %d\n",i);
      t1 = 0;
      for(int j=0;j<L;++j){
       // printf("%d mod %d * %d + %d / %d\n",i,D[j],D[L-j],i,D[j]);
        tmp = i%D[j]*D[L-j] + i/D[j];
      //  printf(" %d ",tmp);
        if(tmp >= A && tmp <= B) visit[tmp] = 1;
      }
     // printf("\n");
      for(int j=0;j<L;++j){
        tmp = i%D[j]*D[L-j] + i/D[j];
      //  printf("tmp = %d\n",tmp);
        if(tmp >= A && tmp <= B){
           // printf("hi %d\n",tmp);
           if(visit[tmp] && tmp < i){
       //   printf("%d adds to %d\n",tmp,i);
            ++t1;
          }
        }
        visit[tmp] = 0;
      }
    //  printf("i=%d: t1 = %d\n",i,t1);
      ans += t1;
    }
    printf("Case #%d: %lld\n",TC,ans);
  }
}
