#include <iostream>
#include <sstream>
#include <cmath>
#include <cstring>
#include <map>
#include <string>
#include <vector>
#define inf 1000000000
#define len(a) int((a).size())
#define pb push_back
using namespace std;

struct dir {
    string name;
    map<string, dir> dirs;
    
    dir(){
        
    }
    
    dir(string nm){
        name = nm;
    }    
    
    int add(int id, vector<string> &w){
        if (id >= len(w)){
            return 0;    
        }
        string cur = w[id];
        
        int res = 0;
        if (dirs.find(cur) == dirs.end()){
            res++;
            dirs[cur] = dir(cur);
        }
        res += dirs[cur].add(id+1, w);
        return res;
    } 
};

int N, M;

vector<string> explode(string w){
    vector<string> res;
    string r = "";
    w += "/";
    for (int i = 0; i < len(w); i++){
        if (w[i] == '/'){
            if (r != ""){
                res.pb(r);
                //cout << r << " | ";
                r = "";    
            }
        } else {
            r += w[i];    
        }    
    }    
    //cout << endl;
    return res;
}

int solve(){
    cin >> N >> M;
    dir root("/");
    for (int i = 0; i < N; i++){
        string tmp;
        cin >> tmp;
        vector<string> path = explode(tmp);
        root.add(0, path);
    }
    
    int res = 0;
    for (int i = 0; i < M; i++){
        string tmp;
        cin >> tmp;
        vector<string> path = explode(tmp);
        res += root.add(0, path);
    }
    return res;
}

int main(){
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++){
        int r = solve();
        cout << "Case #" << t << ": " << r << endl;
    }
    return 0;    
}
