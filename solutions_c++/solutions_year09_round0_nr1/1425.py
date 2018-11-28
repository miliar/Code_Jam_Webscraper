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

int d,n,l;
int words[5050][20];
int pattern[20];
void readwords(void){
    char c;
    REP(i,d){
        REP(j,l){
            scanf("%c",&c);
            words[i][j]=1<<(c-'a');
        }
        scanf("%c",&c);
    }
}
void readpattern(void){
    memset(pattern,0,sizeof(pattern));
    char c;
    REP(i,l){
        scanf("%c",&c);
        if(c=='('){
            do{
                scanf("%c",&c);
                if(c==')')
                    break;
                pattern[i]+=1<<(c-'a');
            }while(c!=')');
        }
        else
            pattern[i]+=1<<(c-'a');
    }
    scanf("%c",&c);
}
int solve(void){
    int cnt=0;
    REP(i,d){
        cnt++;
        REP(j,l)
            if(!(words[i][j]&pattern[j])){
                cnt--;
                break;
            }
    }
    return cnt;
}
int main(){
    scanf("%d %d %d ",&l,&d,&n);
    readwords();
    REP(i,n){
        readpattern();
        printf("Case #%d: %d\n",i+1,solve());
    }
    return 0;
}
