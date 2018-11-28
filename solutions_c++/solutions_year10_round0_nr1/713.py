#include <iostream>
using namespace std;

void solve (int t,int n, int k) {
    // solve for
    int snap[n];
    for (int i = 0; i<n ;i++) {
        snap[i]=0;
    }
    string onof = "OFF";
    // snap k times;
/*    for (int i = 0; i<k ;i++) {
        // cauta n positie
        bool on =false;
        int pos =n;
        //verifica daca toate-s aprinse

        for (int m = 0; m<n;m++) {
            if (snap[m] == 0) {
                pos = m;
                snap[m] = 1;
                break;
            }
        }

        for (int m = 0; m<pos ; m++) {
            snap[m] = 0;
        }


        }
    for (int i = 0; i<n;i++) {
        if (snap[i] == 0) {
            onof = "OFF";
            break;
        }
    }
  */
    ///calculate 2 to n
    long result2ton =2;
    for (int i =1; i<n; i++) {
        result2ton *=2;
    }
    if (((k+1) % result2ton) ==0)
        onof="ON";
            
    cout << "Case #" <<++t <<": " << onof <<endl;
}
int main() {
    
    // read cases
    int t;
    cin >> t;

    // read each case

    for (int i = 0; i< t; i++) {
        // read
        int n,k;
        cin >> n;
        cin >>k;
        solve (i, n ,k);
    }
}
// to compile : g++ namefile
// to run : ./a.out < text.in >text.out


