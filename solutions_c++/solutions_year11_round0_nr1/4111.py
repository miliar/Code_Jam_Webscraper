#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <list>
#include <map>

using namespace std;

int main()
{
   int t;
   scanf("%d", &t);
   for(int i = 0; i < t;i++){
      list<int> os;
      list<int> bs;
      list<bool> as;
      int n, time;
      int ob=1, bb=1;
      scanf("%d", &n);
      for(int j = 0; j < n;j++){
	 char c[2];
	 int s;
	 scanf("%s %d", c, &s);
	 if(c[0]=='O'){
	    os.push_back(s);
	    as.push_back(true);
	 }
	 else{
	    bs.push_back(s);
	    as.push_back(false);
	 }
      }
      for(time=1;!as.empty();++time){
		  bool push = false;
	 if(!os.empty()){
	    if(ob==os.front()){
	       if(as.front()){
		//  printf("Orange Push button %d\n", os.front());
		  as.pop_front();
		  os.pop_front();
		push = true;
	       }
	    }
	    else{
	    //   printf("Orange Move\n");
	       if(ob>os.front())ob--;
	       else ob++;
	    }
	 }
	 if(!bs.empty()){
	    if(bb==bs.front()){
	       if(!as.front()&&!push){
		  as.pop_front();
		  bs.pop_front();
	       }
	    }
	    else{
	       if(bb>bs.front())bb--;
	       else bb++;
	    }
	 }
	 if(as.empty())
	    break;
      }
      printf("Case #%d: %d\n", i+1, time);
   }
   return 0;
}
