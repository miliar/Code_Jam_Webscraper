#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

long long mcd (long long a, long long b){
    if (b == 0) return a;
    return mcd(b,a%b);
}

long long mcm(long long a, long long b){
    return (a*b)/mcd(a,b);
}

int main(){
    ofstream fout ("out.out");
    ifstream fin ("in.in");
    int t;
    fin >> t;
    for (int caso = 1; caso <= t; caso++){
        long long n, l, h;
        fin >> n >> l >> h;
        vector<long long> v (n);
        for (int i = 0; i < n; i++){
            fin >> v[i];
        }
        bool enc = false;
        long long res = 0;
        for (int i = l; i <= h and !enc; i++){
            bool enc2 = false;
            for (int j = 0; j < n and !enc2; j++){
                if (v[j]%i != 0 and i%v[j] != 0) enc2 = true;
            }
            if (!enc2){
                res = i;
                enc = true;
            }
        }
        fout << "Case #" << caso << ": ";
        if (!enc) fout << "NO" << endl;
        else fout << res << endl;
    }
}
