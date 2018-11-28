#include <iostream>

using namespace std;

const int infinite = 100000000;

int varmin[10001][2];
int nodes[10001][2];
int val[10001];

int m;

int getvarmin(int n, int v){
    if(varmin[n][v]!=-1){
        //cout << "direct: " << n << " " << v << " " << varmin[n][v] << endl;
        return varmin[n][v];
    }
    //cout << "n: " << n << "  v: " << v << endl;
    if(2*n + 1 > m){
        if(v == val[n]){
            varmin[n][v] = 0;
            //cout << n << " " << v << " " << varmin[n][v] << endl;
            return 0;
        } else {
            varmin[n][v] = infinite;
            //cout << n << " " << v << " " << varmin[n][v] << endl;
            return infinite;
        }
    } else {
        int varminim;
        if(v==1){
            if(nodes[n][0] == 1){
                varminim = getvarmin(2*n,1) + getvarmin(2*n + 1,1);
                if(nodes[n][1] == 1){
                    varminim <?= getvarmin(2*n,1) + getvarmin(2*n + 1,0) + 1;
                    varminim <?= getvarmin(2*n,0) + getvarmin(2*n + 1,1) + 1;
                }
            } else {
                //cout << "is or, " << nodes[n][1] << endl;
                varminim = getvarmin(2*n,1) + getvarmin(2*n + 1,1);
                varminim <?= getvarmin(2*n,1) + getvarmin(2*n + 1,0);
                varminim <?= getvarmin(2*n,0) + getvarmin(2*n + 1,1);
            }
        } else {
            if(nodes[n][0] == 1){
                //cout << "node " << n  << " is and, " << nodes[n][1] << endl;
                varminim = getvarmin(2*n,0) + getvarmin(2*n + 1,1);
                varminim <?= getvarmin(2*n,1) + getvarmin(2*n + 1,0);
                varminim <?= getvarmin(2*n,0) + getvarmin(2*n + 1,0);
            } else {
                //cout << "is or, " << nodes[n][1] << endl;
                varminim = getvarmin(2*n,0) + getvarmin(2*n + 1,0);
                if(nodes[n][1] == 1){
                    varminim <?= getvarmin(2*n,1) + getvarmin(2*n + 1,0) + 1;
                    varminim <?= getvarmin(2*n,0) + getvarmin(2*n + 1,1) + 1;
                }
            }
        }
        varmin[n][v] = varminim;
        //cout << n << " " << v << " " << varminim << endl;
        return varminim;
    }
}

int main(){
    int ncases;
    cin >> ncases;
    for(int casen = 1; casen <= ncases; casen++){
        int v;
        cin >> m >> v;
        for(int i=1;i<=(m-1)/2;i++){
            varmin[i][0] = -1;
            varmin[i][1] = -1;
            //cout << "reading nodes[" << i << "][0] and [1]" << endl;
            cin >> nodes[i][0] >> nodes[i][1];
        }
        for(int i=1;i<=(m+1)/2;i++){
            cin >> val[i + (m-1)/2];
            varmin[i + (m-1)/2][0] = (val[i + (m-1)/2] == 0? 0 : infinite);
            varmin[i + (m-1)/2][1] = (val[i + (m-1)/2] == 1? 0 : infinite);
        }
        int ans = getvarmin(1,v);
        if(ans >= infinite) cout << "Case #" << casen << ": IMPOSSIBLE" << endl;
        else cout << "Case #" << casen << ": " << ans << endl;
    }
}
        
