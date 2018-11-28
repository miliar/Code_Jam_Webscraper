#include <iostream>
#include <vector>
#include <set>
#include <cmath>

using namespace std;

struct node
{
  float weight;
  string sp;
  int t, f;
  
  node() { weight = 0.0; sp = ""; t = -1; f = -1; }
  node(float _weight, string _sp, int _t, int _f)
  { weight = _weight; sp = _sp; t = _t; f = _f; }
};

string off;
vector <node> tree;
set <string> ppp;
float probability;

void getProbability(int index)
{
  probability *= tree[index].weight;
  if (tree[index].sp == "") return;
  if (ppp.find(tree[index].sp) != ppp.end()) getProbability(tree[index].t);
  else getProbability(tree[index].f);
}

int get(int pos, int index)
{ 
  //cout << "!!!!!!" << pos << " " << index << endl; system ("pause");
  float w = 0.0; string name = "";bool answ = 0;
  int p = pos + 1;
  for (; p < off.size(); )
    { 
      //cout << off[p] << endl;
      if ( off[p] == ' ' ) { p++; continue; }
      if ( off[p] == '0' || off[p] == '1' ) 
        { 
          bool flag = 0; int cnt = 1;
          while ((off[p] >= '0' && off[p] <='9') || off[p] == '.')
            {
              if ( off[p] == '.' ) flag = 1;
              if ( off[p] != '.' )
                {
                  if (!flag) w = w * 10 + off[p] - '0';
                  else { w += (float)(off[p] - '0')/(float)pow(10.0,(double)(cnt)); cnt++; }
                }
              p++;
            }
        continue; }  
      if ( off[p] == '(' && !answ ) { /*cout << "old " << p << " ";*/ p = get(p, 2 * index + 1) + 1; /*cout << p << endl;*/ answ = 1; continue; }
      if ( off[p] == '(' &&  answ ) { /*cout << "old " << p << " ";*/ p = get(p, 2 * index + 2) + 1; /*cout << p << endl;*/ answ = 1; continue; }
      if ( off[p] >= 'a' && off[p] <='z') { p++; name = name + off[p - 1]; continue; }
      if ( off[p] == ')') break;
    }
  
  //cout << index << " " << answ << endl;  
  if (answ) tree[index] = node(w, name, 2 * index + 1, 2 * index + 2);
  else tree[index] = node(w, name, -1, -1);
  return p;
}

void Solve()
{
  int l; off = ""; 
  tree = vector <node> ();
  tree.resize(100000);
  
  scanf("%d\n", &l);
  for (int i = 0; i < l; i++)
    {
      string tmp;
      getline(cin,tmp);
      off = off + tmp;
    }
  //cout << off << endl;
  //system("pause");  
  get(0, 0);
      
  //cout << "tree ended" << endl;
  int a;
  scanf("%d", &a);
  for (int i = 0; i < a; i++)
    {
      ppp = set <string> ();
      char name[128];
      scanf("%s", &name);
      int tmp;
      scanf("%d", &tmp);
      for (int j = 0; j < tmp; j++)
        {
          scanf("%s", &name); ppp.insert(name);
        }
      probability = 1.0;
      getProbability(0);
      printf("%.7f\n", probability);
    }
  
}

int main()
{
  int tests;
  scanf("%d\n", &tests);
  for (int i = 1; i <= tests; i++)
    {
      printf("Case #%d:\n", i);
      Solve();
    }
    
  //system("pause");
  return 0;
}
