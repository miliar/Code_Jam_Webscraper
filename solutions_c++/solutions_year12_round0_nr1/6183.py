#include<iostream>
#include<string>
#include<fstream>
using namespace std;
main(){
char map[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
ifstream ifs;
ofstream ofs;
ifs.open("input.txt");
ofs.open("answer.txt");
int m;ifs>>m;
string s;
for(int j=0;j<m+1;j++){getline(ifs,s);
if(j!=0){
ofs<<"Case #"<<j<<": ";
int n=s.size();
for(int i=0;i<n;i++){if(s[i]!=32){s[i]=map[s[i]-97];}
ofs<<s[i];}
ofs<<endl;}
}
ifs.close();
ofs.close();
}
