#include <cstdio>
#include <string>
#include <map>
#include <vector>
#include <set>
#define MAX_DIF 50000

using namespace std;

map<string, int> index;
set<int> sons[MAX_DIF];

vector<string> split()
{
    string last = "", path;
    vector<string> sol;
    char lin[1024];
    fgets(lin, 1024, stdin);
    path = lin;
    for (size_t i=0; i<path.length() && path[i] > ' '; i++){
        if (path[i] == '/')
            sol.push_back(last);        
        last += path[i];
    }
    sol.push_back(last);
    return sol;
}

int norm(const string &s){
    int nr = index.size();
    if (index.find(s) != index.end())
        nr = index[s];
    else
        index[s] = nr;
    return nr;
}

bool inThere(string &a, string &b){
    int par = norm(a), fiu = norm(b);
    bool res = sons[par].find(fiu) != sons[par].end();
    //fprintf(stderr, "%s %d %s %d %d\n", a.c_str(), par, b.c_str(), fiu, res);
    return res;
}

int addPath(vector<string> &path){
    int n = path.size();
    int k = 1, rez = 0;
    while (k < n && inThere(path[k-1], path[k]))
        k++;
    //fprintf(stderr, "%d %d\n", k, n-1);
    for (; k<n; k++){
        rez++;
        sons[norm(path[k-1])].insert(norm(path[k]));
        //fprintf(stderr, "Inserting %s %d %s %d\n", path[k-1].c_str(), norm(path[k-1]), path[k].c_str(), norm(path[k]));
    }
    //fprintf(stderr, "%d\n", rez);    
    return rez;
}

void solve(int tst)
{
    int n, m, total = 0, sol = 0;
    map<string, int> index;
    scanf("%d %d\n", &n, &m);
    index[""] = 0;
    for (int i=0; i<n; i++){
        vector<string> path = split();
        total += addPath(path);
    }
    
    //fprintf(stderr, "%d\n", total);
    
    for (int i=0; i<m; i++){
        vector<string> path = split();
        sol += addPath(path);        
    }
    
    fprintf(stderr, "Total: %d %d\n", total, sol);
    printf("Case #%d: %d\n", tst, sol);
        
    index.clear();
    for (int i=0; i<MAX_DIF; i++)
        sons[i].clear();
}

int main()
{
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int tst;
    scanf("%d", &tst);
    for (int i=1; i<=tst; i++)
        solve(i);
    fflush(stdout);
    //while (1);
    return 0;
}
