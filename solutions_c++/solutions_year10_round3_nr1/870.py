#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#define x first
#define y second
using namespace std;

int main(){
    ifstream fin ("A-large.in");
    ofstream fout ("A-large.out");
    int cases;
    fin>>cases;
    for (int z=1;z<=cases;z++){
        int n;
        fin>>n;
        vector <pair <int,int> > v(n);
        for (int i=0;i<n;i++) fin>>v[i].x>>v[i].y;
        int res=0;
        for (int i=0;i<n;i++){
            for (int j=i+1;j<n;j++){
                if (v[i].x>v[j].x&&v[i].y<v[j].y) res++;
                if (v[i].x<v[j].x&&v[i].y>v[j].y) res++;
            }
        }
        fout<<"Case #"<<z<<": "<<res<<endl;
    }
}
