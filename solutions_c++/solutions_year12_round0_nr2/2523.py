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
  int c;
  scanf("%d", &c);
  int n,s,p;
  int x = c;
  while(c--){
	int count = 0;
	vector<int> sc;
	cin>>n>>s>>p;

	for(int i=0; i<n; i++){
	  int t;
	  cin>>t;
	  sc.push_back(t);
	}

	if(p==0) {count = n; cout<<"Case #"<<x-c<<": "<<count<<endl; continue;}

	sort(sc.begin(), sc.end());

	int i;
	for(i = sc.size()-1; i>-1; i--){
	  if(sc[i] < (3*p-2)) break;
	  //cout<<sc[i]<<" "<<3*p-2<<endl;
	  count++;
	}

	int z = s;
	for (; i>-1 && s>0; i--){
	  if(sc[i] >= 3*p-4 && sc[i] >0 && s>0)
	  {count++;s--;}
	}
	cout<<"Case #"<<x-c<<": "<<count<<endl;
  }
  return 0;
}
