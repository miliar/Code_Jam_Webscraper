#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string.h>
#include <cassert>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define fr(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define INF (int)1e9

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef pair<int,int> PII;
int main(){
	
	freopen("iinn.txt","r",stdin);
	freopen("oonn.txt","w",stdout);
	int tt,c,n,s,p,t[101],cnt,x,t2;
    cin>>tt;c=1;
    while(tt--){ cin>>n>>s>>p;cout<<"Case #"<<c<<": ";c++;
    fr(i,0,n)cin>>t[i];if(p==0)cout<<n;else if(p==1){cnt=0;fr(i,0,n)if(t[i]>0)cnt++;cout<<cnt;}
    else { x=3*p-4;cnt=0;t2=0;fr(i,0,n)if(t[i]==x || t[i]==x+1)cnt++;else if(t[i]>x+1)t2++;cout<<(t2+min(s,cnt));}
    cout<<endl;
    }
    return 0;
}
