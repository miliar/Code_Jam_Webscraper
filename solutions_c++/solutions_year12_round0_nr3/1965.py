#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define pb push_back
#define mp make_pair

vector<pair<int,int> > memo;
int proc(int a,int b){
    memo.clear();
    int x,y;
    for (int i=a;i<=b;++i){
        for (int t=10;;){
            if (t>i) break;
            x=i/t;
            y=i%t;
            for (int u=1;;){
                if (u<=x && x<u*10){
                   u*=10;
                   y*=u;
                   y+=x;
                   break;
                }
                else u*=10;
            }
            memo.pb(mp(min(i,y),max(i,y)));
            t*=10;
        }
    }
    sort(memo.begin(),memo.end());
    memo.resize(unique(memo.begin(),memo.end())-memo.begin());
    int cnt=0;
    for (int i=0;i<memo.size();++i){
        if (a<=memo[i].first && memo[i].second<=b && memo[i].first!=memo[i].second){
           cnt++;
        }
    }
    return cnt;
}

int main(){
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int ntest,A,B,digit,temp;
    scanf("%d",&ntest);
    for (int test=1;test<=ntest;++test){
        scanf("%d %d",&A,&B);
        printf("Case #%d: %d\n",test,proc(A,B));
    }
    return 0;
}
