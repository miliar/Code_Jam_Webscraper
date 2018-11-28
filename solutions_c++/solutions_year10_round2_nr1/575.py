#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){
  int c;

  cin >> c;
  for(int i=0;i<c;i++){
    int n, m;
    int ans=0;
    set<string> tree;
    tree.clear();
    string path;
    cin >> n >> m;
    for(int j=0;j<n;j++){
      cin >> path;
      for(int k=0;k<path.length();k++){
	if(path[k]=='/'&&k!=0){
	  tree.insert(path.substr(0,k));
	}
      }
      tree.insert(path);
    }
    tree.insert("/");
    for(int j=0;j<m;j++){
      cin >> path;
      for(int k=0;k<path.length();k++){
	if(path[k]=='/'&&k!=0){
	  int tmp=tree.size();
	  tree.insert(path.substr(0,k));
	  if(tmp<tree.size())ans++;
	}
	int tmpt=tree.size();
	tree.insert(path);
	if(tmpt<tree.size())ans++;
      }
    }  
    /*set<string>::iterator it=tree.begin();
    while(it!=tree.end()){
      cout << *it << endl;
      ++it;
      }*/
    printf("Case #%d: %d\n",i+1,ans);
  }
  return 0;
}
