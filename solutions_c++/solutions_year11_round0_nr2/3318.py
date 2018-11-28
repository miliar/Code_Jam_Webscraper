#include <iostream>
#include <cstdio>
#include <queue>
#include <utility>
#include <map>
#include <string>

using namespace std;

map<string, char> mc, md;
map<string, char>::iterator it;

string s,s1;

int main(){

  int t,c,d,n;
  char c1,c2,c3;
  
  scanf("%d", &t);
  for(int T=0; T<t; T++){
    scanf("%d", &c);
    for(int i=0; i<c; i++){
      scanf(" %c%c%c", &c1, &c2, &c3);
      //add to c map
      s.clear();
      s += c1; s+= c2;
      mc[s] = c3;
      s.clear();
      s += c2; s+= c1;
      mc[s] = c3;
    }
    scanf("%d", &d);
    for(int i=0; i<d; i++){
      scanf(" %c%c", &c1, &c2);
      //add to d map
      s.clear();
      s += c1; s+= c2;
      md[s] = 'a';
      s.clear();
      s += c2; s+= c1;
      md[s] = 'a';
    }
    scanf("%d ", &n);
    s.clear();
    for(int i=0; i<n; i++){
      scanf("%c", &c1);
      //process
     // cout << s << endl;
      if(s.length() == 0){
	s += c1;
      } else {
	s1.clear();
	s1 += c1; s1 += s[s.length()-1];
	if(mc.find(s1) != mc.end()){
	  s[s.length()-1] = mc[s1];
	} else {
	  //find if we delete all
	  int j,le;
	  le = s.length();
	  for(j=0; j<s.length();j++){
	    s1[1] = s[j];
	    if(md.find(s1) != md.end()){
	      s.clear();
	      break;
	    }
	  }
	  if(j==le)
	    s += c1;
	}
      }
    }
    
    
    printf("Case #%d: [", T+1);
    for(int i=0; i<s.length(); i++){
      printf("%c", s[i]);
      if(i<s.length()-1){
	printf(", ");
      }
    }
    printf("]\n");  
    
    mc.clear();
    md.clear();
    
    
    
  }
  
  return 0;
}