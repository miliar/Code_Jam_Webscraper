#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <map>
using namespace std;

multimap<int, int>lst;

int totalDigit(int n) {
    
    int digit =0;
    while(n>0) {
        digit++;
        n=n/10;
    }
    return digit;
}

int getChange(int num, int Dth) {

    int ntop = totalDigit(num)-Dth+1;
    int div =pow(10,ntop);


    return num%div * pow(10,Dth-1) + num/div;
}



int get(int a, int b) {


    if (a <=10 && b<=10) return 0;

    int sum = 0;
    int N;
    multimap<int, int>::iterator it;
    // assume all double digit or above
    for (int cont = max(11, a); cont <= b; cont++) {
        for (int i =2; i<=totalDigit(cont); i++) {
            N = getChange(cont, i);

            if (N <= b && N > cont) {

                for (it =  lst.equal_range(cont).first; it !=lst.equal_range(cont).second; ++it) {
                    if ((*it).second == N) break;
                }
                if (it ==lst.equal_range(cont).second)
                    sum  = sum+1;
            }
            // one to many here problem here

        }

    }

    lst.clear();
    return sum;
}


int main() {

    int cases;
    int a;
    int b;
    cin >> cases;
    for (int j = 1; j<=cases; j++) {
        cin >> a;
        cin >> b;
        cout << "Case #" << j <<": " << get(a,b)<<endl;
    }

    return 0;
}
