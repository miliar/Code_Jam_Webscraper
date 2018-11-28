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

int main() {
    ios_base::sync_with_stdio(false);
    ofstream fout("a2.out");
    ifstream fin("a2.in");

    int t;
    fin >> t;
    FOR(tt,t)
    {
        int n;
        fin >> n;
        vvi match(n,vi(n,0));
        FOR(i,n) FOR(j,n) {
            char ch;
            fin >> ch;
            match[i][j] = (ch=='.' ? (0) : (ch=='1' ? 1 : -1)); }

        vi score(n,0);
        vi matches(n,0);
        FOR(i,n) FOR(j,n) {
            if(match[i][j] != 0) {
                ++matches[i];
                if(match[i][j] == 1) {
                    ++score[i]; } } }

        vector<double> wp(n,0.0);
        FOR(i,n) wp[i] = ((double)score[i]) / ((double)matches[i]);

        vector<double> owp(n,0.0);
        FOR(i,n) {
            FOR(j,n) if(match[i][j] != 0) owp[i] += ((double)(score[j] - (match[j][i]==1 ? 1 : 0))) / ((double)(matches[j]-1));
            owp[i] /= (double)matches[i]; }

        vector<double> oowp(n,0.0);
        FOR(i,n) {
            FOR(j,n) if(match[i][j] != 0) oowp[i] += owp[j];
            oowp[i] /= matches[i]; }

        fout << "Case #" << tt+1 << ":\n";
        FOR(i,n) {
            fout.precision(12);
            fout << ((0.25*wp[i]) + (0.5*owp[i]) + (0.25*oowp[i])) << '\n'; }
    }

    fout.close();
    fin.close();
    return 0;
}
