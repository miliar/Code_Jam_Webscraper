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
#define ALL(x) (x).begin(), (x).end()
#define SET(A,v) memset(A,v,sizeof A)
#define INF (int)1e9

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef list<int> LI;
typedef vector<string> VS;
typedef pair<int,int> PII;
#define FORE(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

map<string,char> paired;
map<char,char> oppose;

char s_in[5];

int main()
{
    #ifdef VIN
        freopen("1_in.txt","r",stdin);
        freopen("2_out.txt","w",stdout);
    #else
        freopen("B-small.in","r",stdin);
        freopen("B-small.txt","w",stdout);
    #endif
        
    int T,C,D,N,nu=0;
    scanf("%d",&T);
    while(T--){
        vector<char> v; string str;
        scanf("%d",&C);
        REP(i,C){
            scanf("%s",s_in);
            string s;
            s+=s_in[0]; s+=s_in[1];
            paired[s]=s_in[2];
            swap(s[0],s[1]);
            paired[s]=s_in[2];
        }
        scanf("%d",&D);
        REP(i,D){
            scanf("%s",s_in);
            oppose[s_in[0]]=s_in[1];
            oppose[s_in[1]]=s_in[0];
        }
        scanf("%d",&N);
        cin>>str; 
        v.PB(str[0]);
        FOR(i,1,N){
            if(!v.empty()){
                string s;
                int sz=v.size();
                s+=v[sz-1]; s+=str[i];
                if(paired.find(s)!=paired.end()){
                    char ch=paired[s];
                    v[sz-1]=ch;
                    continue;
                }
                if(oppose.find(str[i])!=oppose.end()){
                    if(find(ALL(v),oppose[str[i]])!=v.end()){v.clear();continue;}
                }
                v.PB(str[i]);
            }
            else v.PB(str[i]);
        }
        printf("Case #%d: [",++nu);
        if(!v.empty()){
            printf("%c",v[0]); 
            REP(i,v.size())if(i)printf(", %c",v[i]);
            
        }
        printf("]\n");
        oppose.clear();
        paired.clear();
    }
    return 0;
}
                
            
