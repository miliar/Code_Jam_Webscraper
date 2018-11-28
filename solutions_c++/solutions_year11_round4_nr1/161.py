#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>

using namespace std;

vector<pair<int,int> > w;
int X,S,R,t,N;

void solve(int cas){
    int i,j,k;
    int b,e,v;
    scanf("%d%d%d%d%d",&X,&S,&R,&t,&N);
    w.clear();
    for (i=0;i<N;i++){
        scanf("%d%d%d",&b,&e,&v);
        w.push_back(make_pair(v,e-b));
        X-=e-b;
    }
    w.push_back(make_pair(0,X));
    sort(w.begin(),w.end());
    double r = 0;
    double tt;
    for (i=0;i<w.size();i++){
        
        if (r>=t){
            // walk
            r+=w[i].second*1.0/(w[i].first+S);
        }else{
            tt = 1.0*w[i].second/(w[i].first+R);
            if (tt+r<=t){
                r+=tt;
            }else{
                r=t+1.0*(w[i].second-(t-r)*(w[i].first+R))/(w[i].first+S);
            }
        }
    }
    printf("Case #%d: %.10lf\n",cas,r);
}

int main(){
    int T,cas;
    scanf("%d",&T);
    for (cas=1;cas<=T;cas++) solve(cas);
    return 0;
}

