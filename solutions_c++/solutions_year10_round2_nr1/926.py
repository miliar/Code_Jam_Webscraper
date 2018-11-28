#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <utility>
#include <functional>

using namespace std;

#define REP(i,n) for(int (i)=0;(i)<(int)(n);(i)++)

int main(){
    int casos;
    int m,n;
    string tmp, tmp2;
    vector <string> directorios;
    cin>>casos;
    int pos;
    for (int ncaso=1; ncaso<=casos; ncaso++){
        directorios.clear();
        cin>>n>>m;
        REP(i,n){
            cin>>tmp;
            while (tmp.size()>0){
                if (find(directorios.begin(),directorios.end(),tmp)==directorios.end())
                    directorios.insert(directorios.begin(),tmp);
                pos=tmp.rfind('/');
                tmp.erase(tmp.begin()+pos,tmp.end());
            }
        }
        int cont=0;
        REP(i,m){
            cin>>tmp;
            while (tmp.size()>0){
                if (find(directorios.begin(),directorios.end(),tmp)==directorios.end()){
                    directorios.insert(directorios.begin(),tmp);
                    cont++;
                }
                pos=tmp.rfind('/');
                tmp.erase(tmp.begin()+pos,tmp.end());
            }
        }
        /*REP(i,directorios.size())
            cout<<directorios[i]<<endl;*/
        cout<<"Case #"<<ncaso<<": "<<cont<<endl;
    }
    return 0;
}
