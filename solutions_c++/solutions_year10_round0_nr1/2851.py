#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;


void main(){
ifstream cin;
ofstream cout;
cin.open("A-large.in");
cout.open("A-large.out");
int t,n,k;
cin>>t;
for(int i=1;i<=t;i++){
//cout<<"How many Snappers?"<<endl;
cin>>n;
//cout<<"How many flips?"<<endl;
cin>>k;
int l;
cout<<"Case #"<<i<<": ";
l=pow(2.0,n)-1; // number of flips needed to turn light on for the first time
if((k+1)%(l+1)==0) cout<<"ON";
else cout<<"OFF";
cout<<endl;
}
}