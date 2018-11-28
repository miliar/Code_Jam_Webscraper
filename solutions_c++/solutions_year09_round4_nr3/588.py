#include<iostream>
#include<vector>
using namespace std;
int e,k;
struct gr {
    int k[25];
};
gr s[100];
void read() {
    cin>>e>>k;

    for(int i=0;i<e;i++) {
        for(int j=0;j<k;j++) {
            cin>>s[i].k[j];
        }
    }
}
vector<vector<gr> > chs;
int ans=-1;
bool cross(int i, gr g) {
    if(i>=chs.size()) return false;
    for(int a=0;a<chs[i].size();a++) {
        for(int b=0;b<k-1;b++) {
            if(chs[i][a].k[b+1]>=g.k[b+1]&&chs[i][a].k[b]<=g.k[b]) return true;
            if(chs[i][a].k[b+1]<=g.k[b+1]&&chs[i][a].k[b]>=g.k[b]) return true;
            
        }
        
    }
 //   cout<<"Ei koske\n";
    return false;


}

void dfs(int n) {
//    cout<<n<<endl;
    if(ans!=-1&&chs.size()>=ans) return;
    if(n<e) {
 //       if(ans>=0) return;
        for(int i=0;i<chs.size();i++) {
            if(!cross(i, s[n])) {
                chs[i].push_back(s[n]);
                dfs(n+1);
//                if(ans>=0) return;
                chs[i].pop_back();
            }
        }
        chs.resize(chs.size()+1);
        chs[chs.size()-1].push_back(s[n]);
        dfs(n+1);
        chs.pop_back();
    } else {
/*        cout<<n<<": \n";
        for(int i=0;i<chs.size();i++) {
            cout<<i<<":\n";
            for(int j=0;j<chs[i].size();j++) {
                for(int z=0;z<k;z++) {
                    cout<<chs[i][j].k[z]<<" ";
                }
                cout<<endl;
            }
        }
        cout<<"----\n";*/
        if(chs.size()<ans) ans=chs.size();
//        return;
    }

}
void solve() {

    ans=-1;
    dfs(0);    
}
int main() {
    int tim;
    cin>>tim;
    for(int j=0;j<tim;j++) {
        chs.resize(0);
        read();
        solve();
        cout<<"Case #"<<(j+1)<<": "<<ans<<endl;
    }

}
