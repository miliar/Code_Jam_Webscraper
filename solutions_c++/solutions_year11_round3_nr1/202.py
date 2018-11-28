#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

#define LOOP(i,a,b) for((i)=(a);(i)<(b);++(i))
#define FOR(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define SZ(v) ((int)((v).size()))
#define PB push_back
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;

vector< vector<char> > a;
bool res;
int r,c;

void transform()
{
    FOR(i,r) FOR(j,c) {
        if(a[i][j]=='#') {
            if((i==r-1) || (j==c-1) || (a[i][j+1]!='#') || (a[i+1][j]!='#') || (a[i+1][j+1]!='#')) {
                res = false;
                return; }
            a[i][j] = '/';
            a[i][j+1] = '\\';
            a[i+1][j] = '\\';
            a[i+1][j+1] = '/'; } }
}


int main() {
    ios_base::sync_with_stdio(false);
    ofstream fout("a2.out");
    ifstream fin("a.in");

    int t;
    fin >> t;
    FOR(tt,t)
    {
        fin >> r >> c;
        a = vector< vector<char> >(r,vector<char>(c));
        FOR(i,r) FOR(j,c) {
            fin >> a[i][j]; }

        res = true;
        transform();

        fout << "Case #" << tt+1 << ":\n";
        if(res) {
            FOR(i,r) {
                FOR(j,c) fout << a[i][j];
                fout <<'\n'; }
        } else {
            fout << "Impossible\n";
        }
    }

    fout.close();
    fin.close();
    return 0;
}
