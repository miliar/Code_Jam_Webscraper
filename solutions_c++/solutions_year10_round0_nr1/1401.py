#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream cin("in.txt");
    ofstream cout("out.txt");
    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cout << "Case #" << i+1 << ": ";
    int n,k;
    cin >> n >> k;
    //cout << (1 << (n-1));
            bool on = true;
            for (int m = 0; m <= n-1; m++) {
                if (!((1 << m) & k)) {
                    on = false;
                    break;
                }
            }
            if (on) {
                cout << "ON\n";
            } else {
                cout << "OFF\n";
            }
        }
}