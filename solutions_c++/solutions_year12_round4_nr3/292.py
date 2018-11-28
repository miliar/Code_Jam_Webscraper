//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

#define For(i, n) for(int i = 0; i<(n); ++i)
#define ForEach(it, i) for(typeof i.begin() it = i.begin(); it!=i.end(); ++it)
#define eps 1e-9

typedef long long ll;
typedef pair<int, int> pii;

int N;
int vys[2047];
int h[2047];

int extra(){
    vector<int> vidiama[2047];
    scanf("%d",&N);
    For(i,N-1) {
        scanf("%d",vys+i);
        vys[i]--;
        vidiama[vys[i]].push_back(i);
    }
    vys[N-1] = N;
    h[N] = 1000000000;
    h[N-1] = 1000000000;
    for(int i = N-1; i>0; i--){
        //printf("!%d, %d\n", h[i], vidiama[i].size());
        if (vidiama[i].size()==0) continue;
        int d = (i-vidiama[i][0]);
        int H = (ll(h[vys[i]] - h[i])*ll(d))/(vys[i]-i)+1;
        //printf("?%d\n",H);
        for(int k = 0; k < vidiama[i].size(); k++) h[vidiama[i][k]] = h[i]-H;
    }
    int zle = 0;
    For(i,N) {
        if (zle) break;
        if (h[i]<0 || h[i]>1000000000) {
            zle = 1; break;
        }
        for(int j = i+1; j<vys[i]; ++j){
            if ( ll(h[j]-h[i])*ll(vys[i]-i) >= ll(h[vys[i]]-h[i])*ll(j-i)) {
                zle = 1;
                break;
            }
        }
        for(int j = vys[i]+1; j<N; ++j){
            if ( ll(h[j]-h[i])*ll(vys[i]-i) > ll(h[vys[i]]-h[i])*ll(j-i)) {
                zle = 1;
                break;
            }
        }
    }
    if (zle) {
        printf(" Impossible\n");
    }else{
        For(i,N) printf(" %d",h[i]);
        printf("\n");
    }
}

int main(){
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d:",i+1);
        extra();
    }
}
