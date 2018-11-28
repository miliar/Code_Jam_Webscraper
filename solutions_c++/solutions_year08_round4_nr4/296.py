
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;
vector<int> pr;
string str;
int k, cmin;
int calc(){
    string tstr;
    for(int i = 0; i < str.size(); i += k){
        for(int j = 0; j < k; ++ j)
            tstr += str[i + pr[j]];
    }
    int ret = 1;
    for(int i = 1; i < str.size(); ++ i)
        if (tstr[i] != tstr[i - 1]) ++ ret;
    return ret;
}
int main(){
    ifstream cin("D-small-attempt0.in");
    ofstream cout("out.txt");
    int ncase;
    cin >> ncase;
    for(int tcase = 1; tcase <= ncase; ++ tcase){
        cin >> k >> str;
        pr.clear();
        for(int i = 0; i < k; ++ i) pr.push_back(i);
        cmin = str.size();
        do{
            cmin <?= calc();
        }while ( next_permutation(pr.begin(), pr.end()));
        cout << "Case #" << tcase << ": " << cmin << endl;
    }
    return 0;
}
