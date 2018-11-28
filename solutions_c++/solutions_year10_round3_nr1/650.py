#include<fstream>
using namespace std;

int main()
{
    ifstream fin("A.in");
    ofstream fout("A.out");
    
    int t,j,n,pt,k,a[1000],b[1000];
    fin>>t;
    
    for(int i=1;i<=t;i++)
    {
        fin>>n;
        
        pt=0;
        for(k=0;k<n;k++)
        {
            fin>>a[k]>>b[k];
        }

        if(n>1)
        {
            for(j=0;j<n;j++)
            {
                for(k=j+1;k<n;k++)
                {
                    if(a[j]<a[k]&&b[j]>b[k])
                       pt++;
                    else if(a[j]>a[k]&&b[j]<b[k])
                       pt++;
                }
            }
        }
        fout<<"Case #"<<i<<": "<<pt<<endl;
    }
}
