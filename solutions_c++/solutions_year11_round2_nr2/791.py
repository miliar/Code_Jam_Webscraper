#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;
int testcases, d, c, a, b;
int gatve[1001000];
//int gatvex[1001000];

bool ar_speja(double time, int v){
    double last = (double)gatve[0] - time;
    for(int i = 1; i < v; i++){
      //cout << last << " " << gatve[i] << endl;
      if( last + d <= gatve[i] - time ){
	last = gatve[i] - time; 
	//cout << "1as"; 
	continue;
      }
      if( (last + d) > (gatve[i] - time) &&  !(last + d  > gatve[i] + time) ){
	last = last + d; 
	//cout << "2as";
	continue;
      }
      if( (last + d > gatve[i] + time) )
	return false;
      
    }
  return true;
}

int main(){
  freopen("hotdog.in", "r", stdin);
  //freopen("x.out", "w", stdout);
  
  
  scanf("%d", &testcases);
  
  for(int test = 0; test < testcases; test++){
    int v = 0;
    scanf("%d %d", &c, &d);
    for(int i = 0; i < c; i++){
      scanf("%d %d", &a, &b);
      for(int j = 0; j < b; j++)
	gatve[v++] = a;
    }
    
    double left = 0.0, right = 200000000.0;
    while(right - left > 0.0000001){
      //cout << left << " " << right << endl;
      if( ar_speja( (double)(right + left)/2, v ) )
	right = (double)(right + left)/2;
      else
	left = (double)(right + left)/2;
    }
    
    cout << "Case #" << test+1 << ": " << left << endl;
    //for(int i = 0; i < v; i++)
    //  cout << gatve[i] << endl;
  }
  
  return 0;
}