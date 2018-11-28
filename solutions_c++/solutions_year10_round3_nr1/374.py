/*
ID: Manal Sadek
LANG: C++
TASK:
*/

#include <map>
#include <set>
#include <math.h>
#include <deque>
#include <stack>
#include <queue>
#include <vector>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <memory.h>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,s,m) for(int i=s;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define PI = (2.0 * acos(0.0));
typedef stringstream ss;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define OO ((int)1e9)


int main()
{

    freopen("A.in", "rt", stdin);
    freopen("A.out", "wt", stdout);
    int t =0, n,T;
    vector<pair<int,int> > v;
    cin>>T;
    while(t++<T)
    {
      cin>>n;
      int cnt = 0;
      v.clear();
      for(int i = 0 ; i < n ; i++)
      {
        int x , y;
        cin>> x>>y;
        v.push_back(make_pair(x,y)); 
      }
        for(int i = 0 ; i < n ; i++)
          for(int j = i+1 ; j < n ; j++)
            if(((v[i].first < v[j].first) + (v[i].second < v[j].second)) == 1) 
            cnt++;
      printf("Case #%d: %d\n",t,cnt);
    }
    //system("pause");
    return 0;
}
