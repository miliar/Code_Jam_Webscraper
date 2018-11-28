#include <iostream>
#include <cstdio>

#include <vector>
#include <cstring>
#include <queue>
#include <cmath>

#define EPS 0.000001
#define INF 2000000000

#define y1 jhsdfdasdg
#define y2 sjgfkagaef

#define ABS(a) ((a)<0?(-(a)):(a))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))

using namespace std;

void sol(){
    int N, mm[1500][2], i, j;
    cin>>N;
    for(i=0;i<N;++i) cin>>mm[i][0]>>mm[i][1];
    int K=0, res=0, t;

    for(i=0;i<N-1;++i)
        if(mm[i][0]>mm[i+1][0] || (mm[i][0]==mm[i+1][0] && mm[i][1]<mm[i+1][1])){
            t=mm[i][0]; mm[i][0]=mm[i+1][0]; mm[i+1][0]=t;
            t=mm[i][1]; mm[i][1]=mm[i+1][1]; mm[i+1][1]=t;
            if(i)i-=2;
        }

    bool f=true;
    while(f){
        f=false;
        for(i=0;i<N;++i){
            if(mm[i][1]<=K){
                if(mm[i][0]<INF)K+=2;
                else K++;
                res+=1;
                f=true;
                mm[i][0]=mm[i][1]=INF;
                break;
            }
        }
        if(f) continue ;
        int max=-1;
        for(i=0;i<N;++i){
            if(mm[i][0]<=K && (max<0 || mm[i][1]>mm[max][1])) max=i;
        }
            if(max>=0){
                K++;
                res+=1;
                f=true;
                mm[max][0]=INF;

            }

    }
    for(i=0;i<N;++i) if(mm[i][0]<INF || mm[i][1]<INF) break;
    if(i>=N) cout<<res;
    else cout<<"Too Bad";
}

int main(){

    freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);

    int T;
    cin>>T;
    char str[100];
//    cin.getline(str,99);
    for(int ii=1;ii<=T;++ii){
        cout<<"Case #"<<ii<<": ";
        sol();
        cout<<endl;
    }

    return 0;
}
