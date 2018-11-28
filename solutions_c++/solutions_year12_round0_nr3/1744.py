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

int A,B;
set<int> h;

int generate (int i){
  h.clear();
  char s[8];
  sprintf(s,"%d",i);
  int len = strlen(s);
  char s2[15] = "";
  strcat(s2,s);
  strcat(s2,s);
  char temp[8];
  int count = 0;
  for(int k = 1; k<len; k++){
    strncpy(temp,s2+k,len);
    if(temp[0] == '0') continue;
    int j = atoi(temp);
    if(j != i && j >= A && j <= B && h.count(j)==0){
      count++;
      h.insert(j);
    }
  }
//  cout<<i<<" "<<count<<endl;
  return count;
}

int main (){
  int t;
  scanf("%d",&t);
  int n = t;
  while(t--){
    ll count = 0;
    cin>>A>>B;
    for(int i=A; i<=B; i++){
      int temp = generate(i);
      //if(temp) cout<<i<<" "<<temp<<endl;
      count += temp;
    }
    cout<<"Case #"<<n-t<<": "<<count/2<<endl;
  }
  return 0;
}
