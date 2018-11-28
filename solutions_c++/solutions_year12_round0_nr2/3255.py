#include<cstdio>
#include<string>
#include<iostream>
using namespace std;
int main(){
  int T,N,S;
  scanf("%d",&T);
  for(int z=0;z<T;z++){
    int N,S,M;
    int i,count=0,pre=0;
    scanf("%d%d%d",&N,&S,&M);
    int *c;
    c=new int[N];
    for(i=0;i<N;i++){
      scanf("%d",&c[i]);
    }
    for(i=0;i<N;i++){
      if(c[i]%3==1){
        if((c[i]/3)+1>=M){
          count++;
          continue;
        }
      }
      else if(c[i]%3==2){
        if((c[i]/3)+1>=M){
          count++;
          continue;
        }
        if((c[i]/3)+2>=M&&(c[i]/3)>=0&&(c[i]/3)+2<=10)
          pre++;
      }
      else if(c[i]%3==0){
        if((c[i]/3)>=M){
          count++;
          continue;
        }
        if((c[i]/3)+1>=M&&(c[i]/3)-1>=0&&(c[i]/3)+1<=10)
          pre++;
      }
    }
    if(pre<S)
      count+=pre;
    else
      count+=S;
    printf("Case #%d: %d\n",z+1,count);
    delete[] c;
  }
	return 0;
}
