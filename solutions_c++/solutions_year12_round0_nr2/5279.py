#include <iostream>
#include <fstream>
#include <cstdlib>


using namespace std;

int main()
{

    ifstream inFile;
    ofstream outFile;
    inFile.open("input.txt");
    outFile.open("output.txt");

    int x, qtd, n, s, p, notas[100];
    int contador;

    inFile >> x;
    qtd = x; // qtd

    for(int k=0; k<qtd; k++){

        contador = 0;

        inFile >> n;
        inFile >> s;
        inFile >> p;
        for(int i=0; i<n; i++)
            inFile >> notas[i];
/*
        cout << "n: " << n << endl;
        cout << "s: " << s << endl;
        cout << "p: " << p << endl;
        cout << "notas: " ;

        for(int i=0; i<n; i++)
            cout << notas[i] << " ";
        cout << endl << "------"<< endl;
*/

        for(int i=0; i<n; i++){
            if(p <= 1){
                if(notas[i]!=0 || p==0) contador++;
            }else
                if(notas[i] >= p*3 -2) contador++;
                else if( (notas[i] >= p*3 -4) && s > 0){
                        contador++;
                        s--;
                    }
        }

//            cout << "Case #" << k+1 << ": " << contador << endl;
//            system("pause");

         outFile << "Case #" << k+1 << ": " << contador << endl;
    }


    return 0;
}
