#include <iostream>
#include <stdlib.h>
#include <fstream>


using namespace std;

int main(){
    
    long long N,T,C[2000],sum,tmp,min;
    
    ifstream in("1.in");
    ofstream out("1.out");
    
    
    in >> N;
    

    for (int i = 0;i < N;i++){
        in >> T;
        tmp = 0;
        sum = 0;
        for (int j = 0;j<T;j++){
            in >> C[j];
            tmp = C[j]^tmp;
            sum += C[j];
            if ( j == 0) min = C[j];
            else if (C[j]<min) min = C[j];
        }
        if (!tmp) out << "Case #" << i+1 << ": " << sum - min << endl;
        else out << "Case #" << i+1 << ": NO" << endl;
    }
    system("pause");
}
