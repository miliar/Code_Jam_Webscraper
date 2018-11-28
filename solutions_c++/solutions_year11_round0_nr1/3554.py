#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <map>
#include <fstream>
#define x first
#define y second
#define mp make_pair
using namespace std;

int main(){
    ifstream fin  ("A-large.in");
    ofstream fout ("A-large.out");
    int cases;
    fin>>cases;
    for (int z=1;z<=cases;z++){
        vector <int> b;
        vector <int> o;
        vector <pair <char,int> > v;
        int n;
        fin>>n;
        for (int i=0;i<n;i++){
            char caux;
            int iaux;
            fin>>caux>>iaux;
            if (caux=='B') b.push_back(iaux);
            if (caux=='O') o.push_back(iaux);
            v.push_back(mp(caux,iaux));
        }
        int t=0,pb=1,po=1;
        for (;v.size();t++){
            bool done=false;
            //B
            if (b.size()){
                if (b[0]>pb) pb++;
                else{
                    if (b[0]<pb) pb--;
                    else{
                        if (v[0].x=='B'&&v[0].y==pb){
                            v.erase(v.begin());
                            b.erase(b.begin());
                            done=true;
                        }
                    }
                }
            }
            //O
            if (o.size()){
                if (o[0]>po) po++;
                else{
                    if (o[0]<po) po--;
                    else{
                        if (v[0].x=='O'&&v[0].y==po&&!done){
                            v.erase(v.begin());
                            o.erase(o.begin());
                        }
                    }
                }
            }
        }
        fout<<"Case #"<<z<<": "<<t<<endl;   
    }
}
