#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;
#define REP(i,n) for(int i=0;i<n;i++)

//values found with the freely available command line calculator 'bc'
//and the commands "scale=500" and (3+sqrt(5))^1, (3+sqrt(5))^2, ... 
//(3+sqrt(5))^30
string res[40] = {
    "",
    "005",
    "027",
    "143",
    "751",
    "935",
    "607",
    "903",
    "991",
    "335",
    "047",
    "943",
    "471",
    "055",
    "447",
    "463",
    "991",
    "095",
    "607",
    "263",
    "151",
    "855",
    "527",
    "743",
    "351",
    "135",
    "407",
    "903",
    "791",
    "135",
    "647"
};

int main() {
    FILE *fin = fopen("numbers.in", "r"), *fout = fopen("numbersslow.out", "w");
    int T; fscanf(fin, "%d", &T); REP(t, T) {
        int n; fscanf(fin, "%d", &n);
        fprintf(fout, "Case #%d: %s\n", t+1, res[n].c_str());
    }
    return 0;
}
