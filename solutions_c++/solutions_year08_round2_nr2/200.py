#include<iostream>
#include<fstream>
#include<vector>
#include<set>
using namespace std;
typedef long long ll;
#define PB push_back
vector<int> pr;
bool prime[1005];

bool share(int a,int b,int p)
{
    vector<int> pa,pb;
    for(int i=2;i<=a;++i)
    {
        if(a%i==0)
            {
                if(i>=p)
                pa.PB(i);
                while(a%i==0)a/=i;  
            }    
    }    
    for(int i=2;i<=b;++i)
    {
        if(b%i==0)
            {
                if(i>=p)
                {
                if(find(pa.begin(),pa.end(),i)!=pa.end())return true;
                
                }
                while(b%i==0)b/=i;  
            }    
    }    
    return false;
}


int main()
{
ifstream fin;
fin.open("C:\\data\\B-small-attempt0.in");
ofstream fout;
fout.open("C:\\data\\bss.txt");
memset(prime,true,sizeof(prime));
prime[0]=prime[1]=false;
for(int i=2;i<1005;++i)if(prime[i])
{ pr.PB(i);
    for(int j=i*2;j<1005;j+=i)
        prime[j]=false;
    }
int t;
fin>>t;
int a,b,p;
int s[1005];
for(int cas=1;cas<=t;++cas)
{
  fin>>a>>b>>p;
  for(int i=a;i<=b;++i)s[i]=i;
  
  for(int i=a;i<=b;++i)
    for(int j=i+1;j<=b;++j)if(s[i]!=s[j])
        if(share(i,j,p))
            {
                int ta=s[i];
                int tb=s[j];
                int t=ta<?tb;
                for(int k=a;k<=b;++k)
                if(s[k]==ta || s[k]==tb)
                s[k]=t;    
            }
set<int> f;
  for(int i=a;i<=b;++i)
  f.insert(s[i]);
  fout<<"Case #"<<cas<<": "<<f.size()<<endl;
} 
fin.close();
fout.close();
return 0;    
}
