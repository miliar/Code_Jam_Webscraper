#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

const int MAXN = 100;

int main(){
    int t;
    cin >> t;
    
    for(int lp=1;lp<=t;++lp){
        int n;
        cin >> n;
        string table[MAXN];
        for(int i=0;i<n;++i){
            cin >> table[i];
        }
        
        int nplay[MAXN];
        int nwin[MAXN];
        for(int i=0;i<n;++i){
            nplay[i] = 0;
            nwin[i] = 0;
            for(int j=0;j<n;++j){
                nplay[i] += (table[i][j] != '.') ? 1 : 0;
                nwin[i] += (table[i][j] == '1') ? 1 : 0;
            }
        }
        
        double wp[MAXN];
        double owp[MAXN];
        for(int i=0;i<n;++i){
            wp[i] = double(nwin[i])/nplay[i];
            owp[i] = 0;
            for(int j=0;j<n;++j){
                if(table[i][j] != '.'){
                    owp[i] += double(nwin[j] - ((table[j][i] == '1') ? 1 : 0))/(nplay[j] - 1);
                }
            }
            owp[i] /= nplay[i];
        }
        
        double oowp[MAXN];
        for(int i=0;i<n;++i){
            oowp[i] = 0;
            for(int j=0;j<n;++j){
                if(table[i][j] != '.'){
                    oowp[i] += owp[j];
                }
            }
            oowp[i] /= nplay[i];
        }
        
        cout << "Case #" << lp << ":\n";
        for(int i=0;i<n;++i){
            cout << 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] << "\n";
        }
        
    }
    
    return 0;
}