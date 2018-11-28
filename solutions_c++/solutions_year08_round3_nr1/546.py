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

int tab[1111];


int main(){        
    freopen ("a.out","w",stdout);
    freopen ("a.in","r",stdin);
    
    int n;
    scanf("%d",&n);
    for(int i=0; i<n; i++){
            int maxOnKey, howMuchKeys, howMuchLetters;
            scanf("%d%d%d",&howMuchKeys,&maxOnKey,&howMuchLetters);
            
            for(int j=0; j<howMuchLetters; j++)
                    scanf("%d",&tab[j]);
                    
            sort(tab,tab+howMuchLetters);
            reverse(tab,tab+howMuchLetters);
            
            
            int ret=0;
            for(int j=0; j<howMuchLetters; j++){
                    ret+=tab[j]*(j/maxOnKey+1);
           //         cout<<tab[j]<<' '<<j/maxOnKey+1<<endl;
                    }



            cout<<"Case #"<<i+1<<": "<<ret<<endl;
            }

    
    return 0;
}
