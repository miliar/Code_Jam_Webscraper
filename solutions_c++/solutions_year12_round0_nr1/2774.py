#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
using namespace std;

int main() {

    int numberCase;
    cin >> numberCase;
    char alfa[] = {"yhesocvxduiglbkrztnwjpfmaq"};

    getchar();
    int aux;
    for(int i = 0; i < numberCase; i++) {
        string frase;
        getline(cin, frase);

        for(int j = 0; j < frase.length(); j++) {
            aux = frase[j];

            if(aux >= 97 and aux <= 122 )
                frase.at(j) = alfa[aux - 97];
        }
        cout << "Case #" << i + 1 << ": " << frase << endl;
    }
    return 0;
}
