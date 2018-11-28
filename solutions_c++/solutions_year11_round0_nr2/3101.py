#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <list>

using namespace std;

int abs(int x) 
{
   return (x > 0) ? x : -x;
}

int main() {
  int cases, comb, op, ev;
  string temp;
  cin >> cases;
  
  for(int c = 1; c <= cases; c++) {
    map<pair<char,char>, char> combl;
    set<pair<char,char> > opl;
    
    cin >> comb;
    for(int i = 0; i < comb; i++) {
      cin >> temp;
      combl[make_pair(temp[0],temp[1])] = temp[2];
      combl[make_pair(temp[1],temp[0])] = temp[2];
    }
    
    cin >> op;
    for(int i = 0; i < op; i++) {
      cin >> temp;
      opl.insert(make_pair(temp[0],temp[1]));
      opl.insert(make_pair(temp[1],temp[0]));
    }
    
    cin >> ev;
    cin >> temp;
    list<char> elem;
    char result;
    for(int l = 0; l < ev; l++) {
      elem.push_back(temp[l]);
      
      if(elem.size() > 1) {
	
	while(elem.size() > 1) {
	  list<char>::iterator it = elem.end(), jt = --it;
	  jt--;
	  char result = combl[make_pair(*it, *jt)];
	  //cout << *it << " " << *jt << "-> " << result << endl;
	  if(result != 0) {
	    elem.insert(it, result);
	    elem.erase(it);
	    elem.erase(jt);
	  }else{
	    break;
	  }
	}
	bool cleared = false;
	for(list<char>::iterator it = elem.begin(); it != elem.end(); it++) {
	  list<char>::iterator jt = it;
	  jt++;
	  for(; jt != elem.end(); jt++) {
	    bool areop = opl.find(make_pair(*it,*jt)) != opl.end();
	    if(areop) {
	      elem.clear();
	      cleared = true;
	      break;
	    }
	  }
	  if(cleared)
	    break;
	}
      }
    }
    
    cout << "Case #" << c << ": [";
    for(list<char>::iterator i = elem.begin(); i != elem.end(); i++)
      if(i == elem.begin())
	cout << *i;
      else
	cout << ", " << *i;
    cout << "]" << endl;
  }
  
  return 0;
}