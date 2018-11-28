#include <cstdio>
#include <map>
#include <set>
#include <vector>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <fstream>
#include <queue>
#include <list>
#include <cstring>
#define FOR(i,a,n) for(int i=a;i<=n;i++)
#define REP(i,n) for (int i=0;i<n;i++)
#define FORD(i,n,a) for(int i=n;i>=a;i--)
#define PB push_back
#define MP make_pair
#define xx first
#define yy second
#define Min(a,b) a<b ? a:b
#define Max(a,b) a>b ? a:b
#define p2(a) ((a)*(a))
#define ALL(v) v.begin(),v.end()
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef double dd;
typedef long long ll;
    
map<char,int> M;

ll solve(void){
    M.clear();
    char c=' ';
    int cnt=0;
    string s="";
    while(c!='\n'){
        scanf("%c",&c);
        if(c=='\n')
            break;
        if(M.count(c)==0){
            cnt++;
            if(cnt==1)
                M[c]=1;
            else if(cnt==2)
                M[c]=0;
            else 
                M[c]=cnt-1;
        }
        s+=c;
    }
    int base=max(2,cnt);
    ll pot =1ll;
    ll result = 0;
    FORD(i,s.size()-1,0){
        result += pot*(ll)M[s[i]];
        pot*=(ll)base;
    }
    return result;
}
            
    
int main(){
    int n;
    scanf("%d ",&n);
    REP(i,n)
        printf("Case #%d: %lld\n",i+1,solve());
    return 0;
}
