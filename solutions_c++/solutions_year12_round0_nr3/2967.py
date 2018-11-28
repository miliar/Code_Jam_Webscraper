#include <iostream>
//#include <set>
#include <string>
#include <cstdlib>
#include <sstream>

using namespace std;

int main(){
    int T;
    cin >> T;
    long long A,B, valor, cont;
    string auxA, sub1, sub2;
    stringstream ss;
    //set<long long> conj;
    for(int i = 1; i <= T; i++){
        cin >> A;
        cin >> B;
        cont = 0;
        for(long long j = A; j <= B; j++){
            ss.str("");
            ss << j;
            auxA = ss.str();
            for(long long k = 1; k < auxA.size(); k++){
                valor = A-1;
                sub1 = auxA.substr(auxA.size()-k,k); //final
                sub2 = auxA.substr(0,auxA.size()-k); //começo
                sub1 += sub2;
                valor = atoi(sub1.c_str());
                if((valor <= B) && (valor >= j+1)) cont++;
            }
        }
        cout << "Case #" << i << ": " << cont << endl;
    }
    return 0;
}
