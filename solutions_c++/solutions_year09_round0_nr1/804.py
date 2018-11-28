#include <iostream>
#include <vector>
using namespace std;
int l, d, N;
string dic[10000];
vector <string> tdic;
void scan1(){
    string sss;
    cin >> l >> d >> N;
    for ( int i = 0; i < d; ++i )
        cin >> dic[i];
    getline(cin, sss);
}
void solve(int q){
    int ind = 0;
    string let[32], s;
    tdic.erase(tdic.begin(), tdic.end());
    getline(cin, s);
    s  += '(';
    int K = 0;
    for ( int i = 0; i < s.size(); ++i ){
        if ( s[i] == '(' || !K) { ++ind; if ( s[i] == '(' )K = 1; }
        if ( s[i] >= 'a' && s[i] <= 'z' )let[ind] += s[i];
            else if ( s[i] == ')' ) { K = 0; }
    }
    --ind;
    if ( ind != l ) { cout << "Case #" << q << ": " << 0 << endl; return; }
    for ( int i = 0; i < d; ++i )
        tdic.push_back(dic[i]);
    for ( int i = 1; i <= l; ++i )  {
        for ( int j = 0; j < tdic.size(); ++j ){
            int lamp = 0;
            for  ( int k = 0; k < let[i].size(); ++k )
                if ( tdic[j][i - 1] == let[i][k] ) lamp = 1;
            if ( !lamp ) { tdic.erase(tdic.begin() + j, tdic.begin() + j + 1); --j; }
    } 
    }
    cout << "Case #" << q << ": " << tdic.size() << endl;
}
int main(){
    scan1();
    for ( int i = 1; i <= N; ++i )
        solve(i);
}
