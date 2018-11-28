#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <cctype>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <utility>

#define forn(i, n) for(int i=0; i < (int)(n); i++)

using namespace std;

int main() {
    int n;
    cin >> n;
    
    for(int z=1; z<=n; z++) {
        //Read inputs
        int Ncomb;
        cin >> Ncomb;
        vector<string> comb(Ncomb);
        forn(i, comb.size()) {
            cin >> comb[i];
        }
        int Nopp;
        cin >> Nopp;
        vector<string> opp(Nopp);
        forn(i, opp.size()) {
            cin >> opp[i];
        }
        int N;
        cin >> N;
        string cars;
        cin >> cars;
        
        char ap[N];
        int pos = 0;
        forn(i, cars.size()) {
            bool rajoute = true;
            char remplace;
            if(pos>0) {
                forn(j, comb.size()) {
                    if((ap[pos-1] == comb[j][0] && cars[i] == comb[j][1])
                            || (ap[pos-1] == comb[j][1] && cars[i] == comb[j][0])) {
                        remplace = comb[j][2];
                        rajoute = false;
                        break;
                    }
                }
            }
            if(rajoute) {
                bool clear = false;
                forn(j, pos) {
                    forn(k, opp.size()) {
                        if((cars[i] == opp[k][0] && ap[j] == opp[k][1])
                                || (cars[i] == opp[k][1] && ap[j] == opp[k][0])) {
                            clear = true;
                            break;
                        }
                    }
                    if(clear) break;
                }
                if(clear) {
                    pos = 0;
                } else {
                    ap[pos++] = cars[i];
                }
                
            } else {
                ap[pos-1] = remplace;
            }
        }
        ap[pos] = 0;
        
        int size = strlen(ap);
        char res[size+1];
        strcpy(res, ap);
        
        //vector<char> res(0);
        
        
        //Print outputs
        printf("Case #%d: ", z);
        cout << "[";
        for(int i=0; i<size; i++) {
            cout << res[i];
            if(i != size-1) {
                cout << ", ";
            }
        }
        cout << "]" << endl;
    }
    
    return 0;
};
