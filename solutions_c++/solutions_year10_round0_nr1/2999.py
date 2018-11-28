//Rakib Ansary Saikot

//Google code jam
//Snapper Chain

#include <iostream>
#include <fstream>

using namespace std;

typedef unsigned long long ULONG;

ULONG Pow(int base, int power);

int main(){
    ifstream cin ("large.in");
    ofstream cout ("output.txt");

    int t;
    cin >> t;
    for (int i = 0; i < t; i++){
        int n, k;
        cin >> n >> k;

        ULONG m = Pow(2,n);

        if ((k+1)%m==0)
            cout << "Case #" << i+1 << ": ON" << endl;
        else
            cout << "Case #" << i+1 << ": OFF" << endl;
    }
    return 0;
}

ULONG Pow(int base, int power){
    ULONG res = 1;
    for (int i = 0; i < power; i++){
        res*=base;
    }
    return res;
}
