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

    int t,n;
    fin >> t;
    FOR(tt,t) {

        fin >> n;
        vector<bool> orange(n);
        vector<int> button(n);
        FOR(i,n) {
            char ch;
            fin >> ch;
            orange[i] = (ch=='O');
            fin >> button[i]; }

        int nextO=0, nextB=0, atO=1, atB=1,steps=0;
        while((nextO<n) && (!orange[nextO])) ++nextO;
        while((nextB<n) && (orange[nextB])) ++nextB;
        FOR(i,n) {
            if(nextO<nextB) {
                int cur = abs(atO - button[nextO])+1;
                atO = button[nextO];
                ++nextO;
                while((nextO<n) && (!orange[nextO])) ++nextO;
                if(nextB<n) if(button[nextB] > atB) {
                    atB += min(cur,button[nextB] - atB); }
                else if(button[nextB] < atB) {
                    atB -= min(cur,atB - button[nextB]); }
                steps += cur; }
            else {
                int cur = abs(atB - button[nextB])+1;
                atB = button[nextB];
                ++nextB;
                while((nextB<n) && (orange[nextB])) ++nextB;
                if(nextO<n) if(button[nextO] > atO) {
                    atO += min(cur,button[nextO] - atO); }
                else if(button[nextO] < atO) {
                    atO -= min(cur,atO - button[nextO]); }
                steps += cur; } }

        fout << "Case #" << tt+1 << ": " << steps << '\n';
    }
    fout.close();
    fin.close();
    return 0;
}
