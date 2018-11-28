#include<iostream>
#include<sstream>
#include<fstream>
using namespace std;
#define MAX 600
ifstream fin("C-large.in");
ofstream fout("CODEJAM.OUT");
string S;

void proccess(int t){
    int A[MAX][20];
    string str="";
    stringstream ss;
    string kq="";
    int i,j;
    for(i=0;i<MAX;i++)
        fill(A[i],A[i]+20,0);
    ss.clear();
    bool first=true;
    getline(fin,str);
    
    for(i=0;i<=str.length();i++)
         A[i][S.length()]=1;
         
    for(i=S.length()-1;i>=0;i--)
         for(j=str.length()-1;j>=0;j--){
               if(str[j]==S[i]){
                  A[j][i]=A[j+1][i]+A[j+1][i+1];
                  A[j][i]%=10000;
               }
               else
                  A[j][i]=A[j+1][i];
         }
    ss<<A[0][0];
    ss>>kq;
    while(kq.length()<4)
       kq.insert(0,"0");
    fout<<"Case #"<<t<<": "<<kq<<endl; 
}
int main(){
    int T;
    fin>>T;
    fin.ignore();
    S="welcome to code jam";
    for(int t=1;t<=T;t++)
        proccess(t);
    //system("pause");
    return 0;
}
