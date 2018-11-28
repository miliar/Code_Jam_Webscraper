#include <vector>
#include <map>
#include <iostream>
using namespace std;

int main(){
    int casos;
    cin >> casos;
    string esta;
    getline(cin, esta);
    esta = "welcome to code jam";
    map<char, vector<int> > M;
    for(int i = 0; i < esta.size(); i++){
        if (!M.count(esta[i]))
            M[esta[i]] = vector<int>(1, i+1);
        else
            M[esta[i]].push_back(i+1);
    }
    for(int caso = 1; caso <= casos; caso++){
        vector<int> estados(20,0);
        estados[0] = 1;
        getline(cin,esta);
        for(int i = 0; i < esta.size(); i++){
            for(int j = 0; j < M[esta[i]].size(); j++){
                int nuevo = M[esta[i]][j];
                int estado = nuevo-1;
                estados[nuevo] += estados[estado];
                while (estados[nuevo] > 9999) estados[nuevo] -= 10000;
            }
        }
        int cont = estados[19];
        cout << "Case #" << caso << ": ";
        cout << (cont/1000)%10 << (cont/100)%10 << (cont/10)%10 << cont%10 << endl;
    }
    return 0;
}
