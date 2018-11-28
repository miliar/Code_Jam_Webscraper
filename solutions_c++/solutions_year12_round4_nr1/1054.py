#include <iostream> 
#include <fstream> 
#include <cmath>
#include <stdlib.h> 
#include <stdio.h> 
#include <vector> 
#include <string> 
#include <iterator> 
#include <algorithm> 
#include <numeric> 
#include <utility> 
#include <map> 
#include <queue> 
#include <set> 
#include <stack> 
#include <sstream> 
#include <cctype> 
#include <assert.h> 
#include <list> 
#include <cstring>

using namespace std; 

#define MP(a,b) make_pair(a,b) 
#define ll long long 
#define pb push_back 
#define For(i,a,b) for(typeof(a) i=(a);i<(b);i++) 
#define FOREACH(V,it) for(typeof(V.begin()) it=V.begin();it!=V.end();it++) 
#define CLR(a,x) memset(a,x,sizeof(a)) 
#define ALL(x) x.begin(),x.end() 
#define DBG(a) cerr << #a << ' ' << a << endl;

/**********************************************************************************/ 
const int maxn=10010;
ll n,D,len[maxn];
pair<ll,ll> a[maxn];

void p1(FILE *f, int cas){
    scanf("%lld",&n);
    For(i,0,n){
        scanf("%lld%lld",&a[i].first, &a[i].second);
    }
    scanf("%lld",&D);
    CLR(len,-1);
    ll inf = a[n-1].first+a[n-1].second;
    a[n]=MP(inf,0);
    len[0]=min(a[0].first,a[0].second);
    ll maxreach=0;

    for(int cur=0;cur<n;cur++){
        if (len[cur]==-1) break;
        maxreach = max(maxreach,a[cur].first+len[cur]);
        pair<ll,ll> k = MP(a[cur].first+len[cur],inf);
        int v = upper_bound(a,a+n,k)-a;
        //cout << v << ' ' << a[v].first << endl;
        v--;
        //printf("%d can reach %d \n",cur,v);
        while (v>cur){
            int val = min(a[v].first-a[cur].first,a[v].second);
            if (len[v]==-1 || len[v]< val){
                len[v]=val;
            } else {
               break;
            }
            v--;
            //printf("%d %d\n",v,cur);
        }
        
    }
    if (maxreach>=D){
        fprintf(f,"Case #%d: %s\n",cas,"YES");
    } else {
        fprintf(f,"Case #%d: %s\n",cas,"NO");
    }

}

int main(){
    int c;
    scanf("%d",&c);
    FILE *f = fopen("output3.txt","w");
    for(int cas=1;cas<=c;cas++){
        DBG(cas);
        p1(f,cas);
    }
    fclose(f);
    return 0;
}
