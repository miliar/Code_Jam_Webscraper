#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <stack>
#include <utility>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string.h>
#include <iomanip>
#include <stdio.h>
#include <fstream>

using namespace std;

typedef long long ll;

#define mp make_pair
#define pb push_back
#define srt(x) sort((x).begin(), (x).end())
#define fil(x,c) fill((x).begin(), (x).end(), c) //memset(&a, c, sizeof(a))

template<typename T> inline int siz(const T& c) { return (int)c.size(); }

ifstream fin("input.txt");
ofstream fout("output.txt");

int main() {
    int N;
    char c;
    fin >>N;
    for (int test = 1; test <= N; test++) {
        int n;
        
        vector<vector<char> > M;
        vector<double> WP, OWP, OOWP;
        
        fin >>n;
        for (int i=0; i < n; i++) {
            vector<char> m;
            double d = 0;
            int u = 0;
            for (int j=0; j < n; j++) {
                fin >>c;
                m.push_back(c);
                if (c == '1') {
                    d ++;
                    u ++;
                } else if (c == '0') {
                    u ++;
                }
                
            }
            WP.push_back(d / u);
            M.push_back(m);
        }
        
        for (int i=0; i < n ;i ++) {
            double d = 0;
            int u= 0;
            
            //cout <<"FOR: " <<i  <<endl;
            
            for (int j=0; j < n; j++) if (j != i && M[i][j] != '.') {
                
                //cout <<"WITH: " <<j <<endl;
                
                double wp = 0;
                int uu = 0;
                for (int t = 0 ;t <n ;t++) if (t != i) {
                    if (M[j][t] == '1') {
                        wp++;
                        uu++;
                    } else if(M[j][t] == '0') {
                        uu++;
                    }
                }
                wp /= uu;
                
                //cout <<"WP: " <<wp <<endl;
                
                d += wp;
                u++;
            }
            OWP.push_back(d / u);
        }
        
        for (int i=0; i < n; i++) {
            double d = 0;
            int u= 0;
            for (int j=0; j < n; j++) if (j != i && M[i][j] != '.') {
                d += OWP[j];
                u++;
            }
            OOWP.push_back(d / u);
        }
        
        /*for (int i=0; i <n; i++) {
            fout <<OOWP[i] <<" ";
        }*/
        
        fout <<"Case #" <<test <<":" <<endl;
        for (int i =0; i < n; i++) {
            fout <<setprecision(12) <<(0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
            
            if (i != n-1) fout<<endl;
        }
        
        fout <<endl;
    }
}