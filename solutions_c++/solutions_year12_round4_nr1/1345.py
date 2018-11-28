/*
 * Bidhan Roy
 * University of Dhaka
 */

using namespace std;

#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <ctime>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#define rep(i,n) for(__typeof(n) i=0; i<(n); i++)
#define foreach(i,n) for(__typeof((n).begin())i =(n).begin();i!=(n).end();i++)
#define inf (1<<30)
#define eps 1e-9
#define pb push_back
#define ins insert
#define mp make_pair
#define sz(x) ((int)x.size())
#define clr clear()
#define all(x) x.begin(),x.end()
#define xx first
#define yy second
#define sqr(x) ((x)*(x))
#define mem(x,val) memset((x),(val),sizeof(x));
#define read(x) freopen(x,"r",stdin);
#define rite(x) freopen(x,"w",stdout);
#define chk(a,k) ((bool)(a&(1<<(k))))
#define off(a,k) (a&(~(1<<(k))))
#define on(a,k) (a|(1<<(k)))

typedef long long i64;
typedef unsigned long long ui64;
typedef string st;
typedef vector<int> vi;
typedef vector<st> vs;
typedef map<int,int> mii;
typedef map<st,int> msi;
typedef map<int,st> mis;
typedef set<int> si;
typedef set<st> ss;
typedef pair<i64,i64> pii;
typedef vector<pii> vpii;

#define mx 15000
pii a[mx];
i64 D;
int n;
map<i64,bool> dp[mx];
bool call(int pos,i64 h){
    //cout<<pos<<" "<<h<<endl;
    if(a[pos].xx+h>=D) { return true; }
    if(dp[pos].find(h)!=dp[pos].end()) return dp[pos][h];
    for(int i=pos+1; i<n; i++){
        if(a[i].xx-a[pos].xx<=h){
            if(call(i,min(a[i].xx-a[pos].xx,a[i].yy))) return dp[pos][h]=true;
        }
        else break;
    }
    //cout<<pos<<" "<<h<<" No"<<endl;
    return dp[pos][h]=false;
}
int main(){
    double cl = clock();
    cl = clock() - cl;
    read("ain.txt");
    rite("aout.txt");
	ios_base::sync_with_stdio(0);
	int test,kas=0;
	cin>>test;

	while(test--){
	    cin>>n;
	    rep(i,n) { cin>>a[i].xx>>a[i].yy; dp[i].clr; }
	    dp[n].clr;
	    cin>>D;
	    int f=0;
	    rep(i,1)if(a[i].xx<=a[i].yy){
	        if(call(i,a[i].xx)) { f=1; break; }
	    }
	    else break;
	    cout<<"Case #"<<++kas<<":";
	    cout<<(f?" YES":" NO")<<endl;
	}
    fprintf(stderr, "Total Execution Time = %lf seconds", cl / CLOCKS_PER_SEC);
    return 0;
}
