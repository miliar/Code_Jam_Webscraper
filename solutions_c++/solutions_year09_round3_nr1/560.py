#include <iostream>
using namespace std;
int numb[128], used[128];
void solve(int q){
    memset(numb, 0, sizeof(numb));
    memset(used, 0, sizeof(used));
    string a;
    cin >> a;
    numb[1] = 1;
    for (int  i = 1; i < a.size(); ++i )
        if ( a[i] == a[0] ) { a[i] = 1; used[i] = 1; }
    a[0] = 1;
    used[0] = 1;
    long long br = 0;
    for ( int i = 1; i < a.size(); ++i )
        if ( !used[i] ){
            for ( int j = i + 1; j < a.size(); ++j )
                if ( a[i] == a[j] && !used[j] ) {a[j] = br;used[j] = 1;}
            a[i] = br;
            ++br;used[i] = 1;
            if ( numb[br] ) ++br;
        }
    if ( br == 0 ) br = 2;
    reverse(a.begin(), a.end());
    long long p = 1;
    long long rez = 0;
    for ( int i = 0; i < a.size(); ++i ){
        rez += (p * (long long)a[i]);
        p *= br;
    }
    cout << "Case #" << q << ": " << rez << endl;
}
int main(){
    int t;
    cin >> t;
    for ( int i = 1; i <= t; ++i ){
        solve(i);
    }
}
