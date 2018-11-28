#include<iostream>
#include<fstream>
#include <iomanip>
using namespace std;



int main(){
    
    ios::sync_with_stdio(0);
   // cout.precision(6);
    int T;
    int N;
    long long int sum;
    int min=-1;
    int xxor=0;
    int pom;
    cin>>T; T++;
 //   fstream plik("goro.txt") ;    // ifstream - odczyt z pliku, ofstream - zapis, fstream - odczyt+zapis 

    for(int q=1;q<T;q++)
    {
    cin>>N; N++; min=0; sum=0; xxor=0;
            for(int i=1;i<N;++i)
            {       cin>>pom;
            sum=sum+pom;
            
                    if(pom<min || min==0){min=pom;} 
                   xxor=xxor^pom;
                    }
                    
                    
                    if(xxor==0){
                               
                               
                                       cout<<"Case #"<<q<<": "<<(sum-min)<<"\n";
                               }else{
                                     
                                     
                                     
                                             cout<<"Case #"<<q<<": "<<"NO"<<"\n";}
    
            }

// plik.close() ; 
//cin>>pom;
};
