#include<iostream>
#include<fstream>
#include<vector>
#include<stdlib.h>
#include<sstream>
#include<string>
#include<iterator>

//#define ONLINE
using namespace std;

int nCandy=0;
int nDivided=0;
int *Number;
bool possible=false;
int maxV=0;
vector<int> Candys;
void comb2(int *P,int posOfP,int startPos){
    if(posOfP==0){
        int value=0;
        int value2=0;
        int realValue2=0;
        for(int i=0;i<nCandy;i++){
            bool same=false;
            for(int j=nDivided;j>0;j--){
                if(i==P[j]){
                    value^=Candys[P[j]];
                    same=true;
                }
            }
            if(!same){
                value2^=Candys[i];
                realValue2+=Candys[i];
            }
        }
        if(value==value2){
            possible=true;
            if(realValue2>maxV)maxV=realValue2;
        }
    }else{
        for(int i=startPos;i<nCandy;i++){
            P[posOfP]=Number[i];
            comb2(P,posOfP-1,i+1);
        }
    }
}

int main(){
    #ifndef ONLINE
    freopen("C-small-attempt0.in", "rt", stdin);
    freopen("C-small-attempt0.out","wt",stdout);
    #endif
    string line;
    getline(cin,line);
    int nCase=0;
    nCase= atoi(line.c_str());
    int count=0;
    while(count<nCase){
        Candys.clear();
        getline(cin,line);
        nCandy=atoi(line.c_str());
        Number = new int[nCandy];
        for(int i=0;i<nCandy;i++)
            Number[i]=i;
        getline(cin,line);
        istringstream iss(line);
        for(int i=0;i<nCandy;i++){
            int tmp;
            iss>>tmp;
            Candys.push_back(tmp);
        }
        int realMax=0;
        for(int i=1;i<nCandy;i++){
            nDivided=i;possible=false;maxV=0;
            int *dividedCandys=new int[nCandy];
            comb2(dividedCandys,nDivided,0);
            if(possible){
                if(maxV>realMax) realMax=maxV;
            }
        }
        if(realMax==0)cout<<"Case #"<<count+1<<": "<<"NO"<<endl;
        else cout<<"Case #"<<count+1<<": "<<realMax<<endl;
        count++;
    }
    return 0;
}

