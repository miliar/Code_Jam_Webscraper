#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <memory>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

#define ll long long int
using namespace std;


int main (){
  int t;
  scanf("%d", &t);
  int N = t;
  while(t--){
	int n,s,p;
	scanf("%d%d%d", &n, &s, &p);
	int lim = 3*(p-1)+1;
	if(p-1 < 0) {
	  lim = 0;
	}
	int low = 3*(p-2)+2;
	int count = 0;
	int j;
	for(int i=0; i<n; i++){
	  cin>>j;
	  if(j >= lim){
		count++;
		continue;
	  } else {
		if(j>=low && s>0 && j>=p){
		  count++;
		  s--;
		}
	  }
	}
//	cout<<"Hello\n";
	cout<<"Case #"<<N-t<<	": "<<count<<endl;
  }
  return 0;
}
