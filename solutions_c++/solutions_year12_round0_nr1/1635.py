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
//   string str;
  char ch;
  scanf("%d", &t);
  scanf("%c", &ch);
  char map[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'}; 
  scanf("%c", &ch);
  int i=1;
  while(t--){
	cout<<"Case #"<<i<<": ";
	while(ch != '\n'){
// 	  cout<<ch;
	  if(ch != ' '){
		int c = ch-'a';
		cout<<map[c];
	} else cout<<" ";
	  scanf("%c", &ch);
	}
	cout<<"\n";
	scanf("%c", &ch);
	i++;
  }
  return 0;
}
