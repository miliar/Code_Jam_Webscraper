//#include <iostream>
#include <fstream>

using namespace std;

ifstream cin("1.in");
ofstream cout("1.out");

const int s1[8]={-1,-1,-1,0,0,1,1,1},s2[8]={-1,0,1,-1,1,-1,0,1};

int t;
char map[4][4],map2[4][4];

bool Check(char ch){
    for(int i=0;i!=4;i++)
        for(int j=0;j!=4;j++) map2[i][j]=(map[i][j]=='T')?ch:map[i][j];
    for(int i=0;i!=4;i++)
        for(int j=0;j!=4;j++){
            if (map2[i][j]!=ch) continue;
            for(int k=0;k!=8;k++){
                bool find=true;
                for(int l=0;l!=4;l++){
                    int x=i+l*s1[k],y=j+l*s2[k];
                    if (x<0||x>=4||y<0||y>=4){find=false;break;}
                    if (map2[x][y]!=ch) {find=false;break;}
                }
                if (find) return true;
            }
        }
    return false;
}

int main(){
    cin>>t;
    for(int q=1;q!=t+1;q++){
        cout<<"Case #"<<q<<": ";
        int num=0;
        for(int i=0;i!=4;i++)
            for(int j=0;j!=4;j++){
                cin>>map[i][j];
                num+=(map[i][j]!='.');
            }
        if (Check('O')){cout<<"O won"<<endl;continue;}
        if (Check('X')){cout<<"X won"<<endl;continue;}
        if (num!=16){cout<<"Game has not completed"<<endl;continue;}
        cout<<"Draw"<<endl;
    }
}
