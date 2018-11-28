#include<iostream>
#include<fstream>
using namespace std;
int main(){
    ifstream readfile("TS.txt");
    ofstream outfile;
    outfile.open("OH.txt");
    int i,j,t,n,r,c,k;
    bool hash;
    readfile>>t;
    for(i=0;i<t;i++){
        readfile>>r;
        readfile>>c;
        char layout[r][c];
        for(j=0;j<r;j++){
            for(k=0;k<c;k++){
                readfile>>layout[j][k];
            }
        }
        for(j=0;j<r-1;j++){
            for(k=0;k<c-1;k++){
                if((layout[j][k]=='#')&&(layout[j][k+1]=='#')&&(layout[j+1][k]=='#')&&(layout[j+1][k+1]=='#')){
                    layout[j][k]='/';
                    layout[j][k+1]='\\';
                    layout[j+1][k]='\\';
                    layout[j+1][k+1]='/';
                }
            }
        }
        hash=false;
        outfile<<"Case #"<<i+1<<":"<<endl;
        for(j=0;j<r;j++){
            for(k=0;k<c;k++){
                if(layout[j][k]=='#'){
                    outfile<<"Impossible"<<endl;
                    hash=true;
                    break;
                }
            }
            if(hash)
                break;
        }
        if(!hash){
            for(j=0;j<r;j++){
                for(k=0;k<c;k++){
                    outfile<<layout[j][k];
                }
                outfile<<endl;
            }
        }

    }
    return 0;
}
