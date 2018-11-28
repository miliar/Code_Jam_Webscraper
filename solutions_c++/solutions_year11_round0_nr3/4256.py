#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;
int a[5000], n, p = 0;
        
int main(int argc, char *argv[]) {
    int test;
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    cin.rdbuf(fin.rdbuf());
    cout.rdbuf(fout.rdbuf());
    cin >> test;
    
    for(int cases = 1; cases <= test; ++cases) {
        cin >> n;
        p = 0;
        for(int i = 0; i < n; ++i) {
            cin >> a[i];
            p = p ^ a[i];
        }
        
        cout << "Case #" << cases ;
        if(p != 0) {
            cout << ": NO" << endl;
        }
        else {
            sort(a, a+n);
            int s = 0;
            for(int i = 1; i < n; ++i) {
                s += a[i];
            }
            
            cout << ": " << s << endl;
        }
    }
    
    return 0;
}
