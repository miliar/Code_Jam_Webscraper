using namespace std;
#include <cmath>
#include <cstdio>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
typedef long long ll; 
typedef pair<int,int> pii; 
#define FOR(i,n) for (int i = 0; i < n; i++)
#define SZ(x) ((int)x.size())
#define PB push_back
#define MP make_pair
#define sf(x) scanf("%d",&x)
#define pf(x) printf("%d\n",x)
#define split(str) {vs.clear();istringstream ss(str);while(ss>>(str))vs.push_back(str);}
#define PI 3.141592653589793
int winner(vector<char> v) //v contains 4 elements. returns 0 for none 1 for X and 2 for O
{
  int x = 0, o = 0, t = 0;
  FOR(i,v.size())
  {
    if(v[i] == 'X')
      x++;
    else if(v[i] == 'O')
      o++;
    else if(v[i] == 'T')
      t++;
  }
  if(t == 1 || t == 0)
  {
    if(t + x == 4)
      return 1;
    else if(t + o == 4)
      return 2;
  }
  return 0;
}

int main()
{
  int t;
  sf(t);
  int temp = t;
  while(t--)
  {
    cout<<"Case #"<<temp - t<<": ";
    vector<vector<char> > v(7,vector<char>(10,'K'));
    
    FOR(i,4)
    {
      string s;
      cin>>s;
      FOR(j,4)
      {
	v[i][j+3] = s[j];
      }
    }
    
    bool notc = false, xwon = false, owon = false;
    
    FOR(i,4)
    {
      int var;
      for(int j = 3; j<7; j++)
      {
	if(v[i][j] == '.') notc = true;
	
	vector<char> dig;
	FOR(k,4)
	  dig.PB(v[i][j+k]);
	  
	var = winner(dig);
	if(var == 1)xwon = true;
	else if(var == 2)owon = true;
	  
	dig.clear();
	FOR(k,4)
	  dig.PB(v[i+k][j+k]);
	var = winner(dig);
	if(var == 1)xwon = true;
	else if(var == 2)owon = true;
	  
	dig.clear();
	FOR(k,4)
	  dig.PB(v[i+k][j]);  
	var = winner(dig);
	if(var == 1)xwon = true;
	else if(var == 2)owon = true;
	  
	dig.clear();
	FOR(k,4)
	  dig.PB(v[i+k][j-k]);  
	var = winner(dig);
	if(var == 1)xwon = true;
	else if(var == 2)owon = true;
	
	if(xwon || owon) goto exit;
      }
    }
    
    exit:
    if(xwon)
      cout<<"X won"<<endl;
    else if(owon)
      cout<<"O won"<<endl;
    else if(notc)
      cout<<"Game has not completed"<<endl;
    else
      cout<<"Draw"<<endl;
  }
}