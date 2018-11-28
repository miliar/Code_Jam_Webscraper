#define _CRT_SECURE_NO_WARNINGS
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define repd(i,n) for (int i((n)-1); i >= 0; --i)
#define rep2(i,x,m) for(int i=x;i<m;i++)
#define rep2d(i,x,m) for(int i=x;i>=0;i--)
#define repit(i,c) for (typeof((c).end()) i=(c).begin(); i!=(c).end(); ++i)
#define fill(a,c) memset(&a, c, sizeof(a))
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()

int main()
{
 freopen("C-large.in","r",stdin);
 freopen("oo.txt","w",stdout);
 int i,j,k,N,c,l;
 int v[1000],v1[1000];
 int take,prison=0;
 cin>>N;
 while(prison++<N)
 {
  int mine[150][150]={0};
  int bribe[1001]={0};
  cin>>l>>c;
  v1[0]=0;
  rep(i,c)
   {
    cin>>v[i];
    v1[i+1]=v[i];
   }
   
  v[c]=l;
  rep(i,c+1)
     mine[i][i]=0;
     
  rep2(i,1,c+1)
  {
    rep(j,c-i+1)
     {
        take=0;
        rep2(k,j,i+j)
        {
          bribe[take++]=mine[j][k]+mine[k+1][i+j];
        }
        mine[j][j+i]=bribe[min_element(bribe,bribe+take)-bribe]+v[j+i]-v1[j]-2;
        if(v[j+i]==l) mine[j][j+i]++;
      }
   }
   cout<<"Case #"<<prison<<": "<<mine[0][c]<<endl;
     
  }
  return 0;
}

