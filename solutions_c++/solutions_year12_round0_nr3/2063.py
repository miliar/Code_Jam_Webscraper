#include <iostream>
#include <cmath>
using namespace std;

int digits(int n){
    int res = 0;
    int cur_n = n;

    while(cur_n >= 1){
        cur_n = cur_n / 10;
        res++;
    }

    return res;
}

int rec(int n, int a, int b){
    int d = digits(n);
    int temp[d];
    int res = 0;
    for(int i = 1; i <= d - 1; i++){
        int back = n % (int) pow(10, i); // back has i digits
        if(digits(back) == i){
            int front = n / (int) pow(10, i); // front has d - i digits
            int rec_n = back * pow(10, d - i) + front;
            temp[i] = rec_n;

            bool ok = true;
            for(int j = 1; j < i; j++) if(temp[j] == rec_n) ok = false;
            if((rec_n > n) && (a <= rec_n) && (rec_n <= b) && ok) res++;
        }
    }
    return res;
}


int main(void) {
    int n;
    cin >> n;

    for(int i = 0; i < n; i++){
        int a, b;
        cin >> a;
        cin >> b;
        int res = 0;
        for(int j = a; j <= b; j++){
            res = res + rec(j, a, b);
        }
        cout << "Case #"; cout << (i + 1); cout << ": "; cout << res << endl;
    }
}
