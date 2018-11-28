#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<string>
#include<string.h>
#include<math.h>
#include<iostream>
#include<sstream>
using namespace std;
#define ll long long
#define pii pair<int,int>
#define pll pair<long long,long long>
#define x first
#define y second
int dist[101000];
int mn[101000];
int mx[101000];
void solve(){
    int n;
    cin >>n;
    vector<int > d,l;
    for(int i=0;i<n;i++){
        pii p;
        cin >> p.x >> p.y;
        d.push_back(p.x);
        l.push_back(p.y);
    }
    int D;
    cin >> D;
    for(int i=0;i<n;i++){
        dist[i]=0;
        mn[i]=n+1;
        mx[i]=0;
    }
    dist[0]=d[0];
    bool up=1;
    int turn=0;
    while(up){
        up=0;
        for(int j=0;j<n;j++){
            if(dist[j]+d[j]>=D){
                cout <<"YES"<<endl;
                return;
            }
            if(dist[j]==0)continue;
            for(int k=turn?mn[j]:0;k<n;k++){
                if(j==k)continue;
                if(d[k]-d[j]>dist[j])break;
                if(k<mn[j])mn[j]=k;
                if(k>mx[j])mx[j]=k;
                if(dist[j]>=abs(d[j]-d[k])&&min(l[k],abs(d[j]-d[k]))>dist[k]){
                    up=1;
                    dist[k]=max(dist[k],min(l[k],abs(d[j]-d[k])));
                }
            }
        }
        turn++;
    }
    cout << "NO"<<endl;
    return ;
}
int main(){
    int n;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        printf("Case #%d: ",i);
        solve();
    }
}
