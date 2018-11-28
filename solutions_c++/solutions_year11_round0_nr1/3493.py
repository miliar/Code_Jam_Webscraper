#include <iostream>
#include <cstdio>
#include <queue>
#include <utility>

using namespace std;

queue<int> oq,bq,bothq;

int main(){

  int t,n,p,b,o,time;
  char r;
  
  scanf("%d", &t);
  for(int T=0; T<t; T++){
    time = 0;
    scanf("%d", &n);
    for(int i=0; i<n; i++){
      scanf(" %c %d", &r, &p);
      if(r == 'O'){
	bothq.push(0);
	oq.push(p);
      }else{
	bothq.push(1);
	bq.push(p);
      }
    }
    
    b=o=1;
    //start
    while(!bothq.empty()){
      if(bothq.front() == 0){
	//O has to push
	if(o==oq.front()){
	    oq.pop();
	    bothq.pop();
	} else {
	  if(o < oq.front())
	    o++;
	  else if(o >oq.front())
	    o--;
	}
	if(b < bq.front())
	  b++;
	else if(b > bq.front())
	  b--;
	  
      } else {
	//B has to move
	if(b==bq.front()){
	    bq.pop();
	    bothq.pop();
	} else {
	  if(b < bq.front())
	    b++;
	  else if(b >bq.front())
	    b--;
	}
	if(o < oq.front())
	  o++;
	else if(o > oq.front())
	  o--;
      }
     
      time++;
    }
    printf("Case #%d: %d\n", T+1, time);  
    
    
  }
  
  return 0;
}