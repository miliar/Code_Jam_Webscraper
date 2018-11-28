#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int c,r,k,g[1000],sum=0,j=0,i=0,mon=0,n;
    ifstream fin("C-small.in");
    ofstream fout("output.out");
    fin>>c;
    j=1;
    while(c)
    {
        mon=0;
        sum=0;
        fin>>r>>k>>n;
        for(i=0;i<n;i++)
        {
            fin>>g[i];
            sum=sum+g[i];
        }
        if(sum<=k)
        {
            fout<<"Case #"<<j<<": "<<sum*r<<endl;
        }
        else
        {
            i=0;

            while(r)
            {
                sum=0;
                while(sum+g[i]<=k)
                {
                    sum=sum+g[i];
                    i++;
                    if(i==n)
                    i=0;
                }
                r--;
                mon+=sum;
            }
            fout<<"Case #"<<j<<": "<<mon<<endl;
        }
        j++;
        c--;
    }
}
