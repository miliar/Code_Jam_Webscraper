#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
using namespace std;

int main(int argc, char *argv[])
{
    ifstream infile;
    ofstream outfile;

    infile.open("entrada.in", ifstream::in);
    outfile.open("salida.out", ofstream::out);

    unsigned int cantidadInstancias;
    infile >> cantidadInstancias;

    for(int instancia=1;instancia<=cantidadInstancias;instancia++){
        unsigned long long int n;
        unsigned long long int A;
        unsigned long long int B;
        unsigned long long int C;
        unsigned long long int D;
        unsigned long long int x0;
        unsigned long long int y0;
        unsigned long long int M;
        
        infile >> n;
        infile >> A;
        infile >> B;
        infile >> C;
        infile >> D;
        infile >> x0;
        infile >> y0;
        infile >> M;
        
        //TREES POSITIONS
        long long int trees[100000][2];
        
        trees[0][0] = x0;
        trees[0][1] = y0;
            //cout << "arbol: " << trees[0][0] << " " << trees[0][1] << endl;
        for(int i=1; i<= n-1;i++){
          trees[i][0] = (A * trees[i-1][0] + B) % M;
          trees[i][1] = (C * trees[i-1][1] + D) % M;
            //cout << "arbol: " << trees[i][0] << " " << trees[i][1] << endl;
        }
        int total = 0;
        
        for(int i=0;i<=n-3;i++){

            for(int j=i+1;j<=n-2;j++){

                for(int k=j+1;k<=n-1;k++){
                    //cout << "arbol i: " << trees[i][0] << " " << trees[i][1] << endl;
                    //cout << "arbol j: " << trees[j][0] << " " << trees[j][1] << endl;
                    //cout << "arbol k: " << trees[k][0] << " " << trees[k][1] << endl;
                    float centerx = float (trees[i][0] + trees[j][0] + trees[k][0]) / 3;
                    //cout << trees[i][0] << "  " << trees[j][0] << " " << trees[k][0] << " " << centerx << endl;
                    float centery =  float (trees[i][1] + trees[j][1] + trees[k][1]) / 3;
                    //cout << trees[i][1] << "  " << trees[j][1] << " " << trees[k][1] << " " << centery << endl;
                    //for(int m = 0; m<=n-1;m++){
                        //cout << centerx << "  " << centery << " " << trees[m][0] << " " << trees[m][1] << endl;
                        //if(centerx == trees[m][0] && centery == trees[m][1]){
                        if(centerx == floor(centerx) && centery == floor(centery)) {
                             total++;
                        }
                    //}
                }
            }
        }
        
        
        cout << "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" << endl;
        
        outfile << "Case #" << instancia << ": " << total << endl;
    }
    
    system("PAUSE");
    infile.close();
    outfile.close();
    return EXIT_SUCCESS;
}
