#include <iostream>
#include <vector>
using namespace std;

int sumdigit(int input) {
    int n=0;
    while (input) {
        n++;
        input = input/10;
    }
    return n;
}

int myPow(int x, int p) {
    if (p == 0) return 1;
    if (p == 1) return x;
    return x * myPow(x, p-1);
}

vector<int> muter(int input) {
    vector<int> result;
    int temp,i,digit;
    if (input/100 == 0) {
        temp = (input%10)*10 + input/10;
        result.push_back(temp);
    } else {
/*        digit = sumdigit(input);
        for (i=1; i<digit; i++) {
            temp = (input%myPow(10,digit-i))*myPow(10,i) + input/myPow(10,digit-i);
            result.push_back(temp);
        }*/
        temp = (input%10)*100 + input/10;
        result.push_back(temp);
        temp = (input%100)*10 + input/100;
        result.push_back(temp);
    }
    return result;
}

int main() {
    int i,T,A,B,count,j,k,cek;
    vector<int> tes;
    cin >> T;
    for (i=1; i<=T; i++) {
        count = 0;
        tes.clear();
        cin >> A >> B;
        if (((A/10 == 0) && (B/10 == 0)) || (A == B))
            count = 0;
        else {
            for (j=A; j<=B; j++) {
                tes = muter(j);
                for (k=0; k<2; k++) {
                    cek = tes.back();
                    if ((A<=cek) && (j<cek) && (cek<=B))
                        count++;
                    tes.pop_back();
                }
            }
        }
        cout << "Case #" << i << ": " << count << endl;
    }
}
