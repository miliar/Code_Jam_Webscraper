#include <cstdio>
#include <algorithm>

using namespace std;

pair<int, int> duzine[2000];

bool sijeku(int i, int j){
    if( duzine[j].first < duzine[i].first && duzine[j].second > duzine[i].second ) return true;
    if( duzine[j].first > duzine[i].first && duzine[j].first < duzine[i].second && duzine[j].second < duzine[i].second ) return true;
    return false;
}

int main(){
    int t;
    scanf("%d",&t);
    for(int test = 0;test<t;++test){
        int n;
        scanf("%d",&n);
        for(int x = 0;x<n;++x){
            scanf("%d %d",&duzine[x].first, &duzine[x].second);
        }
        int sol = 0;
        for(int x = 0;x<n-1;++x){
            for(int y = x+1;y<n;++y){
                if( sijeku( x, y ) ) ++sol;
            }
        }
        printf("Case #%d: %d\n",test+1,sol);
    }
}
