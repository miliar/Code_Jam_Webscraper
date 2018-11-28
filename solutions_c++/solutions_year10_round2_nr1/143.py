#include<iostream>
#include<set>
#include<string>
using namespace std;

set<string> root;
int ans =0;
void add(string s)
{
    int t = 0;
    while(t!=string::npos)
    {
        t = s.find('/',t+1);
        if(t==string::npos)break;
        string ss  = s.substr(0,t);
        if(root.find(ss)==root.end()){
            root.insert(ss);
            ans++;
        }
    }
    if(root.find(s) == root.end()){
        root.insert(s);
        ans++;
    }
}

int main()
{
    string s;
    int T,n,m;
    cin >> T;
    root.insert("/");
    for(int k =1 ; k<=T;k++){
        cin >> n>>m;
        root.clear();
        root.insert("/");
        for(int i = 0;i < n;i++){
            cin >> s;
            add(s);
        }
        ans =0;
        for(int i = 0; i<m;i++){
            cin >> s;
            add(s);
        }
        cout << "Case #"<<k<<": "<<ans << endl;
    }
}
