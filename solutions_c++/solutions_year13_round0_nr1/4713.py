/*
ID: kelovef2
LANG: C++
*/

#include <fstream>
#include <cstring>
#include <cstdlib>
using namespace std;

int main()
{
    ifstream fin("A-large.in");
    int amount;
    fin>>amount;
    string s,tmp;
    int x[10], y[10];
    bool empty=false,xw,ow;
    ofstream fout("A-large.out");
    
    getline(fin,s);
    for(int i=0;i<amount;i++){
            s="";
            for(int j=0;j<10;j++){
                    x[j]=0;
                    y[j]=0;
            }

            empty=false;
            xw=false;
            ow=false;
            
            fout<<"Case #"<<i+1<<":";
            for(int j=0;j<4;j++){
                    fin>>tmp;
                     s+=tmp;
            }
            for(int j=0;j<=12;j+=4){
                    for(int k=j;k<j+4;k++){
                            if(s[k]=='.'){
                                          empty=true;
                            }
                            else if(s[k]=='T'){
                                 x[j/4]++;
                                 y[j/4]++;
                            }
                            else if(s[k]=='O'){
                                 x[j/4]++;
                            }
                            else{
                                 y[j/4]++;
                            }
                    }
            }
            for(int j=0;j<=3;j++){
                    for(int k=0;k<4;k++){
                            if(s[j+k*4]=='.'){
                                          empty=true;
                            }
                            else if(s[j+k*4]=='T'){
                                 x[j+4]++;
                                 y[j+4]++;
                            }
                            else if(s[j+k*4]=='O'){
                                 x[j+4]++;
                            }
                            else{
                                 y[j+4]++;
                            }
                    }
            }
            for(int j=0;j<16;j+=5){
                            if(s[j]=='.'){
                                          empty=true;
                            }
                            else if(s[j]=='T'){
                                 x[8]++;
                                 y[8]++;
                            }
                            else if(s[j]=='O'){
                                 x[8]++;
                            }
                            else{
                                 y[8]++;
                            }
            }
            for(int j=3;j<13;j+=3){
                            if(s[j]=='.'){
                                          empty=true;
                            }
                            else if(s[j]=='T'){
                                 x[9]++;
                                 y[9]++;
                            }
                            else if(s[j]=='O'){
                                 x[9]++;
                            }
                            else{
                                 y[9]++;
                            }
            }

            for(int j=0;j<10;j++){
                    if(x[j]==4) ow=true;
                    if(y[j]==4) xw=true;
            }
            
            if(ow && !xw){
                  fout<<" O won"<<endl;
            }
            else if(xw && !ow){
                 fout<<" X won"<<endl;
            }
            else if(xw && ow){
                 fout<<" Draw"<<endl;
            }
            else if(!xw && !ow && empty){
                 fout<<" Game has not completed"<<endl;
            }
            else{
                 fout<<" Draw"<<endl;
            }
    }
    
    
    
    fout.close();
    
    return 0;
}
