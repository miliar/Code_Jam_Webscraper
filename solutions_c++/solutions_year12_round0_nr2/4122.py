//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

#define For(i, n) for(int i = 0; i<(n); ++i)
#define ForEach(it, i) for(typeof i.begin() it = i.begin(); it!=i.end(); ++it)

typedef long long ll;
typedef pair<int, int> pii;

int N,S,P,a,T;
int main(){
    scanf("%d",&T);
    For(t,T){
        scanf("%d %d %d",&N,&S,&P);
        int Smin = P+max(0,P-2)*2;
        int Xmin = P+max(0,P-1)*2;
        int M = 0;
        For(i,N) {
            scanf("%d",&a);
            if (a>=Xmin) {
                M++;
                continue;
            }
            if (S>0 && a>=Smin) {
                M++;
                S--;
                continue;
            }
        }
        printf("Case #%d: %d\n",t+1,M);
    }
}
