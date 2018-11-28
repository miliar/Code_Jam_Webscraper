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
   ifstream fin  ("C-small.in");
   ofstream fout ("C-small.out");
   int casos;
   fin>>casos;
   for (int cas=1;cas<=casos;cas++){
        int n,l,h;
        fin>>n>>l>>h;
        vector <int> v(n);
        for (int i=0;i<n;i++) fin>>v[i];
        bool corr=false;
        int res;
        for (int i=l;i<=h;i++){
            bool ok=true;
            for (int j=0;j<n&&ok;j++){
                if (v[j]>i&&v[j]%i) ok=false;
                if (v[j]<=i&&i%v[j]) ok=false;
            }
            if (ok){
                corr=true;
                res=i;
                break;
            }
        }
        fout<<"Case #"<<cas<<": ";
        if (!corr) fout<<"NO"<<endl;
        else fout<<res<<endl;
    }
}
