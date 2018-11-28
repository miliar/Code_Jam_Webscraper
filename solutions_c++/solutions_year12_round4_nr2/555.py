#include <cstdio>
#include <vector>
#include <string>
#include <numeric>
#include <cstring>
#include <cassert>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <algorithm>
using namespace std;

typedef pair<int,int> PII;
typedef long long LL;
const int INF = 1000000007;

const double eps = 1e-7;

double random(){
    return rand()*1.0/(RAND_MAX+1)+rand()*1.0/RAND_MAX/RAND_MAX;
}

int random(int n){
    return ((rand()<<15)^rand())%n;
}

double dist(double x, double y, double cx, double cy){
    return sqrt((cx-x)*(cx-x)+(cy-y)*(cy-y));
}

int main(){
    int cs,no=0;
    scanf("%d",&cs);
    while(cs--){
        int n,w,l,r[1000];
        scanf("%d%d%d",&n,&w,&l);
        vector<int> u;
        for(int i=0;i<n;i++){
            scanf("%d",r+i);
            u.push_back(i);
        }
        vector<tuple<double,double,int,int>> has;
        while(u.size()){
            swap(u[random(u.size())],u.back());
            double x=random()*w;
            double y=random()*l;
            int t=u.back(),tr=r[t],sum=0;
            vector<int> v;
            u.pop_back();
            for(size_t i=0;i<has.size();i++){
                double cx,cy;
                int c,cr;
                tie(cx,cy,c,cr)=has[i];
                if(dist(x,y,cx,cy)>tr+cr+eps) continue;
                sum+=cr;
                v.push_back(i);
            }
            if(tr<=sum){
                u.push_back(t);
            }else{
                for(size_t i=v.size()-1;~i;i--){
                    u.push_back(get<2>(has[v[i]]));
                    swap(has[v[i]],has.back());
                    has.pop_back();
                }
                has.push_back(make_tuple(x,y,t,tr));
            }
        }
        printf("Case #%d:",++no);
        pair<double,double> ans[1000];
        for(size_t i=0;i<has.size();i++){
            double cx,cy;
            int c,cr;
            tie(cx,cy,c,cr)=has[i];
            ans[c]={cx,cy};
        }
        for(int i=0;i<n;i++) printf(" %.9f %.9f",ans[i].first,ans[i].second);
        puts("");
    }
}
