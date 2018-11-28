#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int main(){
   freopen("Portal.in", "r", stdin);
  freopen("Portal.out", "w", stdout);
   
   int testcases, n, time = 0, x;
   char rob;
   scanf("%d\n", &testcases);
   
   for(int i = 0; i < testcases; i++){
     scanf("%d ", &n);
      int o = 1;
      int b = 1;
      int otime = 0;
      int btime = 0;
      time = 0;
     for(int j = 0; j < n; j++){
       cin >> rob >> x;
       if(rob == 'O'){
	 if(abs(x-o) <= otime){
	  time += 1;
	  btime += 1;	   }
	 else{
	   time += abs(x-o) + 1 - otime;
	   btime += abs(x-o) + 1 - otime;}
	  o = x;
	  otime = 0;
	  //cout << "	" << time << endl;
	  } 
	else{
	  if(abs(x-b) <= btime){
	    time += 1;
	    otime += 1;
	  }
	  else{
	    time += abs(x-b) + 1 - btime;
	    otime += abs(x-b) + 1 - btime;
	    }
	  b = x;
	  btime = 0;
	 // cout << "	"  << time << endl;
	  } 
	}
     printf("Case #%d: %d\n", i+1, time);
  }
   
   return 0;
}