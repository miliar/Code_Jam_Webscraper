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
struct node {int g,next,spend;};
node G[1100];

int main() {
    FILE*fin=freopen("input.in","r",stdin);
    int T;
    scanf("%d",&T);
    for (int t=0;t<T;++t){
        int R,k,N;
        scanf("%d%d%d",&R,&k,&N);
        for (int i=0;i<N;++i) scanf("%d", &G[i].g);
        for (int i=0;i<N;++i) {
            int rm=k;
            int j=i;
            for (;;){
                if (rm<G[j].g)break;
                rm-=G[j].g;
                j++;
                if (j==N)j=0;
                if (j==i)break;
            }
            G[i].next=j;
            G[i].spend=k-rm;
        }

        ll ret=0;
        int i=0;
        while (R--){
            ret+=G[i].spend;
            i=G[i].next;
        }
        printf("Case #%d: %I64d\n", t+1, ret);
    }

    return 0;
}
