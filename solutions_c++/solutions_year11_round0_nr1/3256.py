#include<cstdio>
#include<fstream>
#include<vector>
#include<string>
using namespace std;
int t,n,num,obja,objn;
string bot;
bool w;
char b;
int posn,posa;
vector<int> pasoa;
vector<int> pason;
int c,tiempo;
int main(){
    ifstream entra("botin.txt");
    ofstream sale("botout.txt");
    entra>>t;
    for(int j=1;j<=t;j++){
        pasoa.clear();
        pason.clear();
        bot.clear();
        posn=1;
        posa=1;
        entra>>n;
        c=0;
        tiempo=0;
        obja=0;
        objn=0;
        for (int i=0;i<n;i++){
            entra>>b>>num;
            bot+=b;
            if (b=='B') pasoa.push_back(num);
            else pason.push_back(num);}
        bot+='X';
        pasoa.push_back(0);
        pason.push_back(0);
        while (bot[c]!='X'){
            w=0;
            tiempo++;
            if (posn==pason[objn]){
                if(bot[c]=='O'){
                    w=1;
                    c++;
                    objn++;}}
            else{
                if (posn>pason[objn]) posn--;
                else posn++;}
            if (posa==pasoa[obja]){
                if(bot[c]=='B' && w==0){
                    c++;
                    obja++;}}
            else{
                if (posa>pasoa[obja]) posa--;
                else posa++;}}
        sale<<"Case #"<<j<<": "<<tiempo<<endl;}}
