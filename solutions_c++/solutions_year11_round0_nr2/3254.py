#include <iostream>
#include <vector>
#include <map>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <list>
#include <stack>
#include <deque>

using namespace std;

#define FOR(i,a,b) for(int i=(a); i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define itype(c) __typeof((c).begin())
#define FORE(c,i) for(itype(c) i=(c).begin();i!=(c).end();++i)
#define PB push_back
#define PF pop_front
#define SORT(c) sort((c).begin(),(c).end());
#define SZ size()
#define PI acos(-1.)
#define HAS(c,e) (find((c).begin(),(c).end(),e)!=(c).end())
#define CHOMP string chomp;getline(cin,chomp)

typedef unsigned long long int ULL;

class Combination {
  public:
  string elems;
  char result;
  Combination (string,char);
  bool match(char,char);
};

Combination::Combination (string a,char b) {
  //cout<<"new comb "<<a<<" "<<b<<endl;
  elems=a; result=b;
}

bool Combination::match (char a,char b) {
  //cout << "checking if "<<a<<" and "<<b<<" can combine\n";
  if(elems[0]==a && elems[1]==b) return true;
  else if(elems[0]==b && elems[1]==a) return true;
  return false;
}

class Opposition {
  public:
  string elems;
  Opposition (string);
  bool match(deque<char>*,char);
};

Opposition::Opposition (string a) { 
  //cout<<"new opps "<<a<<endl;
  elems=a;
}

bool Opposition::match(deque<char>* st,char toBeInvoked) {
  //cout << "checking if "<<toBeInvoked<<" oppose "<<elems<<" stack size "<<st->size()<<endl;
  if(HAS((*st),elems[0]) && elems[1]==toBeInvoked) {
    //cout<<"true\n";
    return true;
  }
  else if(HAS((*st),elems[1]) && elems[0]==toBeInvoked) {
    //cout<<"true\n";
    return true;
  }
  return false;
}

int main()
{
  int Case;
  cin>>Case;
  REP(_case,Case)
  {
    int nCombine; cin>>nCombine; //read combinations 
    vector<Combination*> comb; 
    REP(i,nCombine) { 
      string s; cin>>s; char c=s[s.size()-1]; s.erase(s.end()-1); 
      comb.PB(new Combination(s,c));
    }
    int nOppos; cin>>nOppos; //read oppositions
    vector<Opposition*> oppos; REP(i,nOppos) { string s; cin>>s; oppos.PB(new Opposition(s)); }

    int nList;cin>>nList;
    deque<char> stack;
    string invokeList; cin>>invokeList;
    //cout<<"invoke list "<<invokeList<<endl;

    FORE(invokeList,c) {
      char toBeInvoked=*c;
      //check combinations
      bool matchFound=false;
      if(!stack.empty()) {
        char lastInvoked=stack.back();
	FORE(comb, _comb) {
	  if((*_comb)->match(lastInvoked,toBeInvoked)) { stack.pop_back(); stack.push_back((*_comb)->result); matchFound=true; break; }
	}
      }

      //check opposition and push if no oppos found
      if(!matchFound) {
//	cout<<"no match found\n";
	bool opposFound=false;
	if(!stack.empty()) FORE(oppos,_op) { if((*_op)->match(&stack,toBeInvoked)) { opposFound=true; break; }}
	if(opposFound) { /*delete<deque<char> > &stack;*/ /*cout<<"deleted\n";*/stack=*(new deque<char>());}
	else {
//	  cout << "pushing "<<toBeInvoked<<endl;
	  stack.push_back(toBeInvoked);
	}
      }

    }

 //   FORE(stack, c) cout<<*c<<endl;

    printf("Case #%d: [",_case+1);
    bool first=true;
    FORE(stack, c) { if(first) {cout<<*c;first=false;} else {cout<<", "<<*c;}}
    cout<<"]\n";
  }

  return 0;
}
