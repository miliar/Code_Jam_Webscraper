#include<iostream>
#include<vector>
#include<map>
#include<cassert>
#include<cstring>

using namespace std;

struct node_t {
  map<char, vector<node_t*> > child;  
  ~node_t(){
    for(map<char, vector<node_t*> >::iterator it=child.begin(); it!=child.end();++it){
      vector<node_t*>& v = it->second;
      for(int i=0;i<v.size();++i)
	delete v[i];
      v.clear();
    }
  }
};

int search(const char* cp, node_t* const cur){
  int ret = 0;
  if(*cp == 0) return 1;
  if(cur->child.empty()) return 0;
  //  cout << *cp << endl;

  if(*cp == '('){
    while(*cp && *cp != ')'){
      if(cur->child.find(*cp) != cur->child.end()){
	vector<node_t*>& v = cur->child[*cp];
	for(int i=0;i<v.size();++i)
	  ret += search(strchr(cp, ')')+1, v[i]);
      }
      ++cp;
    }
  }else{
    if(cur->child.find(*cp) != cur->child.end()){
      vector<node_t*>& v = cur->child[*cp];
      for(int i=0;i<v.size();++i)
	ret += search(cp+1, v[i]);
    }
  }
  return ret;
}

int main(){
  int L, D, N;
  cin>>L>>D>>N;

  node_t root;

  for(int i=0;i<D;++i){
    string str;cin>>str;
    node_t* cur = &root;
    assert(str.size() == L);
    for(int j=0;j<L;++j){
      node_t* n = new node_t;
      cur->child[str[j]].push_back(n);
      cur = n;
    }
  }
  for(int t=0;t<N;++t){
    string str; cin >> str;
    cout << "Case #" << (t+1) << ":" << " " << search(str.c_str(), &root) << endl;
  }
}
