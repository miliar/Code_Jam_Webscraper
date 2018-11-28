#include <map>
#include <string>
#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main (){
    ifstream fin ("B-large.in");
    ofstream fout ("B-large.out");
    int c;
    fin >>c;
    for (int o = 1; o <=c; o++){
        int n,s,p;
        fin >>n>>s>>p;
        int res = 0;
        vector <pair <int, int> > v(n);
        for (int i = 0; i< n; i++){
            int u;
            fin >>u;
            int cont = 0;
            if (u%3) cont = 1;
            v[i].first = (u/3)+cont;
            if (u <= 2) v[i].second = u;
            else v[i].second = (u+4)/3;   
            if (v[i].first >= p) res++;
            else if (v[i].second >= p and s > 0){
                 res++;
                 s--;
            }
        }
        fout <<"Case #"<<o<<": "<<res<<endl;
    }
}
