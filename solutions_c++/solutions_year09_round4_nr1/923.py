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

int a[50], N;

int get()
{
    int res = 0;
    for(int i = 0; i < N; i++){
        if(a[i] > i + 1){
            for(int j = i + 1; j < N; j++){
                if(a[j] <= i + 1){
                    for(int k = j; k > i; k--){
                        swap(a[k], a[k - 1]);
                        res++;
                    }
                    break;
                }
            }
        }
    }
    return res;
}

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int testCnt;
    fin >> testCnt;
    for(int test = 1; test <= testCnt; test++){
        fin >> N;
        for(int i = 0; i < N; i++){
            int rightmost = 0;
            string s;
            fin >> s;
            for(int j = 0; j < N; j++){
                if(s[j] == '1'){
                    rightmost = j + 1;
                }
            }
            a[i] = rightmost;
        }
        fout << "Case #" << test << ": " << get() << endl;
    }
}
