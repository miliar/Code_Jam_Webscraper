#include <iostream>
#include <fstream>

using namespace std;
int main(){
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    bool change;
    char color,prevColor;
    int t,n,pos,steps,oPos,bPos,prevSteps,totalSteps;
    //cin>>t;
    fin>>t;
    for(int i=0;i<t;i++){
        //cin>>n;
        fin>>n;
        oPos=bPos=1;
        steps=prevSteps=totalSteps=0;
        for(int j=0;j<n;j++){
            //cin>>color>>pos;
            fin>>color>>pos;
            if(j==0) prevColor==color;

            if(color==prevColor)
                change=false;
            else
                change=true;

            if(color=='O'){
                steps=abs(oPos-pos)+1;
                oPos=pos;
            }else{
                steps=abs(bPos-pos)+1;
                bPos=pos;
            }
            if(change){
                if(steps<=prevSteps)
                    steps=1;
                else
                    steps-=prevSteps;
                prevSteps=0;
            }
            prevSteps+=steps;
            totalSteps+=steps;
            prevColor=color;
            //cerr<<steps<<endl;
        }
            fout<<"Case #"<<i+1<<": "<<totalSteps<<endl;
    }
    return 0;
}
