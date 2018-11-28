#include<fstream>
using namespace std;

long gcd(long a,long b)
{
    if(b == 0)
         return a;
    else
         return gcd(b, a % b);
}

int main()
{
    ifstream fin("B-small-attempt0.in");
    ofstream fout("B.out");
    
    int c,n,j;
    long val[3],diff[2],g,rem;
    fin>>c;
    
    for(int i=1;i<=c;i++)
    {
         fin>>n;
         for(j=0;j<n;j++)
         {
             fin>>val[j];
         }   
         for(j=0;j<n-1;j++)
         {
             diff[j]=val[j]-val[j+1];
             if(diff[j]<0)
                 diff[j]*=-1;
         }
         if(n==3)
             g=gcd(diff[0],diff[1]);
         else
             g=diff[0];
             
         rem=val[0]%g;
         
         fout<<"Case #"<<i<<": "<<(g-rem)%g<<endl;
    }
}
