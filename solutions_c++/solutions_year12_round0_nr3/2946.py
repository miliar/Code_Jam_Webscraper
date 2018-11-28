#include <iostream>
#include <sstream>
#include <string>
#include <cstdio>
using namespace std;

bool reciclado(string n, string m) {

    int total = 0;
    int tam = m.length();
    int aux;
    for(int j = 0; j < tam - 1; j++) {
        aux = n.at(0);
        for(int i = 0; i < tam - 1; i++) {
            n.at(i) = n.at(i + 1);
        }
        n.at(tam - 1) = aux;

        if(m == n)
            return true;
    }

    return false;
}
int main() {

    int numberCase;
    string sn, sm;
    int a, b;
    int total;
    scanf("%d", &numberCase);

    for(int i = 1; i <= numberCase; i++) {
        scanf("%d %d", &a, &b);
        getchar();

        total = 0;
        for(int n = a; n <= b - 1; n++) {
            for(int m = n + 1; m <= b; m++) {

                    stringstream out;
                    stringstream out2;
                    out << n;
                    sn = out.str();
                    out2 << m;
                    sm = out2.str();
                    //cout << "a e b: " << sn << " , "<< sm  << endl;
                    if(reciclado(sn, sm)) {
                        total++;
                    }
            }
        }
        cout << "Case #" << i << ": " << total << endl;

    }

    return 0;
}
