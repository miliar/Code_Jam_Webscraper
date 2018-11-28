#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool tot(vector <bool>& vis){
     for (int i = 0; i < vis.size(); i++) if (!vis[i]) return false;
     return true;
}

int main(){
    int c;
    cin >>c;
    for (int d = 0; d < c; d++){
        int n;
        cin >>n;
        char c;
        int b;
        int tb = 0, to = 0, posb = 1, poso = 1;
        for (int i = 0; i < n; i++) {
            cin >>c>>b;
            
            if (c=='O'){
               int tmp = max(tb+1, to+abs(b-poso)+1);
               to = tmp;
               poso = b;
            }
            else {
                 int tmp = max(to+1, tb+abs(b-posb)+1);
                 tb = tmp;
                 posb = b;
            }
            
        }
        
        cout <<"Case #"<<d+1<<": "<<max(to, tb)<<endl;
    }
    cin >>c;
}
