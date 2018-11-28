#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;
ifstream fin("jam1.in");
ofstream fout("jam1.out");
#define maxn 51
int T;
char map[maxn][maxn];
char nowmap[maxn][maxn];
int N,K;
int maxnum[maxn];
int res[maxn][maxn];
int dir[8][2]={1,0,
               0,1,
               -1,0,
               0,-1,
               1,1,
               -1,-1,
               -1,1,
               1,-1,
};
void rotate90(){
     for(int i=0;i<N;i++){
             for(int j=0;j<N;j++){
                     nowmap[i][j]=map[N-1-j][i];
             }
     }

}
void adjust(int a,int b){
     int i=a,j=b;
     a++;
     bool flag=0;
     while(a<N&&nowmap[a][b]=='.'){
                                   flag=1;
                                   a++;
     }
     if(flag){
     nowmap[a-1][b]=nowmap[i][j];
     nowmap[i][j]='.';
     }
}
void gravity(){
     for(int i=N-1;i>=0;i--){
             for(int j=0;j<N;j++){
                     if(nowmap[i][j]!='.'){
                                           adjust(i,j);
                     }
             }
     }                                          
}
int findanswer(int a,int b){
    if(res[a][b]!=0) return res[a][b];
    int maxt=0;
    for(int i=0;i<8;i++){
            int ti=a+dir[i][0];
            int tj=b+dir[i][1];
            int cnt=0;
            while((ti>=0 && ti<N && tj>=0 && tj<N) && nowmap[ti][tj]==nowmap[a][b]){
                         ti=ti+dir[i][0];
                         tj=tj+dir[i][1];
                         cnt++;
            }
            maxt=max(maxt,cnt);
    }
    return maxt+1;
    
}
void check(){
     int maxb=0,maxr=0;
     for(int i=0;i<N;i++){
             for(int j=0;j<N;j++){
                     if(nowmap[i][j]=='B'){
                                      maxb=max(findanswer(i,j),maxb);
                     }else if(nowmap[i][j]=='R'){
                                      maxr=max(findanswer(i,j),maxr);
                     }else continue;
             }
     }
     if(maxb>=K && maxr>=K) fout<<"Both"<<endl;
     else if(maxb>=K && maxr<K ) fout<<"Blue"<<endl;
     else if(maxb<K  && maxr>=K) fout<<"Red"<<endl;
     else fout<<"Neither"<<endl;
}
void init(){
     memset(res,0,sizeof(res));
     fin>>N>>K;
     for(int i=0;i<N;i++){
             for(int j=0;j<N;j++){
                     fin>>map[i][j];
             }
     }
}                    
void solve(){
     rotate90();
     gravity();
     check();
}     
int main(){
    fin>>T;
    for(int i=1;i<=T;i++){
            init();
            fout<<"Case #"<<i<<": ";
            solve();
    }
}
