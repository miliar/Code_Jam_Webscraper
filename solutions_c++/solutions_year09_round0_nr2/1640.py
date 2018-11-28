#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#define  f(x,y,i) for(int i=x;i<y;i++)
#define in(n,up) find(up,up+sizeof(up)/4,(n))-&up[0]!=sizeof(up)/4 
using namespace std;

int T,H,W,a;
vector<vector<int> > B;
vector<vector<int> > marca;
int dj[4]={-1,0,0,1};
int dk[4]={0,-1,1,0};
int num=0;


int find(int x,int y){
    if(marca[x][y]>-1) return marca[x][y];
    int menor=10000,mj=H+1,mk=W+1;
    f(0,4,i){
        int J=x+dj[i]; int K=y+dk[i];
        if(J>=0 && J<H && K>=0 && K<W && menor>B[J][K]){
            menor=B[J][K]; mj=J; mk=K;
        }            
    }
//    cout<<mj<<mk<<menor<<" "<<B[x][y]<<B[mj][mk]<<endl;
    if(menor>=B[x][y]) marca[x][y]=num++;
    else marca[x][y]=find(mj,mk); 
    return marca[x][y];
}

int main()
{
    freopen("B.large.in.txt","r",stdin);
    freopen("B.large.out.txt","w",stdout);
    cin>>T;
    f(0,T,i){
        num=0;
        cin>>H>>W;
        B.clear();
        B.resize(H,vector<int>(W,-1));
        marca.clear();
        marca.resize(H,vector<int>(W,-1));
        f(0,H,j)f(0,W,k){cin>>a; B[j][k]=a;}
        printf("Case #%d:\n",i+1);
        f(0,H,j){
            f(0,W,k){
                if(k)printf(" ");
                char letra='a'+find(j,k);
                cout<<letra;
            }
            printf("\n");
        }
    }
}
