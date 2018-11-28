#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

int n, m;
vector<string> p, w;
char str[10000];
//map<pair<int, string>, int>q;

int doit(string st){
    int len = st.size();
    int l = 0;
    int r;
    int now = 0;
    while (true){      
        for (r = l + 1; r < len; ++r)
            if (st[r] == '/') break;
        if (r == len){
            string tmp = "";        
            for (int j = l + 1; j <= r - 1; ++j) tmp += st[j];
            //q[make_pair(now, tmp)]++;
            break;      
        }
        else{
            string tmp = "";
            for (int j = l + 1; j <= r - 1; ++j) tmp += st[j];
            //q[make_pair(now, tmp)]++;
            l = r;
            now++;     
        }           
    }   
    return now + 1;            
}     

void init(){
    scanf("%d%d",&n, &m); 
    p.clear();
    w.clear();
    //q.clear();
    for (int i = 0; i < n; ++i){
        scanf("%s",str);
        //puts(str);
        string st = str;
        p.push_back(st);
    }
    for (int i = 0; i < m; ++i){
        scanf("%s",str);
        w.push_back(str);
    }
}

void run(){
    sort(w.begin(), w.end());
    int tot = 0;
    for (int i = 0; i < m; ++i){
        bool f = false;
        for (int j = 0; j < p.size(); ++j){
            if (p[j].find(w[i]) == 0 && (p[j].size() == w[i].size() || p[j][w[i].size()] == '/')){
               f = true;
            }
        } 
        if (f) continue;
        int maxnl = -1;
        int id = -1;
        for (int j = 0; j < p.size(); ++j){
            if (p[j].find(w[i]) == 0) continue;
            int len = min(p[j].size(), w[i].size());
            int samel = -1;
            for (int k = 0; k < len; ++k){
                if (p[j][k] != w[i][k]){
                   samel = k;
                   break;
                }
            }
            if (samel == -1) samel = len;
            if (maxnl < samel){
               maxnl = samel;
               id = j;
            }
        }
        //printf("%d %d %s %d\n",i, id, w[i].c_str(), maxnl);
        if (id == -1){
            tot += doit(w[i]);
        } 
        else{
            string tmps = w[i].substr(maxnl, w[i].size() - maxnl);     
            tot += doit(tmps);
        }
        p.push_back(w[i]);
    }
    printf("%d\n",tot);
}

int main(){
    int t;
    freopen("A4.in","r",stdin);
    freopen("A3.txt","w",stdout);
    scanf("%d",&t);
    for (int i = 1; i <= t; ++i){
        init();
        printf("Case #%d: ",i);
        run();
    }
    return 0;
}
