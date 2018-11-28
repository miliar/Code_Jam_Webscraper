#include<algorithm>
#include<iostream>
#include<string>
using namespace std;

const int MAXS  =   100+10;
const int MAXQ  =   1000+10;

int S,Q;
string engine[MAXS];
int num[2*MAXQ];
bool app[MAXS];

int find_engine(string &str){
    for(int i=1; i<=S; ++i)
        if(str == engine[i])return i;
    return 0;
}

void init(){
    string str;
    
    cin>>S;
    getline(cin, str);
    for(int i=1; i<=S; ++i)getline(cin, engine[i]);
    cin>>Q;
    getline(cin, str);
    for(int i=0; i<Q; ++i){
        getline(cin, str);
        num[i<<1] = find_engine(str);
        num[(i<<1)+1] = num[i<<1];
    }
    //cout<<"Quanlify: "<<S<<" "<<Q<<endl;
}

void solve(){
    memset(app, false, sizeof(app));
    int apped = 0;
    int res = 0;
    for(int i=0; i<Q<<1; ++i){
        if(num[i] && !app[num[i]])++apped;
        //cout<<i<<" "<<apped<<endl;
        app[num[i]] = true;
        if(apped == S){
            apped = 0;
            memset(app, false, sizeof(app));
            ++res;
        }
    }
    cout<<res<<endl;
}

int main(){
    int N;
    cin>>N;
    for(int i=1; i<=N; ++i){
        init();
        cout<<"Case #"<<i<<": ";
        solve();
    }
}
