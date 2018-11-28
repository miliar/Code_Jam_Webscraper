#include<iostream>
#include<vector>
#include<fstream>
#include<string>
#include<sstream>
#include<map>
#include<set>
#include<algorithm>
#include<cmath>
#include<cstring>
using namespace std;

#define FOR(i,a,b) for(int _b=(b),i=(a);i!=_b;++i)
#define REP(i,n) FOR(i,0,n)
#define SZ(v) (int)(v).size()
#define PB push_back
#define MP make_pair
#define CL(v,a) memset((v),(a),sizeof(v))
#define UN(v) sort((v).begin(),(v).end()),(v).erase(unique((v).begin(),(v).end()),(v).end())

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

int main() {
    FILE*fin=freopen("input.in","r",stdin);
    int T;
    scanf("%d",&T);
    for (int t=0;t<T;++t){
        int n, k;
        scanf("%d%d",&n,&k);
        k%=(1<<n);
        printf("Case #%d: %s\n", t+1, (k+1==(1<<n))?"ON":"OFF");
    }
    return 0;
}
