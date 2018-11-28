#include <iostream>
#include <map>
#include <vector>
#include <iomanip>
#include <cstring>
#include <string>

using namespace std;

int main(){
    vector<string> tab;
    string line;
    int t, tt=1;
    int n, m;
    cin >> t;
    while(t--){
        cin >> n >> m;
        for(int i = 0; i < n; i++){
            cin >> line;
            tab.push_back(line);
        }
        
        cout << "Case #" << tt++ << ":" << endl;
        
        bool flag = true;
        for(int i = 0; i < n-1; i++){
            for(int j = 0; j < m-1; j++){
                if(tab[i][j] == '#'){
                    if(tab[i+1][j] == '#' && tab[i+1][j+1] == '#' && tab[i][j+1] == '#'){
                        tab[i][j] = '/';
                        tab[i+1][j] = '\\';
                        tab[i+1][j+1] = '/';
                        tab[i][j+1] = '\\';
                    }
                    else {;flag = false; }
                }
            }
        }
        for(int i = 0; i < n; i++){
                if(tab[i][m-1] == '#') {; flag = false; }
        }
        for(int j = 0; j < m; j++){
                if(tab[n-1][j] == '#') {;flag = false; }
        }
        if(flag){
            for(int i = 0; i < n; i++){
                cout << tab[i] << endl;    
            }
        }
        else  cout << "Impossible" << endl;     
        
        tab.clear(); 
    }
    return 0;   
}
