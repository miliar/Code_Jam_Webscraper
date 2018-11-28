#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cassert>
#include<cstring>
#include<cmath>
#include<string>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<algorithm>
#define tr(container,it) for(typeof(container.begin()) it=container.begin();it!=container.end();it++)
#define F first
#define S second

using namespace std;
typedef pair<int, int> pii;

int X[1000];
vector<int> v;
map<int,int> mp;
int calc(int N){
    int sum=0,pos=0;
    while(N){
        if(N&1) sum+=X[pos];
        pos++;
        N>>=1;
    }
    return sum;
}
void print(int N){
    int pos=0;
    while(N){
        if(N&1) printf("%d ",X[pos]);
        pos++;
        N>>=1;
    }
    printf("\n");
}
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int T,N;
    scanf("%d",&T);
    for(int I=1;I<=T;I++){
        scanf("%d",&N);
        for(int i=0;i<N;i++)
            scanf("%d",&X[i]);
        mp.clear();
        bool solvable = false;
        int ans1,ans2,tot;
        for(int i=0;i<(1<<N);i++){
            tot=calc(i);
            if(mp.find(tot)!=mp.end()){
                ans1=mp[tot],ans2=i;
                solvable =true;
                break;
            }
            mp[tot]=i;
        }
            
        printf("Case #%d:\n",I);
        if(!solvable) printf("Impossible");
        else{
            print(ans1);
            print(ans2);
        }
    }
    
    return 0;
}
