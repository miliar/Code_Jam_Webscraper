#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void increment(string* str, int* count, string s, int max){
    for (int i = 0; i < max; i++) {
        if (str[i] == s) count[i]++;
    } 
}

int min (int* v, int dim) {
    int n = v[0];
    for (int i = 1; i < dim; i++) if (v[i]<n) n = v[i];    
    return n;
}

int sum0 (int* v, int dim) {
    int n = 0;
    for (int i = 0; i < dim; i++) if (v[i]>0) n++;    
    return n;
}

void zero (int* v, int dim) {
    for (int i = 0; i < dim; i++) v[i]=0;    
}

int main(int argc, char *argv[])
{
    string line;
    const int MaxVect = 1000;
    int cases[MaxVect];
    int Ncase;
    string se[MaxVect];
    int secount[MaxVect];
    int Nse;
    int Nstr;
    int ncambi;
    ifstream myfile (argv[1]);
    if (myfile.is_open()) {
       getline (myfile,line);
       Ncase = std::atoi(line.c_str());
       for (int i = 0; i < Ncase; i++) {
           getline (myfile,line);
           ncambi = 0;
           Nse = std::atoi(line.c_str());
           for (int j = 0; j < Nse; j++) {
               getline (myfile,line);
               se[j] = line;
               secount[j] = 0;
           }
           getline (myfile,line);
           Nstr = std::atoi(line.c_str());
           for (int j = 0; j < Nstr; j++) {
               getline (myfile,line);
               increment(se, secount, line, Nse);  
               if (sum0(secount, Nse) == Nse) {
                  ncambi++;
                  zero (secount, Nse);
                  increment(se, secount, line, Nse); // lascio ad 1 l'attuale
               }
           }
           cout << "Case #" << i+1 <<": " <<ncambi<<endl;
           //for (int k = 0; k< 3; k++) cout << se[k] << ": " << secount[k] << endl; 
           //cout <<"sum0(secount, Nse): " << sum0(secount, Nse) << endl;  
       }                        
    }
    else cout << "Unable to open " << argv[1] << "\n";
    return EXIT_SUCCESS;
}
