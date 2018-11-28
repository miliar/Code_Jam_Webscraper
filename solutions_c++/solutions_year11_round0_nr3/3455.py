#include<iostream>
#include<fstream>
using namespace std;
int s[30];
int main(){
    ifstream cin("a.in");
    ofstream cout("a.out");
    int cas;
    cin>>cas;
    int k=1;
    while(cas--){
           memset(s,0,sizeof(s));
           unsigned n;
           cin>>n;
           unsigned sum=0;
           unsigned min=0xffffffff,m;
           for(int i=0;i<n;i++){
                   cin>>m;
                   sum+=m;
                   if(m<min) min=m;
                   for(int i=0;m;m>>=1,i++)
                        if(m&1)
                          s[i]++;
           }      
           int flag=true;
           for(int i=0;i<30;i++)
                   if(s[i]%2)
                       flag=false;
           cout<<"Case #"<<k++<<": ";
           if(flag)  cout<<sum-min<<endl;
           else      cout<<"NO"<<endl;
    }    
}
