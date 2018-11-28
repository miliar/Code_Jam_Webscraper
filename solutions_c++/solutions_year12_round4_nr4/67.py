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

int r,c;
string mp[11];
vector<pii> ans;
bool mark[21][21];
struct node{
    bool map[11][11];
    node(){
        for(int i=0;i<r;i++)for(int j=0;j<c;j++)map[i][j]=mark[i][j];
    }
    bool bad(){
        for(int i=0;i<r;i++)for(int j=0;j<c;j++){
            if(map[i][j]&&!mark[i][j])return 1;
        }
        return 0;
    }
    bool goodEnd(int x,int y){
        if(map[x][y]==0)return 0;
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++)if(map[i][j]&&(i!=x||j!=y))return 0;
        }
        return 1;
    }
    void move(int dx,int dy){
        bool nxt[11][11];
        for(int i=0;i<r;i++)for(int j=0;j<c;j++){
            nxt[i][j]=0;


        }
        for(int i=1;i<r-1;i++)for(int j=1;j<c-1;j++){
            if(map[i][j]){
                if(mp[i+dx][j+dy]!='#')nxt[i+dx][j+dy]=1;
                else nxt[i][j]=1;
            }
        }
        for(int i=0;i<r;i++)for(int j=0;j<c;j++)map[i][j]=nxt[i][j];
    }
    bool operator < (const node &o ) const{
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++)if(map[i][j]!=o.map[i][j])return map[i][j]<o.map[i][j];
        }
        return 0;
    }
    void print(){
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++)cout << map[i][j];
            cout << endl;
        }
    }
};
int dx[3]={1,0,0};
int dy[3]={0,-1,1};
int bfs(int x,int y){
    queue<node> q;
    set<node> s;
    q.push(node());
    s.insert(node());
    while(!q.empty()){
        node k=q.front();
        q.pop();
        //k.print();
        //cout <<"_________________________"<<endl;
        if(k.bad())continue;
        if(k.goodEnd(x,y)){
            //k.print();
            return 1;
        }
        for(int j=0;j<3;j++){
            node nxt=k;
            nxt.move(dx[j],dy[j]);
            if(nxt.bad())continue;
            if(s.find(nxt)==s.end()){
                //printf("FROM %d %d\n",dx[j],dy[j]);
                //k.print();
                //printf("TO\n");
                //nxt.print();
                s.insert(nxt);
                q.push(nxt);
            }
        }
    }
    return 0;
}
void _find(int x,int y,int id){
    for(int i=0;i<r;i++)for(int j=0;j<c;j++)mark[i][j]=0;
    mark[x][y]=1;
    int cnt=1;
    for(int i=r-1;i>=0;i--){
        for(int j=0;j<c;j++){
            if(mark[i][j]){
                if(i&&mp[i-1][j]!='#'&&mark[i-1][j]==0){
                    mark[i-1][j]=1;
                    cnt++;
                }
                if(j&&mp[i][j-1]!='#'&&mark[i][j-1]==0){
                    mark[i][j-1]=1;
                    cnt++;
                }
                if(j+1<c&&mp[i][j+1]!='#'&&mark[i][j+1]==0){
                    mark[i][j+1]=1;
                    cnt++;
                }
            }
        }
        for(int j=c-1;j>=0;j--){
            if(mark[i][j]){
                if(i&&mp[i-1][j]!='#'&&mark[i-1][j]==0){
                    mark[i-1][j]=1;
                    cnt++;
                }
                if(j&&mp[i][j-1]!='#'&&mark[i][j-1]==0){
                    mark[i][j-1]=1;
                    cnt++;
                }
                if(j+1<c&&mp[i][j+1]!='#'&&mark[i][j+1]==0){
                    mark[i][j+1]=1;
                    cnt++;
                }
            }
        }
    }
    int ok = bfs(x,y);
    //printf("ok=%d\n",ok);
    ans.push_back(make_pair(cnt,ok));
    //system("pause");
    // counting

}
void solve(){
    cin >>r >> c;
    for(int i=0;i<r;i++){
        cin >> mp[i];
    }
    ans.clear();
    bool found=0;
    int cave=0;
    while(1){
        found=0;
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                if(mp[i][j]-'0'==cave){
                    found=1;
                    _find(i,j,cave);
                    cave++;
                }
            }
        }
        if(found==0)break;
    }
    for(int i=0;i<cave;i++){
        cout << i<<": "<<ans[i].first <<" ";
        if(ans[i].second)cout <<"Lucky"<<endl;
        else cout <<"Unlucky"<<endl;
    }
}
int main(){
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        printf("Case #%d:\n",i);
        solve();
    }
}
