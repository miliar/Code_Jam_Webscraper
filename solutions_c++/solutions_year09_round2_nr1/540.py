#include<iostream>
#include<set>
#include<string>
#include<sstream>
#include<iomanip>
using namespace std;
set<string> m;
typedef long double ld;

string data;

bool getbracket(int& l, int& h) {
int lo = l;  while (data[lo] != '(') lo++;
    int cnt = 1; int hi = lo; bool f = false;
    while (cnt) {
      hi++; if (data[hi] == '(') {f=true;cnt++;} else if (data[hi]==')') cnt--;
    }
    l = lo; h = hi;
    return f;
}

class tree {
public:
  tree* t1;
  tree* t2;
  string f;
  ld w;

  tree (int l, int h) {
    bool more = getbracket(l,h);
//cout<<l<<" "<<h<<endl; cout<<data.substr(l+1, h-l-1)<<"**"<<endl;
    stringstream ss (data.substr(l+1, h-l-1));
    ss >> w;
    if (more) {
      ss >> f;
      int l1 = l+1; int h1 = h-1;
      getbracket(l1, h1);
      t1 = new tree(l1, h1);
      t2 = new tree(h1 + 1, h-1);
    }  else f="";   
  }
  ld evaluate() {
    if (f!="") {
      if (m.find(f) != m.end()) return w*t1->evaluate();
      else return w*t2->evaluate();
   } else return w;
  }
};


int main() {
  int N; 
  cin>>N; 
  for (int n = 1; n <= N; ++n) {
    cout<<"Case #"<<n<<":"<<endl;
    int t; cin>>t; cin.ignore();
string s;data="";
    while (t--) { getline(cin, s); data += s + " "; }
    //cout<<data<<endl;
    tree* p = new tree(0, data.length());
    cin >> t; while (t--) {
    cin >> s; int i;
    cin >> i;
    m.clear();
    while (i--) { cin>>s; m.insert(s); }
    cout<<setiosflags(ios::fixed)<<setprecision(7)<<p->evaluate()<<endl;
    }
  }
  return 0;
}