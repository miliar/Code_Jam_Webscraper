#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

int main(int argc, char *argv[])
{
    ofstream outfile;
    ifstream infile;
    infile.open("A.in", ifstream::in);
    outfile.open("A.out", ofstream::out);
    unsigned int cantCasos;
    infile >> cantCasos;
    unsigned int caso = 1;
    while(cantCasos>0)
    {
        int res = 0;
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

        unsigned long long int *x = new unsigned long long int[n];
        unsigned long long int *y = new unsigned long long int[n];

        x[0] = x0;
        y[0] = y0;
        
        for(int i = 1; i<n;i++){
            x[i] = (A*x[i-1]+B) % M;
            y[i] = (C*y[i-1]+D) % M;
        }

        for(int i=0;i<n-2;i++){                             
            for(int j=i+1;j<n-1;j++){
                for(int m=j+1;m<n;m++){
                    if((x[i]+x[j]+x[m])%3==0 && (y[i]+y[j]+y[m])%3==0)
                        res+=1;
                }
            }
        }
                
        outfile << "Case #"<<caso<<": "<<res<<endl;        
        
        delete[] x;
        delete[] y;
        caso++;
        cantCasos--;
    }
    infile.close();
    outfile.close();
    return EXIT_SUCCESS;
}
