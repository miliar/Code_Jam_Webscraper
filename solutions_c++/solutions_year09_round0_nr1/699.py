#include<iostream>
#include<fstream>
#include<string>
#include<vector>
using namespace std;
int Q[16];
int L,D,N;
int W[5001][16];

int go(int k)
{
 for(int i=0;i<L;++i)
 {
  if((Q[i]&W[k][i])==0)
  return 0;
 }     
 return 1;
}

main()
{
ifstream fin;
fin.open("C:\\data\\A-large.in");
ofstream fout;
fout.open("C:\\data\\A-large.out");

fin>>L>>D>>N;
for(int i=0;i<D;++i)
{
        string s;
 fin>>s;
 for(int j=0;j<s.size();++j)
         W[i][j]=1<<(s[j]-'a');
}
string s;
for(int i=1;i<=N;++i)
{
        fout<<"Case #"<<i<<": ";
 fin>>s;
 int in=0,k=0;
 memset(Q,0,sizeof(Q));
 for(int j=0;j<s.size();++j)if(s[j]=='(')
 {
         in=1;
 }
 else if(s[j]==')')
 {
       in=0;
       k++;
 }
 else 
 {
  Q[k]|=1<<(s[j]-'a');
  if(!in)k++;
 }
 int ret=0;
 for(int j=0;j<D;++j)ret+=go(j);
 fout<<ret<<endl;
}
fin.close();
fout.close();      
}
