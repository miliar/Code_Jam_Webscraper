#include<iostream>
#include<algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>



using namespace std;

int main(){
  int C;
  cin >> C;
  for(int caso=1;caso<=C;caso++){
    int N;
    cin >> N;
    int X[10],Y[10],R[10];
    for(int i=0;i<N;i++){
      cin >> X[i];
      cin >> Y[i];
      cin >> R[i];
    }
    double res=123123123.0;
    if(N==1){
      res = R[0];
    }
    else if(N==2){
      res = (R[0]>R[1])?R[0]:R[1];
    }else {
      for(int i=0;i<3;i++){
	double pri=R[i];
	int dx=X[(i+1)%3]-X[(i+2)%3];
	int dy=Y[(i+1)%3]-Y[(i+2)%3];
	double seg = (sqrt(dx*dx+dy*dy)+R[(i+1)%3]+R[(i+2)%3])/2.0;
	double alt= (pri > seg)? pri: seg; 
	res = (res < alt) ? res :alt;
      }
    }
    cout << "Case #"<<caso<<": " << res << endl;
  }
  return 0;
}
