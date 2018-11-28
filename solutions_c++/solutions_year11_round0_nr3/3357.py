#include<iostream>
#include<string>
#include<cstring>
#include<fstream>
#include<vector>
#include<sstream>
using namespace std;
int main(){
    int n,m;
    ifstream readfile("TS.txt");
    readfile>>n;
    int i,j,k,l,caseval[1000],temp,results[n],index;
    for(i=0;i<n;i++){
        temp=0;
        k=0;
        readfile>>m;
        for(j=0;j<m;j++){
            readfile>>caseval[j];
            temp=temp^caseval[j];
        }
        l=caseval[0];
        index=0;
        for(j=1;j<m;j++){
            if(caseval[j]<l){
                l=caseval[j];
                index=j;
            }
        }
        if(temp!=0){
            results[i]=0;
        }
        else{
            for(j=0;j<m;j++){
                if(j!=index){
                    k=k+caseval[j];
                }
            }
            results[i]=k;
        }
    }
    ofstream outfile;
    outfile.open("OH.txt");
    for(i=0;i<n;i++){
        if(results[i]==0){
            outfile<<"Case #"<<i+1<<": "<<"NO"<<endl;
        }
        else{
            outfile<<"Case #"<<i+1<<": "<<results[i]<<endl;
        }
    }
    return 0;
}
