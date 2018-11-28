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
#include <numeric>
#include <stack>
#include <sstream>
#include <queue>
#include <ctime>

using namespace std;

#define debug(x) cout<<#x<<" = "<<x<<"\n"
#define REP(i,n) for(int (i)=0;(i)<(n);(i)++)
#define PI 3.1415926535897932385
#define EPS (1e-9)
#define INF (1<<29)
#define bit(n) (1<<(n))
#define pb push_back
#define sz size()
#define mp make_pair
#define all(a) a.begin(),a.end()
#define fill(ar,val) memset(ar,val,sizeof ar)
#define sqr(x) ((x)*(x))
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define ONLINE_JUDGE 

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> PII;

int case_number;
#define FORE(itr,c) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

void main2()
{
    int r,c;
    cin >> r >> c;
    char ans[r][c];
    REP(i,r) REP(j,c) cin >> ans[i][j];
    
    REP(i,r) REP(j,c){
        if(i+2 > r || j+2 > c || ans[i][j] =='/' || ans[i][j]=='\\' ) continue;
        bool flag =true;
        for(int k=i; k<i+2; k++) for(int l=j; l<j+2; l++){
            if(ans[k][l]!='#')flag=false;
        }
        if(flag){
            ans[i][j]='/';
            ans[i][j+1]  = '\\';
            ans[i+1][j] = '\\';
            ans[i+1][j+1]= '/';
        }
    }
    int match = 1;
    REP(i,r)REP(j,c){
        if(ans[i][j] == '#') match = 0;
    }
    if(match) REP(i,r){
        REP(j,c) cout << ans[i][j];
        cout << endl;
    }
    else printf("Impossible\n");
    
}

int main(void)
{
    
    #ifdef ONLINE_JUDGE
     //   freopen("A-small-attempt0.in","r",stdin);
     //   freopen("A-small-attempt0.txt","w",stdout);
    // 	  freopen("A-small-attempt0.in","r",stdin);
    //    freopen("A-small-attempt0.txt","w",stdout);
	
        freopen("A-large.in","r",stdin);
        freopen("A-large.txt","w",stdout);

    #else
        freopen("1_in.txt","r",stdin);
        freopen("2_out.txt","w",stdout);
    #endif
    
    int num_of_test_cases;
    scanf("%d",&num_of_test_cases);
    REP(i,num_of_test_cases){
	printf("Case #%d:\n",++case_number);
	main2();
    }
    return 0;
}
