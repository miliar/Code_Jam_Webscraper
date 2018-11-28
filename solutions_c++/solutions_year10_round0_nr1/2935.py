#include <iostream>
#include <string>

using namespace std;

int power(int b, int e){
    if (e == 0) return 1;
    int x = 1;
    for (int i=1; i <= e; i++)
        x *= b;
    return x;
}

int problemA(){
    int ncases, ccase = 0;
    cin >> ncases;
    while (ccase++ < ncases){
        int n, k;
        cin >> n >> k;
        int x = power(2, n);
        string state = (k % x) == (x - 1)? "ON": "OFF";
        cout << "Case #" << ccase << ": " << state << endl;
    }
    return 0;
}

int main()
{
   return problemA();
}
