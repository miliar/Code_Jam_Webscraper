#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int t,r,c;
    cin >> t;
    string s;
    for(int i=1; i<=t; i++) {
        cin >> r >> c;
        vector<string> v;
        for(int j=0; j<r; j++) {
            cin >> s;
            v.push_back(s);
        }
        for(int j=0; j<r-1; j++) {
            for(int k=0; k<c-1; k++) {
                if(v[j][k]=='#' && v[j+1][k]=='#' && v[j][k+1]=='#' && v[j+1][k+1]=='#') {
                    v[j][k]='/';    v[j][k+1]='\\';
                    v[j+1][k]='\\';  v[j+1][k+1]='/';
                }
            }
        }
        bool flag=0;
        for(int j=0; j<r; j++) {
            for(int k=0; k<c; k++) {
                if(v[j][k]=='#') {
                    flag=1;
                    break;
                }
            }
            if(flag)
                break;
        }
        
        cout << "Case #" << i << ":" <<endl;
        if(flag) {
            cout << "Impossible" << endl;
            continue;
        }
        
        for(int j=0; j<r; j++) {
            cout << v[j] << endl;
        }
    }
    return 0;
}
