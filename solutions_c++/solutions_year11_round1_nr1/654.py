#include <iostream>

using namespace std;

int solve(unsigned long long N, unsigned long long pD, unsigned long long pG){
    if (pG==100) if (pD!=100) return 0;
    if (pG==0) if (pD!=0) return 0;
    if (N>=1) if (pD%100==0) return 1;
    if (N>=2) if (pD%50==0) return 1;
    if (N>=4) if (pD%25==0) return 1;
    if (N>=5) if (pD%20==0) return 1;
    if (N>=10) if (pD%10==0) return 1;
    if (N>=20) if (pD%5==0) return 1;
    if (N>=25) if (pD%4==0) return 1;
    if (N>=50) if (pD%2==0) return 1;
    if (N>=100) return 1;
    return 0;
}

int main()
{
    unsigned long long  T;
    unsigned long long iT;
    unsigned long long N, pD, pG;
    cin >> T;
    for(iT=1; iT<=T; iT++){
        cin >> N >> pD >> pG;
        cout << "Case #" << iT << ": ";
        if (solve(N, pD, pG)) cout << "Possible"; else cout << "Broken";
        cout << endl;
    }
    return 0;
}
