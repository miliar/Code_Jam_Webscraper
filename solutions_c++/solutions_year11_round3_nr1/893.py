#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <map>
#include <set>
#include <fstream>
#define x first
#define y second
#define mp make_pair
using namespace std;

int main(){
     ifstream fin  ("A-large.in");
     ofstream fout ("A-large.out");
     int casos;
     fin>>casos;
     for (int cas=1;cas<=casos;cas++){
            int n,m;
            fin>>n>>m;
            vector <vector <char> > v(n, vector <char> (m));
            for (int i=0;i<n;i++) for (int j=0;j<m;j++) fin>>v[i][j];
            bool imp=false;
            for (int i=0;i<n&&!imp;i++){
                for (int j=0;j<m&&!imp;j++){
                    if (v[i][j]=='#'){
                        if (i==n-1||j==m-1) imp=true;
                        else{
                            if (v[i+1][j]=='#'&&v[i][j+1]=='#'&&v[i+1][j+1]=='#'){
                                v[i][j]='/';
                                v[i+1][j]='\\';
                                v[i][j+1]='\\';
                                v[i+1][j+1]='/';
                            }
                            else imp=true;
                        }
                    }
                }
            }
            fout<<"Case #"<<cas<<":"<<endl;
            if (imp) fout<<"Impossible"<<endl;
            else{
                for (int i=0;i<n&&!imp;i++){
                    for (int j=0;j<m&&!imp;j++) fout<<v[i][j];
                    fout<<endl;
                }
            }
        }
    }
