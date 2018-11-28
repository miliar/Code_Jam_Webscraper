#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long long potega(int x, int a=10){
    long long wynik=1;
    for (int i=0;i<x;i++) wynik*=a;
    return wynik;
}

int main()
{
    int t;
    cin >> t;

    for (int i=1;i<=t;i++){
        int a,b;

        cin >> a >> b;
        int length=1;
        int btemp=b;
        while (btemp/=10) length++;
        long long wynik=0;
        for (int j=a;j<=b;j++){
           // cout << "\n\n" << j << "\n";
            for (int k=1;k<length;k++){
                int temp=(j%potega(k))*potega(length-k)+(j/potega(k));
                if (temp != j && temp >= a && temp <= b) wynik++;
            }

        }

        cout << "Case #" << i << ": " << wynik/2 << "\n";

    }

    return 0;
}
