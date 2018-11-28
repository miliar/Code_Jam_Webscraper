#include<iostream>
#include<cmath>
#include<string>
#include<sstream>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<numeric>

using namespace std;

#define MAX INT_MAX
#define EPS (1e-10)

#define pb(a) push_back(a)
#define mp(a,b) make_pair(a,b)
#define K(a) ((a)*(a))

#define REP(i,v) for(typeof((v).begin()) i = (v).begin(); i!= (v).end(); ++i )
#define FOR(i,v) for(int i=0; i<v.size(); ++i)

typedef pair<int,int> pii;



int main(){        
    freopen ("a.out","w",stdout);
    freopen ("a.in","r",stdin);
    
    int n;
    scanf("%d",&n);
    for(int i=0; i<n; i++){
            int m;
            vector<int> v1,v2;
            v1.clear();v2.clear();
            
            scanf("%d",&m);
            
            for(int j=0; j<m; j++){
                    int k; scanf("%d",&k); v1.pb(k);
                    }
            for(int j=0; j<m; j++){
                    int k; scanf("%d",&k); v2.pb(k);
                    }
            sort(v1.begin(),v1.end());
            sort(v2.begin(),v2.end());
                    
            int ret=0;
            for(int j=0; j<m; j++)
                    ret+=v1[j]*v2[m-1-j];
            
            printf("Case #%d: %d\n",i+1,ret);
            }

    
    return 0;
}
