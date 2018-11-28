#include <iostream>
#include <fstream>
using namespace std;
struct group{
    unsigned short first;
    unsigned short num;
    unsigned short *groups;
};
int main(){
ifstream fin ("A-small.in");
ofstream fout("A-small.out");
unsigned short cases=0;
unsigned short psn=0;
unsigned short turn=0;
fin>>cases;
unsigned int euros[cases];
unsigned short rides[cases];
unsigned short cap[cases];
group gps[cases];
memset(&gps,0,sizeof(gps));
memset(&rides,0,sizeof(rides));
memset(&euros,0,sizeof(euros));
for(unsigned short i=0;i<cases;i++){
    fin>>rides[i] >>cap[i] >>gps[i].num;
    gps[i].groups=new (nothrow) unsigned short [gps[i].num];
    if (gps[i].groups==0){
        cout<<"ERROR\n";
    }
    else{
        for(unsigned short n=0;n<gps[i].num;n++){
            fin>> gps[i].groups[n];
        }
    }
}

for(unsigned short i=0;i<cases;i++){
    for(unsigned short n=0;n<rides[i];n++){
            gps[i].first=turn;
            while(cap[i]>=(psn+gps[i].groups[turn])){
                psn+=gps[i].groups[turn];
                if (turn+1==gps[i].num){
                    turn=0;
                }
                else {
                    turn++;
                }
                if(turn==gps[i].first){
                    break;
                }
            }
    euros[i]+=psn;  
    psn=0;
    }   
    turn=0;
    fout<<"Case #"<<i+1<<": "<<euros[i]<<endl;
}
}
