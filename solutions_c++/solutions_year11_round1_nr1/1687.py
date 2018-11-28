#include <iostream>
#include <string>
#include <sstream>
#include <list>
using namespace std;

void processLine( string line, int test ){
    std::istringstream stream(line);
    long N;
    double Pd,Pg;
    stream >> N;
    stream >> Pd;
    stream >> Pg;
    bool possible = false;

    if( Pg == 100 && Pd != 100 ||
            Pg == 0 && Pd != 0){
        possible = false;

    }else{

        //calcular si se puede obtener un Pd exacto
        if( Pd == 0 || Pd == 100 || N % 100 == 0 ){
            possible = true;
        }else{
            double cien=100;
            double n, p= Pd/cien;
            for(long i = N*p; i > 0 ; i--){
                n = i/p;
                if( n == long(n) ) {
                    possible = true;
                    break;
                }
            }
        }
    }
    cout << "Case #" << test << ": ";
    if( possible ){
        cout <<  "Possible" << endl;
    }else{
        cout << "Broken" << endl;
    }
}

int main(int argc, char *argv[])
{
    int NTest;
    std::cin >> NTest;
    int test;
    std::string line;
    std::getline(std::cin, line);
    for ( test = 1 ; test <= NTest; test++){
        std::getline(std::cin, line);
        processLine(line, test);
    }

    return 1;
}
