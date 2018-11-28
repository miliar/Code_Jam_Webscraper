#include<iostream>
#include<fstream>
#include<string>
using namespace std;
#define MOD 10000
string W;
string s;
int dp[501][20],S;

int go(int pos,int k)
{
 if(k==19)return 1;
 if(pos==S)return 0;
 int &ret=dp[pos][k];
 if(ret==-1)
 {
  ret=go(pos+1,k);
  if(s[pos]==W[k])
  ret+=go(pos+1,k+1);
  if(ret>=MOD)ret-=MOD;
 }
 return ret;
}

string format(int k)
{
 string ret="0000";
 int i=3;
 while(k)
 {
  ret[i]='0'+k%10;
  k/=10;
  i--;        
 }    
 return ret; 
}

main()
{
 int t;
 
ifstream fin;
fin.open("C:\\data\\C-large.in");
ofstream fout;
fout.open("C:\\data\\C-large.out");
W="welcome to code jam";
fin>>t;
        char ss[502];
fin.getline(ss,1000,'\n');

for(int i=1;i<=t;++i)
{
fin.getline(ss,1000,'\n');
s=ss;
S=s.size();
memset(dp,255,sizeof(dp));
fout<<"Case #"<<i<<": "<<format(go(0,0))<<endl;
}      
fin.close();
fout.close();
}
