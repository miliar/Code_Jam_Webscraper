#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <set>
using namespace std;

int m(string t) {
  stringstream h(t.substr(0,2));
  stringstream m(t.substr(3,2));
  int ho, mi;
  h >> ho;
  m >> mi;
  return (60*ho+mi);
}
  
struct point {
  int start;
  int end;
  int root;
  int id;
  int child;
};
bool operator<(const point& a, const point& b) {
  //  if(a.end!=b.end) 
  //    return a.end<b.end;
  return a.start<=b.start;
}

int main() {
  int c=1;
  string l;
  getline(cin,l);
  stringstream t1(l);
  int ncases;
  t1 >> ncases;
  while(ncases--) {
    getline(cin,l);
    stringstream tt(l);
    int tat;
    tt >> tat;
    getline(cin,l);
    stringstream t2(l);
    int a,b;
    t2 >> a >> b;
    vector<point> A;
    int id =0;
    while(a--) {
      getline(cin,l);
      point p;
      p.start=m(l.substr(0,5));
      p.end=m(l.substr(6,5)) + tat;
      p.child=-1;
      A.push_back(p);
    }
    vector<point> B;
    while(b--) {
      getline(cin,l);
      point p;
      p.start=m(l.substr(0,5));
      p.end=m(l.substr(6,5)) + tat;
      p.child =-1;
      B.push_back(p);
    }
    sort(A.begin(),A.end());
    sort(B.begin(),B.end());
    for(int i=0;i<A.size();i++) A[i].id = A[i].root = i;
    for(int i=0;i<B.size();i++) B[i].id = B[i].root = i + A.size();

    for(int i=0;i<A.size();i++) {
      for(int j=0;j<B.size();j++) {
	  if(B[j].root == B[j].id && A[i].end <= B[j].start) {
	    B[j].root = A[i].root;
	    A[i].child = B[j].id;
	    break;
	  }
      }
    }
    for(int i=0;i<B.size();i++) {
      for(int j=0;j<A.size();j++) {
	if(A[j].root == A[j].id && B[i].end <= A[j].start) {
	  A[j].root = B[i].root;
	  if(A[j].child != -1) B[A[j].child-A.size()].root = B[i].root;
	  B[i].child = A[j].id;
	  break;
	}
      }
    }
    
    set<int> na;
    set<int> nb;
    for(int i=0;i<A.size();i++) {
      //  cout << "Case #"<<c << " A.start " << A[i].start << " A.end " << A[i].end << " root " << A[i].root << endl;
      if(A[i].root<A.size()) {
	na.insert(A[i].root);
      }
    }
    for(int i=0;i<B.size();i++) {
      //      cout << "Case #" << c << " B.start " << B[i].start << " B.end " << B[i].end << " root " << B[i].root << endl;
      if(B[i].root>=A.size()){
	nb.insert(B[i].root); 
      }
    }
    cout << "Case #"<< c++ << ": " << na.size() << " " << nb.size() << endl;
  }
  return 0;
}
    
    

