#include<iostream>
#include<fstream>
using namespace std;
int main(){
    ifstream readfile("TS.txt");
    ofstream outfile;
    outfile.open("OH.txt");
    int t,n,l,h,i,j,k;
    readfile>>t;
    for(i=0;i<t;i++){
        readfile>>n;
        int freq[n];
        readfile>>l;
        readfile>>h;
        for(j=0;j<n;j++){
            readfile>>freq[j];
        }
        outfile<<"Case #"<<i+1<<": ";
        for(k=l;k<=h;k++){
            for(j=0;j<n;j++){
                if((k%freq[j]==0)||(freq[j]%k==0)){
                    continue;
                }
                else{
                    break;
                }
            }
            if(j==n){
                outfile<<k<<endl;
                break;
            }
        }
        if(k>h){
            outfile<<"NO"<<endl;
        }
    }
}
