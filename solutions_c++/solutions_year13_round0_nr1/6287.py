#include<iostream>
#include<fstream>
using namespace std;
fstream fcin ("input.txt");
fstream fcout ("output.txt");
int has[256];
int main(){
    int m,n,q;
    string str[4]={": Draw\n",": X won\n",": O won\n",": Game has not completed\n"},mapa[4];
    fcin >> n;
    m=n;
    has[(int)'.']=0;
    has[(int)'X']=1;
    has[(int)'O']=2;
    has[(int)'T']=3;
    while(n--){
        for(int i=0;i<4;i++) {
            fcin >> mapa[i];
        }
        for(int i=0;i<4;i++){
            q=3;
            for(int j=0;j<4;j++){
                q&=has[(int)mapa[i][j]];
            }
            if(q) {
                fcout << "Case #"<< m-n << str[q];
                break;
            }
        }
        if(q) continue;
        for(int i=0;i<4;i++){
            q=3;
            for(int j=0;j<4;j++){
                q&=has[(int)mapa[j][i]];
            }
            if(q) {
                fcout << "Case #"<< m-n << str[q];
                break;
            }
        }
        if(q) continue;
        q=3;
        for(int i=0;i<4;i++){
            q&=has[(int)mapa[i][i]];
        }
        if(q){
            fcout << "Case #"<< m-n << str[q];
            continue;
        }
        q=3;
        for(int i=0;i<4;i++){
            q&=has[(int)mapa[i][3-i]];
        }
        if(q){
            fcout << "Case #"<< m-n << str[q];
            continue;
        }
        q=0;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(mapa[i][j]=='.') q=3;
            }
            if(q==3) break;
        }
        fcout << "Case #"<< m-n << str[q];
    }
}
