#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

int main(){
  int tmp, i, j, k, t, tc, q, p, pri[20000], num[200], min;
  scanf("%d",&tc);
  for(t=1;t<=tc;t++){
    scanf("%d%d",&p,&q);    
    for(i=0;i<q;i++)scanf("%d",&num[i]);
    for(i=1;i<=p;i++)pri[i]=1;
    tmp=p-1;
    pri[num[0]]=pri[0]=pri[p+1]=0;
    for(i=1;i<q;i++){
      k=j=0;
      while(pri[num[i]+k]!=0)k++;
      while(pri[num[i]-j]!=0)j++;
      tmp+=k+j-2;
      pri[num[i]]=0;
      //printf(" %d ",tmp);
    }
    min=tmp;
    while(next_permutation(num,num+q)){
      for(i=1;i<=p;i++)pri[i]=1;
      tmp=p-1;
      pri[num[0]]=pri[0]=pri[p+1]=0;
      for(i=1;i<q;i++){
	k=j=0;
	while(pri[num[i]+k]!=0)k++;
	while(pri[num[i]-j]!=0)j++;
	tmp+=k+j-2;
	pri[num[i]]=0;
	//printf(" %d ",tmp);
      }
      if(tmp<min)min=tmp;
    }
    printf("Case #%d: %d\n",t,min);

  }

  return 0;
}
