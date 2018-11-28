#include<iostream>
#include<cassert>
#include<cstring>
#include<vector>
#include<queue>
#include<utility>
using namespace std;




const int MAXN = 11000;

bool visited[MAXN][MAXN];

vector<int> vine_pos;
vector<int> vine_len;
int love;

bool dfs(int v1,int v2){
    if(visited[v1][v2])return false;
    //cout<<"dfs("<<v1<<","<<v2<<")\n";
    visited[v1][v2]=true;
    double swing = vine_pos[v2]-vine_pos[v1];
    swing = min(swing,double(vine_len[v2]));
    //cout<<"swing = "<<swing<<"\n";
    if(swing >= love-vine_pos[v2])return true;

    for(int i=v2+1;i<vine_pos.size();i++){
        if(vine_pos[i]-vine_pos[v2] > swing)break;
        if(vine_pos[i]-vine_pos[v2] > vine_len[v2])
            continue;
        if(dfs(v2,i))return true;
    }
    return false;
}

int gs(int v1,int v2){
    int swing = vine_pos[v2]-vine_pos[v1];
    swing = min(swing,(vine_len[v2]));
    return swing;
}

bool can_do_cheap(int v1,int v2){
    double swing =gs(v1,v2);

    if(swing >= love-vine_pos[v2])return true;

    int best = 0;
    int bs = 0;
    for(size_t i=v2+1;i<vine_pos.size();i++){
        if(vine_pos[i]-vine_pos[v2] > swing)break;
        if(vine_pos[i]-vine_pos[v2] > vine_len[v2])
            continue;
        int s = gs(v2,i)+vine_pos[i];
        if(s>bs)
        {
            bs = s+vine_pos[i];
            best = i;
        }
    }
    if(best!=0)return can_do_cheap(v2,best);
    return false;
}


bool can_do(int v1,int v2){
    memset(visited,0,sizeof(visited));
    return dfs(v1,v2);
}

int main(){
    int t;
    cin>>t;
    for(int cno=1;cno<=t;cno++){
        int n;
        cin>>n;
        vine_pos.resize(0);
        vine_len.resize(0);
        vine_len.push_back(0);
        vine_pos.push_back(0);

        for(int i=0;i<n;i++){
            int p,l;
            cin>>p>>l;
            vine_pos.push_back(p);
            vine_len.push_back(l);
            //cout<<"p"<<p<<" l"<<l<<", ";
        }
        //cout<<"\n";
        cin>>love;
        cout<<"Case #"<<cno<<": ";
        if(can_do(0,1))
            cout<<"YES\n";
        else
            cout<<"NO\n";
    }
}
