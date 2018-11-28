#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <list>
#include <math.h>

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define gp(ans) {cout << "Case #" << ((test)+1) << ": " << (ans) << endl;}

using namespace std;

typedef deque<string> DS;

class Node {
public:
  vector<Node*> childs;
  string name;
  Node () {
  }
  Node (string h_name) {
    name = h_name;
  }
  void addChild(Node* child) {
    childs.push_back(child);
  }
  Node* find(string h_name) {
    int len = childs.size();
    int i;
    REP(i,len) {
      Node* child = childs[i];
      string l_name = child->name;
      if (l_name == h_name) {
        return child;
      }
    }
    return NULL;
  }
};

DS split( string s, string c )
{
  DS ret;
  for (int i=0, n; i <= s.length(); i=n+1 ) {
    n = s.find_first_of( c, i );
    if( n == string::npos ) n = s.length();
    string tmp = s.substr( i, n-i );
    ret.push_back(tmp);
  }
  return ret;
}

int main () {
  int test, T;

  cin >> T;
  int N,M;
  int i,j,k;
  REP (test, T) {
    //TODO
    cin >> N;
    cin >> M;
    Node* root = new Node();
    REP(i,N) {
      string path;
      cin >> path;
      DS pathv = split(path,  "/");
      int len = pathv.size();
      Node* cur = root;
      for(j=1;j<len;j++) {
        string s = pathv[j];
        if (s == "") {
          continue;
        }
        //cout << s << ":";
        Node* child = cur->find(s);
        if (child != NULL) {
          cur = child;
        } else {
          child = new Node(s);
          cur->addChild(child);
          cur = child;
        }
      }
    }
    int count = 0;
    REP(i,M) {
      string path;
      cin >> path;
      DS pathv = split(path,  "/");
      int len = pathv.size();
      Node* cur = root;
      for(j=1;j<len;j++) {
        string s = pathv[j];
        if (s == "") {
          continue;
        }
        //cout << s << ":" << endl;
        Node* child = cur->find(s);
        if (child != NULL) {
          cur = child;
        } else {
          child = new Node(s);
          count++;
          //cout << "add:" << s << endl;
          cur->addChild(child);
          cur = child;
        }
      }
    }
    gp(count);
  }
  return 0;
}

