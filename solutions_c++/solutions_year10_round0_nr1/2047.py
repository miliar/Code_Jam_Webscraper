#include<iostream>
using namespace std;
int main(){
  int N,K,T,kase,i;
  scanf("%d",&T);
  for(kase=1;kase<=T;kase++){
	scanf("%d %d",&N,&K);
	if(K%(1<<N) == ((1<<N) - 1))
	  printf("Case #%d: ON\n",kase);
	else
	  printf("Case #%d: OFF\n",kase);
  }
  return 0;
}

	  