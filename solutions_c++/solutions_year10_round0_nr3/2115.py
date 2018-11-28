#include<fstream>
using namespace std;

struct abc
{
    unsigned long prof;
    long nxt;
    
    abc()
    {
         prof=0;
         nxt=-1;
    }
};

int main()
{
    ifstream fin("C-small-attempt0.in");
    ofstream fout("C.out");
    
    int t;
    int n,j,l;
    unsigned long r,k,sum;
    int gn;
    long g[1000];
    
    fin>>t;
    for(int i=1;i<=t;i++)
    {
         fin>>r>>k>>n;
         abc grp[1000];
            
         for(j=0;j<n;j++)
         {
              fin>>g[j];
         }
         
         sum=g[0];
         l=1%n;
         for(gn=0;gn<n;l=((l+1)%n))
         {
              if(((sum+g[l])<=k) && l!=gn)
                   sum+=g[l];
              else
              {
                  grp[gn].prof=sum;
                  grp[gn].nxt=l;
                  sum-=g[gn];
                  gn++;
                  if((sum+g[l])<=k)
                      sum+=g[l];
                  else if(l==0)
                      l=n-1;
                  else
                      l--;
              }    
         }
         l=0;
         sum=0;
         for(j=0;j<r;j++)
         {
              sum+=grp[l].prof;
              l=grp[l].nxt;
         }
         fout<<"Case #"<<i<<": "<<sum<<endl;
    }
}
