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
    int N,L,H,i;
    cin >> N >> L >> H;
    int ar[N];
    REP(i,N) cin >> ar[i];
    for(i=L; i<=H; i++){
        int j;
        for(j=0;j<N;j++){
            if( i%ar[j] ==0 || ar[j]%i ==0) continue;
            else break;
        }
        if(j==N) { printf("%d\n",i); break; }
    }
    if(i>H)  printf("NO\n");
        
}

int main(void)
{
    
    #ifdef ONLINE_JUDGE
        freopen("C-small-attempt0.in","r",stdin);
        freopen("C-small-attempt0.txt","w",stdout);

    // 	  freopen("C-small-attempt0.in","r",stdin);
    //    freopen("C-small-attempt0.txt","w",stdout);
	
    //    freopen("C-large.in","r",stdin);
    //    freopen("C-large.txt","w",stdout);

    #else
        freopen("1_in.txt","r",stdin);
        freopen("2_out.txt","w",stdout);
    #endif
    
    int num_of_test_cases;
    scanf("%d",&num_of_test_cases);
    REP(i,num_of_test_cases){
	printf("Case #%d: ",++case_number);
	main2();
    }
    return 0;
}
