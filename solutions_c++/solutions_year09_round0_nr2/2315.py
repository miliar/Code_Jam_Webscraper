#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <map>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef map<int,char> MIC;


class UF{
    private:
        vector<int> p, rank;
    public:
        void init(int n) {
            rank.assign(n, 0);
            p.resize(n);
            for (int i=0; i<n; i++) p[i] = i;
        }
        int find(int x) {
            if (x != p[x]) return p[x] = find(p[x]);
            return x;
        }
        void unite(int x, int y) {
            x = find(x);
            y = find(y);
            if (rank[x] > rank[y]) p[y] = x;
            else {
                p[x] = y;
                if (rank[x] == rank[y]) rank[y]++;
            }
        }
};

PII dir(int x,int y,const VVI &alt){
    VPII v;
    if(y>0) v.push_back(PII(alt[y-1][x],0)); // north
    if(y<(int)alt.size()-1) v.push_back(PII(alt[y+1][x],3)); // south
    if(x>0) v.push_back(PII(alt[y][x-1],1)); // west
    if(x<(int)alt[0].size()-1) v.push_back(PII(alt[y][x+1],2)); // east
    sort(v.begin(),v.end());
    if(v.size()==0) return PII(1<<16,-1);
    return v[0];
}

int calc(int x,int y,int h,int w,int dir){
    if(dir==-1) return y*w+x;
    if(dir==0) return y*w+x-w;
    if(dir==1) return x-1+y*w;
    if(dir==2) return x+1+y*w;
    if(dir==3) return y*w+x+w;
    return -1;
}

void kase(){
    UF uf;
    int h,w;
    cin >> h >> w;
    uf.init(h*w);
//    int alt[h][w];
    VVI alt(h);
    for(int i=0;i<h;i++)
        for(int j=0;j<w;j++){
            int in;
            cin >> in;
            alt[i].push_back(in);
        }
    
    for(int i=0;i<h;i++){
        for(int j=0;j<w;j++){
            int mh = alt[i][j];
            PII p = dir(j,i,alt);
            if(p.first<mh){
                int mypos = calc(j,i,h,w,-1);
                int to = calc(j,i,h,w,p.second);
                fprintf(stderr,"unite(%d, %d) (%d, %d)@(%d,%d) d: %d\n",
                    mypos,to,mh,p.first,j,i,p.second);
                uf.unite(mypos,to);
            }
        }
    }
    MIC mymap;
    char c = 'a';
    for(int i=0;i<h;i++){
        for(int j=0;j<w;j++){
            int pos = calc(j,i,h,w,-1);
            int set = uf.find(pos);
            if(mymap.find(set)==mymap.end()){
                mymap[set] = c;
                c++;
            }
            printf("%c%c",mymap[set],j<w-1?' ':'\n');
        }
    }
}


int main(){

    int N;
    cin >> N;
    for(int i=1;i<=N;i++) {
        printf("Case #%d:\n",i);
        kase();
    }
    return 0;
}
