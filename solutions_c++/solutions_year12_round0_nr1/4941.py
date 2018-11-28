#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
#include<math.h>
#include<fstream>
using namespace std;
#define MAX 100
int prime[MAX];
fstream oin("order.txt",ios::in);
int main() {
char orig[26];
int i=0;
while(!oin.eof()) { 
 char x;
 oin>>x; 
 orig[i]=x;
 i++;
}
int t;
cin>>t;
for(int i=0;i<t+1;i++) { 
string s;
getline(cin,s);
if(i==0) continue;
cout<<"Case #"<<i<<": "; 
for(int i=0;i<s.size();i++) {
 if(s[i]==' ')
 {cout<<" ";continue;}
 cout<<orig[s[i]-'a'];
}
cout<<endl;
}
}
