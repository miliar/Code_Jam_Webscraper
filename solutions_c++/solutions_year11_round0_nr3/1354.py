#include<iostream>
#include<fstream>
using namespace std;

long t,n,a[200];

int main()
{
    ifstream fin;
    fin.open("C-large.in");
    ofstream fout;
    fout.open("c.out");
    fin>>n;
    for (int k=0;k<n;k++)
    {
        fin>>t;
        long min=10000000,sum=0;
        int p;
        for (int i=0;i<t;i++)
        {
             fin>>a[i];
             sum+=a[i];
             if (a[i]<min) 
             {
                           min=a[i]; 
                           p=i;
             }
        }
        int yh=0;
        for (int i=0;i<t;i++)
         if (i!=p) yh=yh^a[i];
         if (yh!=min) fout<<"Case #"<<k+1<<": NO"<<endl;
          else fout<<"Case #"<<k+1<<": "<<sum-min<<endl;
    }
}
             
        
