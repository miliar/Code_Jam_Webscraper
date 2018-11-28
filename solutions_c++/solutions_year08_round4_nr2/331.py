#include <iostream>
#include <vector>
#include <algorithm>

#define fir first   // x
#define sec second  // y

using namespace std;

int areapol2(vector<pair<int,int> > &pol){
    int area=0;
    for (int i=0;i<pol.size();++i){
        area+=pol[i].fir*pol[(i+1)%pol.size()].sec;
        area-=pol[i].sec*pol[(i+1)%pol.size()].fir;
    }
    return abs(area);         // positivo counterclockwise
}

int main(){
    int c;
    cin>>c;
    for (int cc=0;cc<c;++cc){
        int n,m,a;
        cin>>n>>m>>a;
        vector<pair<int,int> > tri(3);
        tri[0].fir=0;
        tri[0].sec=0;
        bool fin=0;
        for (tri[1].fir=0;tri[1].fir<=n;++tri[1].fir){
            for (tri[1].sec=0;tri[1].sec<=m;++tri[1].sec){
                for (tri[2].fir=0;tri[2].fir<=n;++tri[2].fir){
                    for (tri[2].sec=0;tri[2].sec<=m;++tri[2].sec){
                        if (areapol2(tri)==a){
                            fin=1;
                            break;
                        }
                    }
                    if (fin) break;
                }
                if (fin) break;
            }
            if (fin) break;
        }
        cout<<"Case #"<<cc+1<<":";
        if (tri[1].fir==n+1) cout<<" IMPOSSIBLE";
        else for (int i=0;i<3;++i) cout<<' '<<tri[i].fir<<' '<<tri[i].sec;
        cout<<endl;
    }
}
