#include<iostream>
#include<cmath>
#include<fstream>
using namespace std;

int main(){
    ifstream iFile("B-large.in");
    ofstream oFile("DancingLargeoutput.io");
    int i=0,n=0,s=0,p=0,t[100]={0},count=0,scount=0,c=0;
    iFile>>c;
    for(int j=1;j<=c;j++){
        i=0,n=0,s=0,p=0,count=0,scount=0;
        for(i=0;i<100;i++){
            t[i]=0;
        }
        iFile>>n;
        iFile>>s;
        iFile>>p;
        for(i=0;i<n;i++){
            iFile>>t[i];
            if(ceil(t[i]/3.0)>=p){
                count++;
            }
            else if(round(t[i]/3.0)>=(p-1.0) && t[i]>0){
                if(scount<s){
                    count++;
                    scount++;
                }
            }
        }
        oFile<<"Case #"<<j<<": "<<count<<endl;
    }
}
