#include <iostream>
#include <algorithm>

using namespace std;

int main(){
   int t;
   cin >> t;

   for(int c = 0; c < t; c++){
        int n;
        cin >> n;

        int total = 0;
        int aux = 0;
        bool impossible = false;
        int menor = 1000001;
        for(int i = 0; i < n; i++){
            int j;
            cin >> j;

            aux = aux ^ j;
            if(aux != 0) impossible = true;
            else impossible = false;
            
            if(j < menor) menor = j;
            total += j;
        }

        total -= menor;

        if(impossible){
            cout << "Case #" << c+1 << ": NO" << endl;
        }
        else{
            cout << "Case #" << c+1 << ": " << total << endl;
        }       
   }

}
