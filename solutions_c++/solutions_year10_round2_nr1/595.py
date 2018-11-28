#include <iostream>
#include <cstring>
#include <vector>
#include <set>
using namespace std;

set<string> pathm;

string pop(string path){
    int i=path.size()-1;
    while(path[i]!='/')i--;
    path.resize(i);
    //path[i]=0;
    return path;
}

int create(string path){
    int cnt=0;
    while(pathm.find(path)==pathm.end() && path!=""){
        pathm.insert(path);
        cnt++;
        path=pop(path);
    }
    return cnt;
}
void solve(){
    int n,m,cnt;    
    scanf("%d%d",&n,&m);
    pathm.clear();
    string ts;
    for(int i=0;i!=n;++i){
        cin>>ts;
        create(ts);
    }
    for(int j=0;j!=m;++j){
        cin>>ts;
        cnt+=create(ts);
    }
    cout<<cnt<<endl;
}

int main(){
    //cout<<pop("/home")<<endl;
    int cases;
    scanf("%d",&cases);
    for(int i=0;i!=cases;++i) {printf("Case #%d: ",i+1);solve();}
    return 0;
}
