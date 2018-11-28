#include <iostream>
#include <string>

using namespace std;

int main() {
    int L,D,N;
    cin >> L >> D >> N;
    
    string words[D];
    for(int i=0; i<D; ++i) cin >> words[i];
    
    string alien_lan[N][L];
    for(int i=0; i<N; ++i) {
        string lan;
        cin >> lan;
        for(int j=0, k = 0; j<L; ++j, ++k) {
            if(lan[k]=='(') {
                int ini = k;
                while(lan[k]!=')') ++k;
                alien_lan[i][j] = lan.substr(ini+1,k-ini-1);
            }
            else alien_lan[i][j] = lan[k];
        }
        int count = 0;
        for(int k=0; k<D; ++k) {
            //cout << words[k] << endl;
            bool flag;
            for(int j=0; j<L; ++j) {
                flag = false;
                //cout << words[k][j] << " -> " << alien_lan[i][j] << " ";
                for(int l = 0; l<alien_lan[i][j].size(); ++l) {
                    if(words[k][j]==alien_lan[i][j][l]) {
                        flag = true;
                        break;
                    }
                }
                if(!flag) break;
            }
            if(flag) count++;
            //cout << count << endl;
        }
        cout << "Case #" << i+1 << ": " << count << endl;
    }
    
}
