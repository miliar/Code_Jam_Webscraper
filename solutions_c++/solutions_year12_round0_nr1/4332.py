#include <iostream>
#include <fstream>
#include <String>
using namespace std;
int main(){
int m=0,i,l,k=0;
string s;
char a[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
ifstream fin("A-small-attempt1.in",ios::in);
ofstream fout("A-small-attempt1.out",ios::out);
fin>>m;fin.ignore();
while(m){
 getline(fin,s);
 l=s.length();
 fout<<"Case #"<<++k<<": ";
 for(i=0;i<=l;i++)
 {if(s[i]==' ')fout<<' ';
 else if(('a'<=s[i])&&(s[i]<='z'))fout<<a[s[i]-97];}
 fout<<endl;
 m--;
 }
fin.close();
fout.close();
return 0;
}
