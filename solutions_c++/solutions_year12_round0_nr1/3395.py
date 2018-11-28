#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    char dicc[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    vector<char> diccionari (dicc, dicc + sizeof(dicc) / sizeof(char) );
    int C;
    cin >>C;
    string aux;
    getline(cin,aux);
    int c = 0;
    while (c < C) {
        getline(cin,aux);
        cout <<"Case #" <<c+1 <<": ";
        for(int i =0; i < aux.size();i++) {
            if (aux[i] == ' ') cout <<aux[i];
            else {
                int num = aux[i] - 'a';
                //cout <<num <<" ";
                cout <<diccionari[num];
            }
        }
        c++;
        cout <<endl; 
    }
    
}
