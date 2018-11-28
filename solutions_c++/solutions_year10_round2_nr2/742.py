#include<fstream>
using namespace std;

int main()
{
    ifstream fin("B.in");
    ofstream fout("B.out");
    int c,n,k,b,t,j,swaps,count,num;
    int x[50],v[50];
    bool f[50];
    fin>>c;
    
    for(int i=1;i<=c;i++)
    {
        fin>>n>>k>>b>>t;
        for(j=0;j<n;j++)
        {
            fin>>x[j];
        }
        for(j=0;j<n;j++)
        {
            fin>>v[j];
            if(b<=(x[j]+(v[j]*t)))
                f[j]=true;
            else
                f[j]=false;
        }
        swaps=0;
        count =0;
        num=0;
        for(j=n-1;j>=0&&count<k;j--)
        {
            if(f[j])
            {
                count++;
                swaps+=num;
            }
            else
            {
                num++;
            }
        }        
        if(count==k)
            fout<<"Case #"<<i<<": "<<swaps<<endl;
        else
            fout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
    }
}
