#include <iostream>
#include <cstring>
#include <sstream>
using namespace std;

#define MAX 10000

int adj[MAX][MAX];
int nadj[MAX];
string tree[MAX];
int push_pos, n, m;

int cria(string& path)
{
    for(int i = 0; i < path.size(); i++) {
        if (path[i] == '/')
            path[i] = ' ';
    }
    int ret = 0;
    istringstream in(path);
    string no;
    int par = 0;
    for(;;) {
        if (!(in >> no))
            break;
        for(int i = 0; i < nadj[par]; i++) {
            if (tree[adj[par][i]] == no) {
                par = adj[par][i];
                goto next;
            }
        }
        tree[push_pos] = no;
        adj[par][nadj[par]++] = push_pos;
        //cout << "cria: " << no << " filho de " << tree[par] << endl;
        par = push_pos++;
        ret++;
next:
            continue;
    }
    return ret;
}


int main()
{
    int T;
    cin >> T;
    for(int cas = 1; cas <= T; cas++) {
        cin >> n >> m;
        memset(nadj, 0, sizeof(nadj));
        push_pos = 1;
        tree[0] = "/";
        string path;
        for(int i = 0; i < n; i++) {
            cin >> path;
            cria(path);
        }
        int ret = 0;
        for(int i = 0; i < m; i++) {
            cin >> path;
            ret += cria(path);
        }
        printf("Case #%d: %d\n", cas, ret);
    }

    return 0;
}

