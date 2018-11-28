#include<iostream>
#include<fstream>
using namespace std;

int total[1000];
int norm[1000];
int spec[1000];
int n,s,p;
int ntests;
int accept;

ifstream fin ("B-large.in");
ofstream fout ("dance.out");
int main() {
    fin >> ntests;
    for (int t = 1; t <= ntests; t++) {
        fin >> n >> s >> p;
        accept = 0;
        for (int i = 0; i < n; i++) {
            fin >> total[i];
            norm[i] = total[i] / 3;
            if (total[i] % 3 == 0) {                
                if (norm[i] != 0 && norm[i] != 10) {
                    spec[i] = norm[i] + 1;
                } else spec[i] = norm[i];
            } else if (total[i] % 3 == 1) {                
                norm[i]++;
                spec[i] = norm[i];
            } else {
                norm[i]++;
                spec[i] = norm[i]+1;
            }
            if (norm[i] >= p) accept++;
            else {
                if (spec[i] >= p && s > 0) {
                    accept++;
                    s--;
                }
            }
        }
        fout << "Case #" << t << ": " << accept << endl;
    }
}