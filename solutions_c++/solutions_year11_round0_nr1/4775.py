#include<iostream>
#include<cstdlib>
#include<cmath>
using namespace std;

int main(){
  int c,n,lastnum,lastpos,num,sum,time;
  char cl,lastcl;
  scanf("%d",&c);
  for(int i=0;i<c;i++){
    scanf("%d ",&n);
    sum=0;
    time=0;
    lastnum=1;
    lastpos=1;
    for(int j=0;j<n;j++){
      scanf("%c %d ",&cl,&num);
      //cout <<cl<<" "<<num<<"shitshit"<<endl;
      if(cl==lastcl||j==0){
	int k=abs(num-lastnum)+1;
	sum+=k;
	time+=k;
      }
      else{
	if(abs(num-lastpos)<=time){
	  time=1;
	  sum+=time;
	}
	else{
	  time=abs(num-lastpos)-time+1;
	  sum+=time;
	}
	lastpos=lastnum;
      }
      lastcl=cl;
      lastnum=num;
    }
    printf("Case #%d: %d\n",i+1,sum);
  }
  return 0;
}
