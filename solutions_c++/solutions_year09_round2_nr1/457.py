#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")

using namespace std;

struct vertex{
  string feature;
  double prob;
  int idx;
  
  vertex(){
  }
  
  vertex(string _feature, double _prob, int _idx){
    feature = _feature;
    prob = _prob;
    idx = _idx;
  }
};

string tree;

map<pair<string, int>, pair<vertex, vertex> > mapa;

pair<vertex, int> parse(int sidx, int eidx){
  while (tree[sidx] != '(')
    sidx++;
    
  int co = 1, i = sidx + 1;
  while (co){
    if (tree[i] == ')')
      co--;
    else if (tree[i] == '(')
      co++;
    i++;
  }
    
  eidx = i - 1;
  while (tree[sidx] < '0' || tree[sidx] > '9')
    sidx++;

  double p = 0.0;
  while (tree[sidx] >= '0' && tree[sidx] <= '9'){
    p = p * 10.0 + tree[sidx] - '0';
    sidx++;
  }
  
  if (tree[sidx] == '.'){
    sidx++;
    int st = 10;
    while (tree[sidx] >= '0' && tree[sidx] <= '9'){
      p = p  + (tree[sidx] - '0') / (1.0 * st);
      sidx++;
      st *= 10;
    }
  }


  while (tree[sidx] != ')' && (tree[sidx] < 'a' || tree[sidx] > 'z'))
    sidx++;
  
  string f = "";
  while (tree[sidx] >= 'a' && tree[sidx] <= 'z'){
    f += string() + tree[sidx];
    sidx++;
  }

  vertex v = vertex(f, p, sidx);
  if (f.sz){
    pair<vertex, int> r1 = parse(sidx, eidx - 1);
    pair<vertex, int> r2 = parse(r1.second + 1, eidx - 1);
    mapa[make_pair(f, sidx)] = make_pair(r1.first, r2.first);
  }
  
  return make_pair(v, eidx);
}

map<string, bool> cont;

double calc(vertex v){
  if (!v.feature.sz)
    return v.prob;
  
  pair<vertex, vertex> sons = mapa[make_pair(v.feature, v.idx)];
  double rr;
  if (cont[v.feature])
    rr = calc(sons.first);
  else
    rr = calc(sons.second);
    
  return v.prob * rr;
}

int main(){
  freopen("Al.out","wt", stdout);
  freopen("Al.in","r", stdin);
  int tests, l;
  scanf("%d\n", &tests);
  FOR (test, tests){
    scanf("%d\n", &l);
    tree = "";
    char str[200];
    FOR (i, l){
      gets(str);
      tree += string(str) + " ";
    }
    
    vertex root = parse(0, tree.sz - 1).first;
    cout << "Case #" << (test + 1) << ":" << endl;
    int a;
    scanf("%d", &a);
    string name;
    int cc;
    FOR (i, a){
      cont.clear();
      cin >> name >> cc;
      FOR (j, cc){
        cin >> name;
        cont[name] = true;
      }
      
      printf("%.7lf\n", calc(root));
    }
    
  }
  
  return 0;
}
