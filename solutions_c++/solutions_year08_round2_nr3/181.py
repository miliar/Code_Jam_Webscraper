#include<iostream>
#include<fstream>
#include<vector>
#include<set>
using namespace std;
typedef long long ll;
#define PB push_back
#define SZ(a) ((int)(a).size())
int main()
{
ifstream fin;
fin.open("C:\\data\\C-small-attempt0.in");
ofstream fout;
fout.open("C:\\data\\cs.txt");
int t;
fin>>t;
int k,n;
int s[5005];
for(int cas=1;cas<=t;++cas)
{
  fin>>k;
  vector<int> left;
  for(int i=0;i<k;++i)
  left.PB(i);
  
  int cur=0;
  for(int i=1;i<=k;++i)
  {
        s[left[cur]]=i;
        left.erase(left.begin()+cur);
        if(i<k)
        cur=(cur+i)%SZ(left);    
  }
  
  fin>>n;
  fout<<"Case #"<<cas<<": ";
  int tes;
  for(int i=0;i<n;++i)
  {
   fin>>tes;     
   fout<<s[tes-1]<<" ";
  }
  fout<<endl;
} 
fin.close();
fout.close();
return 0;    
}
