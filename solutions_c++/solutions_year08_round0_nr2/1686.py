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

int add,n,na,nb,n2460=24*60;


int main(){        
    freopen ("b.out","w",stdout);
    freopen ("b.in","r",stdin);

    scanf("%d",&n);
    for(int i=1; i<=n; i++){
            int ile[2]={0,0};
            int z[2][30*60]={0};
            char ss[100];
            int h,m;
            
            scanf("%d%d%d\n",&add,&na,&nb);

                 for(int i=0; i<na; i++){ 
                         scanf("%s",ss);
                         h=(10*(ss[0]-'0')+(ss[1]-'0'));
                         m=(10*(ss[3]-'0')+(ss[4]-'0'));
                         z[0][h*60+m]--;
//                 cout<<h<<' '<<m<<endl;
                         
                         scanf("%s",ss);
                         h=(10*(ss[0]-'0')+(ss[1]-'0'));
                         m=(10*(ss[3]-'0')+(ss[4]-'0'));
                         z[1][h*60+m+add]++;
 //                cout<<h<<' '<<m<<endl;
                         }
                 for(int i=0; i<nb; i++){ 
                         scanf("%s",ss);
                         h=(10*(ss[0]-'0')+(ss[1]-'0'));
                         m=(10*(ss[3]-'0')+(ss[4]-'0'));
                         z[1][h*60+m]--;
   //              cout<<h<<' '<<m<<endl;
                         
                         scanf("%s",ss);
                         h=(10*(ss[0]-'0')+(ss[1]-'0'));
                         m=(10*(ss[3]-'0')+(ss[4]-'0'));
                         z[0][h*60+m+add]++;
    //             cout<<h<<' '<<m<<endl;
                         }
                 

                    
            for(int j=0; j<n2460; j++){
                    if(  z[0][j] < 0 ) ile[0] -= z[0][j];
                    else z[0][j+1]+=z[0][j];
                    
                    if(  z[1][j] < 0 ) ile[1] -= z[1][j];
                    else z[1][j+1]+=z[1][j];
                    }                    
            
            printf("Case #%d: %d %d\n",i,ile[0],ile[1]);
            }
    
    
    return 0;
}
