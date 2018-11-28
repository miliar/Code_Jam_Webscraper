
#include <iostream>
#include<stdio.h>
using namespace std;

int main() {
	 int T;
	 scanf("%d", &T);
	  for (int Ti = 1; Ti <= T; ++Ti) {
		  int N;
		  scanf("%d", &N);
		  int array[N];
		  bool flag=false;
		  int result=0;
		  int sum=0;
		  int min=0;
		  for(int i=0;i<N;i++){
			  scanf("%d", &array[i]);
		  }
		  min=array[0];
		  for(int i=0;i<N;i++){
			  result^=array[i];
			  sum+=array[i];
			  if(min>array[i]) min=array[i];
		  }
		  if(result!=0){
			  printf("Case #%d: NO\n", Ti);
		  }
		  else
			  printf("Case #%d: %d\n", Ti, sum-min);
	  }
	  return 0;
}

