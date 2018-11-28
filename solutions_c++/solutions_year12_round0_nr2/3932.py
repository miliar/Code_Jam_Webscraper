#include <iostream>
#include <cstring>
#include <string>

using namespace std;

int T,N,S,p;
int normal_best[200];
int surprising_best[200];

void calcBests(int sum, int& normal, int& surprising){
  normal = -1;
  surprising = -1;

  if(sum%3==0){
    int t = sum/3;
    if(t>=0 && t<=10)
      normal = normal>t?normal:t;
  }
  
  if(sum%3==1){
    int t = (sum+2)/3;
    if(t-1>=0 && t<=10)
      normal = normal>t?normal:t;
  }

  if(sum%3==2){
    int t = (sum+1)/3;
    if(t-1>=0 && t<=10)
      normal = normal>t?normal:t;
  }

  if(sum%3==2){
    int t = (sum+4)/3;
    if(t-2>=0 && t<=10)
      surprising = surprising>t?surprising:t;
  }

if(sum%3==1){
  int t = (sum+2)/3;
  if(t-2>=0 && t<=10)
    surprising = surprising>t?surprising:t;
}

if(sum%3==0){
  int t = (sum+3)/3;
  if(t-2>=0 && t<=10)
    surprising = surprising>t?surprising:t;
 }
  
  return;
}

int main(){
  
  scanf("%d",&T);

  for(int i=0; i<T; i++){
    scanf("%d %d %d", &N,&S,&p);

    int sum,normal,surprising;
    for(int j=0; j<N; j++){
      scanf("%d",&sum);
      calcBests(sum,normal,surprising);
      normal_best[j] = normal;
      surprising_best[j] = surprising;
    }
    
    int result = 0;
    int S1 = S;
    
    for(int j=0; j<N; j++){
      if(!(normal_best[j]==-1 && surprising_best[j]!=-1))
	continue;

      S1--;
      if(surprising_best[j]>=p)
	result++;
    }

    for(int j=0; j<N; j++){
      if(!(normal_best[j]!=-1 && surprising_best[j]==-1))
	continue;

      if(normal_best[j]>=p)
	result++;
    }

    for(int j=0; j<N; j++){
      if(!(normal_best[j]!=-1 && surprising_best[j]!=-1))
	continue;

      if(normal_best[j]>=p){
	result++;
      }
      else if(normal_best[j]<p && surprising_best[j]>=p){
	if(S1>0){
	  S1--;
	  result++;
	}
      }
    }

    printf("Case #%d: %d\n",i+1,result);

  }
  
  return 0;
}
