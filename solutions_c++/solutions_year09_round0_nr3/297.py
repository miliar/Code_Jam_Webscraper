// eddie s.j. du
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
#include <list>
#include <sstream>
#include <map>
#include <queue>

#define ui unsigned int
#define ll long long
#define ul unsigned long
#define ull unsigned long long
#define fore(i,a,b) for(int i=(a),_b=(b);i<_b;i++)
#define rep(i,a) fore(i,0,a)
#define pb push_back
#define MP make_pair

using namespace std;

//c style
//FILE *fin = fopen("cowxor.in", "r");

//c++ style

//    ofstream fout ("gift1.out");
    ifstream fin ("C-large.in");

string s;
string a;
int res;

int MOD = 10000;

int memo [25][502];

int rec (int i, int j) {
    if (memo[i][j]!=-1) return memo[i][j];
    if (i == a.size()) return memo[i][j]=1;
    if (j == s.size()) return memo[i][j]=0;
    if (a[i] == s[j]) return memo[i][j]=(rec(i+1,j+1)%MOD + rec(i,j+1)%MOD)%MOD;
    return memo[i][j]=rec(i,j+1)%MOD;
}

int main () {
    // c style
    freopen ("C-large.out","w",stdout);
    // ie int n; fscanf (fin,"%d",&n);

    a = "welcome to code jam";

    const int SPACE = 29;

    int cas;
    fin>>cas;
    getline(fin,s); // read end of line
    rep(casNo,cas) {
     rep(i,25)rep(j,502)memo[i][j]=-1;
     getline(fin,s);
     ostringstream os;
     os << rec (0,0);
     string ress = os.str();
     while (ress.size()<4)
        ress = "0" + ress;
     cout << "Case #" << casNo+1 << ": " << ress << endl;
    }
    return 0;
}
