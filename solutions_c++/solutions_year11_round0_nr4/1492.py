#include<iostream>
#include<fstream>
#include <iomanip>
using namespace std;



int main(){
    
    ios::sync_with_stdio(0);
    cout.precision(6);
    int T;
    int N;
    double wyn;
    int pom;
    cin>>T; T++;
 //   fstream plik("goro.txt") ;    // ifstream - odczyt z pliku, ofstream - zapis, fstream - odczyt+zapis 

    for(int q=1;q<T;q++)
    {
    cin>>N; N++; wyn=0.0;
            for(int i=1;i<N;++i)
            {       cin>>pom;
                    if(pom!=i){wyn=wyn+1;} 
                    
                    }
            cout<<"Case #"<<q<<": "<<fixed <<(wyn)<<"\n";
            }

// plik.close() ; 
//cin>>pom;
};
