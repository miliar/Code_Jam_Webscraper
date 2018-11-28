#include<fstream>
#include<iostream>
using namespace std;

int map[100][100];
bool vis[100][100];
char mp[100][100];
int W,H;


void readin() {
    cin>>H>>W;
    for(int i=0;i<H;i++) {
        for(int j=0;j<W;j++) {
            cin>>map[i][j];
        }
    }


}
char cur='a';

bool v(int r, int c, int v) {
if(r<0||c<0) return false;
if(r>=H||c>=W) return false;
//if(vis[r][c]) return false;
if(map[r][c]>=v) return false;

return true;
}

char dfs(int r, int c) {
 //   vis[r][c]=true;
    if(mp[r][c]>0) return mp[r][c];
    int n,e,w,s;
    n=10001;
    e=10001;
    w=10001;
    s=10001;
    if(v(r-1,c,map[r][c])) n=map[r-1][c];
    if(v(r+1,c,map[r][c])) s=map[r+1][c];
    if(v(r,c-1,map[r][c])) w=map[r][c-1];
    if(v(r,c+1,map[r][c])) e=map[r][c+1];
    if(n==10001&&w==10001&&s==10001&&e==10001) {
        mp[r][c]=cur;
        cur++;
        return mp[r][c];
    }



    if(n<=s&&n<=w&&n<=e&&n<=n) {
        mp[r][c]=dfs(r-1,c);

    } else if(w<=s&&w<=w&&w<=e&&w<=n) {
        mp[r][c]=dfs(r,c-1);

    } else if(e<=s&&e<=w&&e<=e&&e<=n) {
        mp[r][c]=dfs(r,c+1);

    } else if(s<=s&&s<=w&&s<=e&&s<=n) {
        mp[r][c]=dfs(r+1,c);

    }
    return mp[r][c];
}


void solve() {
    cur='a';
    for(int i=0;i<W;i++) for(int j=0;j<H;j++) mp[j][i]=0;
    for(int i=0;i<W;i++) for(int j=0;j<H;j++) vis[j][i]=false;;
    for(int i=0;i<H;i++) for(int j=0;j<W;j++) if(mp[i][j]==0) dfs(i,j);



}

void write() {
    for(int i=0;i<H;i++) {
        for(int j=0;j<W-1;j++) {
            cout<<mp[i][j]<<" ";

        }
        cout<<mp[i][W-1]<<endl;
    }


}


int N;
int main() {
    cin>>N;
    for(int i=0;i<N;i++) {
        readin();
        solve();
        cout<<"Case #"<<i+1<<":\n";
        write();

    }


}



