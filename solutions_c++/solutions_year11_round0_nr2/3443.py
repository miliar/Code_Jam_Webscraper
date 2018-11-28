#include <cstdio>
#include <set>
#include <map>
#include <list>
inline int min(int a, int b) {return a<b?a:b;}
inline int max(int a, int b) {return a<b?b:a;}

int main() {
  
  int z;
  scanf("%d", &z);
  
  for(int j = 0; j<z ; ++j) {
    std::set<std::pair<char,char> > opp;
    std::map<std::pair<char,char>,char> comb;
  
    int c;
    char str[4];
    scanf("%d", &c);
    for(int i=0; i<c; ++i) {
      scanf("%s", str);
      std::pair<char,char> p(min(str[0],str[1]),max(str[0],str[1]));
      comb[p] = str[2];
    }
    scanf("%d", &c);
    for(int i=0; i<c; ++i) {
      scanf("%s", str);
      std::pair<char,char> p(min(str[0],str[1]),max(str[0],str[1]));
      opp.insert(p);
    }
    std::list<char> list;
    scanf("%d ", &c);
    for(int i=0; i<c; ++i) {
      char ch;
      scanf("%c", &ch);
      list.push_back(ch);
    start:
      if(list.size() >= 2) {
	std::pair<char,char> p(min(list.back(),*(++list.rbegin())),max(list.back(), *(++list.rbegin())));
	std::map<std::pair<char,char>,char>::iterator k;
	if(( k = comb.find(p)) != comb.end()) {
	  list.pop_back();
	  list.pop_back();
	  list.push_back((*k).second);
	  goto start;
	}
	
	if(!list.empty()) for(std::list<char>::iterator i=list.begin(); i!=list.end(); i++ ) {
	  std::pair<char,char> q(min(*i,list.back()), max(*i,list.back()));
	  if(opp.find(q) != opp.end()) {list.clear();break;}
	}
      }
    }
    
    printf("Case #%d: [", j+1);
    for(std::list<char>::iterator i=list.begin(); i!=list.end(); i++ ) {
      if(i!=list.begin()) printf(", ");
      printf("%c", *i);
    }
    printf("]\n");
  }

}
