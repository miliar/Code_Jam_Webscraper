#include<iostream>
#include<string>
#include<fstream>
using namespace std;

char rep[] ={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
string s;

int main()
{
 ifstream fin("C:\\data\\gcj2012\\A-small-attempt0.in");
 ofstream fout("C:\\data\\gcj2012\\A-small-attempt0.txt");
 int n;
 fin>>n;
 getline(fin,s);
 for(int testcase=1;testcase<=n;++testcase)
 {
  fout<<"Case #"<<testcase<<": ";
  getline(fin,s);
  for(int i=0;i<s.length();++i)
  {
   if(s[i]==' ')fout<<" ";
   else fout<<rep[s[i]-'a'];        
  }
  fout<<endl;
 }
 fin.close();
 fout.close();
 return 0;    
}
