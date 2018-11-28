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

    freopen("B.in", "rt", stdin);
    freopen("B.out", "wt", stdout);
    int t = 0 , T,x,y,c;
    cin>>T;
    while(t++<T)
    {
       double cnt = 1;
       cin>>x>>y>>c;
       while(ceil((double)y/c)>x) 
       {
         cnt+=1;
         int s = y%c;
         y/=c;
         if(s)y++;
       }
       if( cnt == 0)
       {
            printf("Case #%d: 0\n",t);continue;
       }
       int u = ceil(log2(cnt));
       printf("Case #%d: %d\n",t,u);
    }
  //  system("pause");
    return 0;
}
