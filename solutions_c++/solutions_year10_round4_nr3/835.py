#include<fstream>
using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");

int map[2][110][110];
int c;
int r,x1,y1,x2,y2;
int now;

void process(int p){
     for(int i=1;i<=100;i++)
          for(int j=1;j<=100;j++){
               if(map[p][i][j]==0){
                    if(map[p][i-1][j]&&map[p][i][j-1])
                         map[1-p][i][j]=1;
                    else map[1-p][i][j]=0;
               }
               if(map[p][i][j]==1){
                    if(map[p][i-1][j]==0&&map[p][i][j-1]==0)
                         map[1-p][i][j]=0;
                    else map[1-p][i][j]=1;
               }
          }
}

bool judge(){
     for(int i=1;i<=100;i++)
          for(int j=1;j<=100;j++)
               if(map[now][i][j])return false;
     return true;
}

int main(){
    fin>>c;
    for(int k=1;k<=c;k++){
         for(int i=0;i<100;i++)
                   for(int j=0;j<100;j++)
                        map[0][i][j]=map[1][i][j]=0;
         fin>>r;
         while(r){
              fin>>x1>>y1>>x2>>y2;
              for(int i=x1;i<=x2;i++)
                   for(int j=y1;j<=y2;j++)
                        map[0][i][j]=1;
              r--;
         }
         int cnt=0;
         now=0;
         while(!judge()){
              cnt++;
              process(now);
              now=1-now;
         }
         fout<<"Case #"<<k<<": "<<cnt<<endl;
    }
    return 0;
}
