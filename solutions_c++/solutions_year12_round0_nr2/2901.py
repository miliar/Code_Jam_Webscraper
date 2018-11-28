 #include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <string>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;
#define fo(i,b) for(int (i) = 0;(i) < (b);++(i))
#define fo2(i,a,b) for(int (i) = (a);(i) < (b);++(i))
#define pb(a) push_back(a)
#define sz(X) ((int)(X.size()))//NOTES:SIZE(  
#define LENGTH(X) ((int)(X.length()))//NOTES:LENGTH(  
#define MP(X,Y) make_pair(X,Y)//NOTES:MP( 
#define vvi	vector<int>
#define all(a)	(a).begin(),(a).end()
#define iss istringstream
#define oss ostringstream
#define DEBUG(x) cout << (#x) << " " << x << endl;
template<class T> void stov(string s,vector<T> &res){istringstream sin(s);for(T v;sin>>v;res.pb(v));}//NOTES:stoa( 
template<class T> inline void checkmin(T &a,T &b){if(b<a) swap(a,b);}//NOTES:checkmin( 
template<class T> inline void checkmax(T &a,T &b){if(b>a) swap(a,b);}//NOTES:checkmax( 
template<class T> inline T gcd(T a,T b)//NOTES:gcd(  
	{if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);} 
template<class T> inline T euclide(T a,T b,T &x,T &y)//NOTES:euclide(
  {if(a<0){T d=euclide(-a,b,x,y);x=-x;return d;}  if(b<0){T d=euclide(a,-b,x,y);y=-y;return d;}  if(b==0){x=1;y=0;return a;}else{T d=euclide(b,a%b,x,y);T t=x;x=y;y=t-(a/b)*y;return d;}} 
  
const int dx[4] = {-1,0,0,1};
const int dy[4] = {0,-1,1,0};
const double pi=acos(-1.0);//NOTES:pi 

bool isok(int x,int y,int n,int m)
{
    return 0 <= x && x < n && 0 <= y && y < m;
}

/*I believe Spring Bro.*/

bool isp(int sc,int p){
    int mm = sc % 3;
    int ss = sc / 3;
    
    switch(mm){
        case 0: 
        case 1: return (ss+1 >= p && ss-1 >= 0);
        case 2: return ss+2 >= p;
    }
}
bool nop(int sc,int p){
    int mm = sc % 3;
    int ss = sc / 3;
    switch(mm){
        case 0: return ss >= p;
        case 1: 
        case 2: return ss+1 >= p;
    }
}

int main(){
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int T;
    cin >> T;
    int n,s,p;
    int sc;
    fo2(j,1,T+1){
        cout << "Case #" << j << ": ";
        cin >> n >> s >> p;
        int ans(0);
        fo(i,n){
            cin >> sc;
            if(sc / 3 >= p || nop(sc,p)) ans++;
            else
                if(s > 0 && isp(sc,p)){
                    --s;
                    ++ans;
                }
        }
        cout << ans;
        cout << endl;
    }
}
