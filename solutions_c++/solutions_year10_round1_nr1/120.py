#include<iostream>
using namespace std;

int T;
int N,K;
char in1[60][60];
char in2[60][60];


int main(){
    int i,j,k;
    int di,dj;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin>>T;
    int cas = 0;
    while(T--){
        cin>>N>>K;
        for(i=0;i<N;++i) cin>>in1[i];
        for(i=0;i<N;++i) for(j=0;j<N;++j) in2[i][j] = '.';
        for(i=N-1;i>=0;--i){
            int cur = 0;
            for(j=N-1;j>=0;--j){
                if(in1[i][j]!='.'){
                    in2[cur][N-1-i] = in1[i][j];
                    ++cur;
                }
            }
        }
        bool blue = false;
        bool red = false;
        for(i=0;i<N;++i){
            for(j=0;j<N;++j){
                if(in2[i][j]=='.') continue;
                for(di=-1;di<2;++di) for(dj=-1;dj<2;++dj){
                    if(di==0&&dj==0) continue;
                    for(k=0;k<K;++k){
                        int ti = i+di*k;
                        int tj = j+dj*k;
                        if(ti<0||ti>=N) break;
                        if(tj<0||tj>=N) break;
                        if(in2[ti][tj]!=in2[i][j]) break;
                    }
                    if(k==K){
                        if(in2[i][j]=='B') blue= true;
                        else red = true;
                    }
                }    
            }
        }
        ++cas;
        cout<<"Case #"<<cas<<": ";
        int t1 = blue*2+red;
        switch(t1){
            case 0:
                cout<<"Neither\n";
                break;
            case 1:
                cout<<"Red\n";
                break;
            case 2:
                cout<<"Blue\n";
                break;
            case 3:
                cout<<"Both\n";
                break;
  
        }
    }
}
