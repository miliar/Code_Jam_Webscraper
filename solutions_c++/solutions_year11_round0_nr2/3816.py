#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ifstream entrada("B-small.in");
    ofstream salida("B-small.out");
    int Casos;
    entrada >> Casos;
    for(int caso=1; caso<=Casos; caso++){
        int C,D,N;
        entrada >> C;
        string s;
        string comb ="***";
        string opp = "**";
        if(C!=0)entrada >> comb;
        entrada >> D;
        if(D!=0)entrada >> opp;
        entrada >> N;
        entrada >> s;
        bool flag = true;
        while(flag){
            flag = false;
            bool salir = false;
            for(int i =1; i< s.size(); i++){
                if((s[i-1] == comb[0] && s[i] == comb[1])||(s[i-1] == comb[1] && s[i] == comb[0])){
                    s.erase(s.begin() + i-1);
                    s[i-1] = comb[2];
                    flag = true;
                    break;
                }
                for(int j=0;j<i;j++){
                    if((s[j] == opp[0] && s[i] == opp[1])||(s[j]==opp[1] && s[i] == opp[0])) {
                        s.erase(s.begin(),s.begin() + i+1);
                        flag=true;
                        salir= true;
                        break;
                    }
                }
                if(salir)break;
            }
        }




        salida << "Case #" << caso << ": [";
        if(s.size()!=0)for(int i=0; i<s.size()-1;++i){salida << s[i] << ", ";}
        if(s.size()!=0) salida << s[s.size()-1];
        salida << "]" << endl;
    }
    return 0;
}
