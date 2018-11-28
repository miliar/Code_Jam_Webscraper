//
//


#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

class snapper {

   public:
   bool power;
   bool sw;

   snapper(void);
   bool outputcheck() { return power && sw; }

};

snapper::snapper():power(false),sw(false){
}

bool mainroop(int n, int k){
    vector<snapper> sn(n);

    sn[0].power = true;

    for ( int i = 0; i < k; i++ ) {
        for (int j =n; j > 0 ; j--) {
            if ( sn[j-1].outputcheck() ) {
                sn[j].sw =!sn[j].sw;
            }
        }
        sn[0].sw = !sn[0].sw;

        bool e = true;

        for (int j =1; j < n; j++) {
            if ( !sn[j-1].outputcheck() ) {
                e = false;
            }
            sn[j].power = e;
        }
    }
    return sn[n-1].outputcheck();
}

int main() {

   ifstream ifile("input.txt");

   int T;
   ifile >> T;

   for ( int i = 0 ; i < T ; i++ ) {
       int N,K;
       ifile >> N >> K;
       if ( mainroop(N,K) ) 
         cout << "Case #"<< i+1 <<": "<< "ON" << endl;
       else
         cout << "Case #"<< i+1 <<": "<< "OFF" << endl;
   }
 
   return true;

}
