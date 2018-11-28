#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cmath>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <iomanip>
using namespace std;

#define SZ size()
#define PB push_back
#define B begin()
#define E end()
#define SORT(a) sort((a).B, (a).E)
#define REV(a) reverse((a).B, (a).E)
#define UNQ(a) (a).resize(unique((a).B, (a).E) - (a).B)
#define SUM(a) accumulate((a).B, (a).E, 0)
#define FOR(i, a, b) for(int i = (a); i < (b); i++)
#define TR(i, a) for(typeof(a.B) i = a.B; i != a.E; i++)

string N;
int a[30], len;

void get()
{
    N = "0" + N;
    len = N.SZ;
    FOR(i, 0, len){
        a[i] = N[i] - '0';
    }
    next_permutation(a, a + len);
    N = "";
    if(a[0]){
        N += a[0] + '0';
    }
    FOR(i, 1, len){
        N += a[i] + '0';
    }
}

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    int testCnt;
    fin >> testCnt;
    for(int test = 1; test <= testCnt; test++){
        fin >> N;
        get();
        fout << "Case #" << test << ": " << N << endl;
    }
}
