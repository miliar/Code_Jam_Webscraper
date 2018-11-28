#include <algorithm>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
using namespace std;

#define pi 3.1415926535897932384626433832795028841971
#define mp make_pair
#define x first
#define y second
#define FOR(i,a,b) for (long _n(b), i(a); i < _n; i++)
#define CL(a) memset((a),0,sizeof(a))
#define VI vector <int>

int t,tt,n,m,k,l,A[10000];
string S[55];
double x,y;
bool b;

void ch(int i,int j)
{
  S[i][j]='/';
  S[i+1][j]=char(92);
  S[i][j+1]=char(92);
  S[i+1][j+1]='/';  
}


int main ()
{
  freopen ("input.txt","r",stdin);
  freopen ("output.txt","w",stdout);
  cin >> tt;
  FOR(t,1,tt+1)
  {
    int bl=0,rd=0;
    cin >> n>>m;
    FOR(i,0,n)
    cin >> S[i];
    FOR(i,0,n)
    FOR(j,0,m)
    if (S[i][j]=='#') bl++;
    if (bl%4!=0) b=true; else b=false;
    if (!b)
    {
      FOR(i,0,n)
      FOR(j,0,m)
      if ((S[i][j]=='#')&&(S[i+1][j]=='#')&&(S[i][j+1]=='#')&&(S[i+1][j+1]=='#')) ch(i,j);
      FOR(i,0,n)
      FOR(j,0,m)
      if (S[i][j]=='#')b=true;      
    }
    cout << "Case #"<<t<<":"<<endl;
    if (b) cout << "Impossible"<<endl;else
    {
      FOR(i,0,n)
      cout <<S[i]<<endl;      
    }
    
    
  } 
  return 0;
}