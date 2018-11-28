#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream fin("input.in");
    ofstream fout("output.txt");
    int i=1,j,k,t,n,a[15],b[15],c;
    fin>>t;
    while(i<=t)
    {
        c=0;
        fin>>n;
        for(j=1;j<=n;j++)
        fin>>a[j]>>b[j];
        for(j=1;j<n;j++)
        {
            for(k=j+1;k<=n;k++)
            if((a[j]<a[k] && b[j]>b[k]) ||(a[j]>a[k] && b[j]<b[k]))
            c++;
        }
        fout<<"Case #"<<i<<": "<<c<<endl;
        i++;
    }

}
