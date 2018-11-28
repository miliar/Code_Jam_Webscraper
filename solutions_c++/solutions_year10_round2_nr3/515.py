#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
using namespace std;

int main() {
    
    int T, n;
    ifstream in("in5.in");
    ofstream out("out.txt");
    in >> T;
    vector<int> V,C;
    int y,k,f,f2,ret = 0,j;
    for(int k1 = 1; k1 <= T; k1++) {
        in >> n;
        for(int i = 2; i <= n; i++)
            V.push_back(i);
        for(int i = 0; i < (1 << (n-2)); i++) {
            y = i;
            k = 0;
            while(y > 0) {
                if (y%2) C.push_back(V[k]);
                k++;
                y/=2;
            }
            C.push_back(n);
            f2 = 0;
            j = C.size() - 1;
            if (j == 0) f2 = 1;
            hell:;
                for(int j1 = 0; j1 < C.size(); j1++) 
                    if (j+1 == C[j1]) {
                        if (j1 != 0){
                            j = j1;
                            goto hell;
                        }
                        else f2 = 1;     
                    }
            if (f2) {
           
                ret++;
            }   
            C.clear();
        }
        V.clear(); 
   
        out<<"Case #"<<k1<<": "<<(ret%100003)<<endl;
             ret = 0;
    }             
}
