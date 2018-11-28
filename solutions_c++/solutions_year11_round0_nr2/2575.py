#include<cstdio>
#include<vector>
#include<iostream>
using namespace std;

int T=1, TC, C, D, N;
char c1, c2, c3;
char d1, d2, d3;
char l;

void di(vector<char> & list, const vector<char> & di);
bool com(vector<char> & list, const vector<char> & comb);

void print( const vector<char> & v);

int main()
{
  scanf("%d",&TC);
  for (T;T<=TC;T++)
  {
    vector<char> comb, dis;
    vector<char> list;
    vector<char> elements;
    int ic = 0, id = 0;
    int in = 0;
    for(scanf("%d ", &C); ic<C; ++ic)
    {
      scanf("%c%c%c ", &c1, &c2, &c3);
      comb.push_back(c1);
      comb.push_back(c2);
      comb.push_back(c3);
    }
    for(scanf("%d ", &D); id<D; ++id)
    {
      scanf("%c%c ", &d1, &d2);
      dis.push_back(d1);
      dis.push_back(d2);
    }
    for(scanf("%d ", &N);in<N; ++in)
    {
      scanf("%c", &l);
      elements.push_back(l);
    }
    //print(comb);
    for (int i = 0; i<elements.size(); ++i)
    {
      //list.push_back(comb(i,elements, comb));
      list.push_back(elements[i]);
      if (list.size()>1)
      {
        if(!com(list, comb))
        {
          di(list, dis);
        }


      }
    }
    print(list);
  }
}

void print( const vector<char> & v)
{
  cout <<"Case #" << T << ": ";
  cout << "[";
  int i = 0;
  if(!v.size()==0)
  {
  while (i<v.size()-1)
  {
    cout << v[i] << ", ";
    ++i;
  }
  cout << v.back();
  }
  cout << "]"<< endl;

}

bool com(vector<char> & list, const vector<char> & comb)
{
  for (int j = 0; j<comb.size(); j+=3)
  {
    if ((list.back() == comb[j] && list[list.size()-2]== comb[j+1])||
        (list.back() == comb[j+1] && list[list.size()-2] == comb[j])
       )
    { 
      list.pop_back();
      list.pop_back();
      list.push_back(comb[j+2]);
      return 1;
    }
  }
}

void di(vector<char> & list, const vector<char> & di)
 {
  for (int j = 0; j<di.size(); j+=3)
  {
    for (int k = 0; k<list.size(); ++k)
    {
      if ((list.back() == di.front()&& list[k]== di.back())||
          (list.back() == di.back() && list[k] == di.front())
         )
      { 
        list.clear();
        return;
      }
    }
  }
}
