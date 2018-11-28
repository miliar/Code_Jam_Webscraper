#include<iostream>
#include<vector>
#include<string>
#include<fstream>

using namespace std;


ifstream fin("A_large.in");
ofstream fout("A_large.out");

typedef vector<string> VS;

using namespace std;

bool won(char c, VS &v){
    for(int i=0;i<4;++i){
        bool b=true;
        for(int j=0;j<4;++j) if(v[i][j]!=c and v[i][j]!='T') b=false;
        if(b) return true;
    }
    for(int j=0;j<4;++j){
        bool b=true;
        for(int i=0;i<4;++i) if(v[i][j]!=c and v[i][j]!='T') b=false;
        if(b) return true;
    }
    bool b=true;
    for(int i=0;i<4;++i) if(v[i][i]!=c and v[i][i]!='T') b=false;
    if(b) return true;
    b=true;
    for(int i=0;i<4;++i) if(v[i][3-i]!=c and v[i][3-i]!='T') b=false;
    return b;
}

int main(){
    int t;
    fin>>t;
    for(int test=1;test<=t;++test){
        fout<<"Case #"<<test<<":";
        VS v(4);
        for(int i=0;i<4;++i) fin>>v[i];
        if(won('O',v)) {
            fout<<" O won"<<endl;
            continue;
        }
        if(won('X',v)) {
            fout<<" X won"<<endl;
            continue;
        }
        bool b=true;
        for(int i=0;i<4;++i) for(int j=0;j<4;++j) if(v[i][j]=='.') b=false;
        if(!b) fout<<" Game has not completed"<<endl;
        else fout<<" Draw"<<endl;
    }
    system("pause");
}
