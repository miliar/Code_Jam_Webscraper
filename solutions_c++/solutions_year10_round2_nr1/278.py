#include <iostream>
#include <map>

using namespace std;

class node {
  map<string, node*> children;
public:
  int add(string s, size_t pos) {
    //std::cerr << reinterpret_cast<void*>(this) << "::add(" << s << ", " << pos << "):";
    if(pos>=s.size()) return 0;
    size_t slash = s.find('/', pos);
    string next;
    //std::cerr << "slash==" << slash << '\n';
    if(slash == string::npos){
      next = s.substr(pos, string::npos);
      if(children.count(next)) return 0;
      else {
	children[next] = new node;
	return 1;
      }
      return 1;
    } else {
      next = s.substr(pos, slash-pos);
      if(children.count(next)) return children[next]->add(s, slash+1);
      else {
	children[next] = new node;
	return 1+ children[next]->add(s, slash+1);
      }
    }
  }

  ~node() {
    for(map<string, node*>::iterator it=children.begin();it!=children.end();++it)
      delete it->second;
  }
};

node* root;

int main() {
  int t;
  cin >> t;
  for(int tcase=1;tcase<=t;tcase++){
    int n, m;
    cin >> n >> m;
    root = new node();
    for(int i=0;i<n;i++){
      string s;
      cin >> s;
      root->add(s, 1);
    }

    int res = 0;
    for(int i=0;i<m;i++){
      string s;
      cin >> s;
      res += root->add(s, 1);
    }

    cout << "Case #" << tcase << ": " << res << '\n';
    delete root;
  }
}
