#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <string>
#include <cmath>
#include <list>
#include <cstdlib>
#include <map>
#include <cstring>
#include <set>
#include <stack>
#include <sstream>
#include <queue>
#include <ctime>

using namespace std;

#define debug(x) cout<<#x<<" = "<<x<<"\n"
#define FOR(t,a,n) for(int t=(a);(t)<(n);(t)++)
#define REP(I,N) FOR(I,0,N)
#define PB(X) push_back(X)
#define MP(X,Y) make_pair(X,Y)
#define SZ(X) (int)X.size()
#define ALL(x) (x).begin(), (x).end()
#define SET(A,v) memset(A,v,sizeof A)
#define INF (int)1e9

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef list<int> LI;
typedef vector<string> VS;
typedef pair<int,int> PII;

int O[500];
int B[500];

int main()
{
    #ifdef VIN
        freopen("1_in.txt","r",stdin);
        freopen("2_out.txt","w",stdout);
    #else
        freopen("A-large.in","r",stdin);
        freopen("A-large.txt","w",stdout);
    #endif
        
    int T,nu=0;
    scanf("%d",&T);
    getchar();
    while(T--){
        int n,szo=0,szb=0;
        char c;
        string s,str;
        getline(cin,s);
        istringstream ss(s);
        ss>>n;
        REP(i,n){
            ss>>c;
            str+=c;
            if(c=='O')ss>>O[szo++];
            else ss>>B[szb++];
        }
        int posO=1,posB=1,time=0,i=0,j=0,step;
        REP(k,str.length()){
            if(str[k]=='O'){
                if(O[i]>posO)step=O[i]-posO;else step=posO-O[i];
                posO=O[i];
                step++;i++;
                if(B[j]>posB)if(B[j]-posB>step)posB+=step;else posB=B[j];
                else if(B[j]<posB)if(posB-B[j]>step)posB-=step;else posB=B[j];
                time+=step; 
            }
            else { 
                if(B[j]>posB)step=B[j]-posB;else step=posB-B[j];
                posB=B[j]; 
                step++;j++;
                if(O[i]>posO)if(O[i]-posO>step)posO+=step;else posO=O[i];
                else if(O[i]<posO)if(posO-O[i]>step)posO-=step;else posO=O[i];
                time+=step;
            }
        }
        printf("Case #%d: %d\n",++nu,time);
    }
    return 0;
}
    
