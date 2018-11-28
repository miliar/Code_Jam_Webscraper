#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <iterator>
using namespace std;

struct Tree{
  struct Tree *next;
  struct Tree *pre;
  map<string, struct Tree *> m;
};

int
serch(const char *r, Tree *t)
{
  if( *r != '/' ) return 0; //err
  r++;

  string s;
  while( *r != '/' && *r != '\0'){
    s += *r;
    r++;
  }

  //  cout<<s<<endl;

  int ans = 0;

  map<string, struct Tree*>::iterator itr;
  itr = t->m.find(s);
  if(itr == t->m.end()){
    ans++;
    Tree *c = new Tree;
    t->m.insert(make_pair(s, c));
    t->next = c;
    c->pre = t;    
    return serch(r, c) + 1;
  }

  return serch(r, (*itr).second);

}

void parser(const char *r, Tree *t)
{
  //  cout<<*r<<endl;
  if( *r != '/' ) return ; //err
  r++;

  string s;
  while( *r != '/' && *r != '\0'){
    s += *r;
    r++;
  }

  map<string, struct Tree*>::iterator itr;
  itr = t->m.find(s);

  //  cout<<s<<endl;

  if(itr == t->m.end()){

    Tree *c = new Tree;


    t->m.insert(make_pair(s, c));
    t->next = c;
    c->pre = t;
    parser(r, c);
  }
  else parser(r, (*itr).second);
}

int
main()
{
  char c[101];
  int t;
  stringstream ss;

  cin.getline(c, 101);
  ss<<c;
  ss>>t;

  for(int i = 0; i < t; i++){
    stringstream sn;
    int n, m;
    cin.getline(c, 101);
    sn<<c; sn>>n>>m;

    //    cout<<n<<" "<<m<<endl;

    Tree root;

    for(int j = 0; j < n; j++){
      cin.getline(c, 101);
      string s(c);

      //cout<<s<<endl;

      parser(s.c_str(), &root);
    }

    int ans = 0;
    for(int j = 0; j < m; j++){
      cin.getline(c, 101);
      string s(c);
      ans += serch(s.c_str(), &root);
    }
   
    cout<<"Case #"<<i+1<<": "<<ans<<endl;

  }

}
