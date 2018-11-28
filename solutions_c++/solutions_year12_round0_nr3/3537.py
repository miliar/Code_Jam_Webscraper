#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <string.h>
#include <stdlib.h>
#include <sstream>
#include <set>
#include <map>
#include <algorithm>
#include <iomanip>
#include <math.h>

using namespace std;


//ifstream fin("sample.txt");
//#define cin fin

int nd;

int rnd(double x){
    return floor(x + 0.5);
}

int d(int num, int dtm){
    int nd = log10(num) + 1;
    int p = round(pow(10, dtm));
    int q = round(pow(10, nd - dtm));
    return num%p*q + num/p;
}

void run(){
    int a, b;
    cin >> a >> b;
    nd = log10(a) + 1;
    int ans = 0;
    int temp;
    int prev = -1;
    for(int i = a; i <= b; i++){
        for(int j = 1; j < nd; j++){
            temp = d(i, j);
            if(temp > i && temp <= b && prev != temp){
                prev = temp;
                //cout << i << ", " << temp << ", " << j << endl;
                ans++;
            }
        }
    }

    cout << ans;

}


int main(){
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        cout << "Case #" << i+1 << ": ";
        run();
        cout << endl;
    }
    return 0;
}

