#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int br[31][2];

int main(){
    int t;
    cin >> t;

    for(int i=0;i<31;++i){
        br[i][0] = (int)ceil((double)i/3);
        br[i][1] = (i+1)/3 + 1;
    }
    br[0][1] = -2;
    br[1][1] = -2;
    br[29][1] = -2;
    br[30][1] = -2;

    for(int i=0;i<t;++i){
        int n,s,p;
        cin >> n >> s >> p;

        int tmp, ok=0, cand=0;
        for(int j=0;j<n;++j){
            cin >> tmp;
            if(br[tmp][0] >= p){
                ok++;
            }else if(br[tmp][1] == p){
                cand++;
            }
        }
        cout << "Case #" << i+1 << ": " << ok + min(cand, s) << endl;
    }
}
