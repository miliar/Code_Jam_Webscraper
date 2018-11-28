#include <cstdio>
#include <cstring>
#include <queue>
#include <vector>

using namespace std;

int T, n, m, nivel[512];
int nadj[512], C=1;
int adj[512][512];
bool nocaminho[512];

vector<int> pais[512];

vector<vector<int> > lista(int u) {
    vector<vector<int> > R;
    if (u == 0) {
        vector<int> v;
        v.push_back(0);
        R.push_back(v);
        return R;
    }
    if (pais[u].empty()) {
            vector<vector<int> > vazio;
            return vazio;
    }
    for (int i=0;i<(int)pais[u].size();i++) {
        vector<vector<int> > S = lista(pais[u][i]);
        for (int j=0;j<(int)S.size();j++)
            S[j].push_back(u);
        for (int j=0;j<(int)S.size();j++)
            R.push_back(S[j]);
    }
    return R;
}

int main() {

    for(scanf("%d",&T);T--;) {
        scanf("%d %d",&n,&m);
        memset(nadj,0,n*sizeof(int));
        for (int i=0;i<m;i++) {
            int v1,v2;
            scanf("%d,%d",&v1,&v2);
            adj[v1][nadj[v1]++] = v2;
            adj[v2][nadj[v2]++] = v1;
        }
        for (int i=0;i<n;i++)
            pais[i].clear();
        queue<int> Q;
        memset(nivel,0x3f,n*sizeof(int));
        Q.push(0);
        nivel[0]=0;
        while (!Q.empty()) {
            int u = Q.front();
            Q.pop();
            if (u == 1) break;
            for (int i=0;i<nadj[u];i++) if (nivel[adj[u][i]]==0x3f3f3f3f) {
                nivel[adj[u][i]] = nivel[u]+1;
                Q.push(adj[u][i]);
                pais[adj[u][i]].clear();
                pais[adj[u][i]].push_back(u);
            } else if (nivel[adj[u][i]] == nivel[u]+1)
                pais[adj[u][i]].push_back(u);
        }
        //lista tashdf
        vector<vector<int> > l = lista(1);

        int resp = 0;
        printf("Case #%d: %d ",C++, (int)l[0].size()-2);
        for (int i=0;i<(int)l.size();i++) {
            l[i].pop_back();
            memset(nocaminho,false,n*sizeof(bool));
            for (int j=0;j<(int)l[i].size();j++)
                nocaminho[l[i][j]]=true;
            int c = 0;
            for (int j=0;j<n;j++) if (!nocaminho[j]) {
                bool temgente = false;
                for (int k=0;k<nadj[j];k++)
                    if (nocaminho[adj[j][k]]) {
                        temgente= true;
                        break;
                    }
                if (temgente)
                    c++;
            }
            resp = max(resp,c);
        }
        printf("%d\n",resp);
    }

    return 0;
}
