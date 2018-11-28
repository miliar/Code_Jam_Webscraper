#include<iostream>
#include<fstream>
using namespace std;

int t;

int main()
{
    ifstream fin;
    fin.open("d.in");
    ofstream fout;
    fout.open("d.out");
    fin>>t;
    for (int k=0;k<t;k++)
    {
             
        int n,a[2000],b[2000];
            fin>>n;
        for (int i=0;i<n;i++) {fin>>a[i];b[i]=a[i];}
        for (int i=0;i<n-1;i++)
         for (int j=0;j<n-i-1;j++)
             if (a[j]>a[j+1])
             {    
                  int temp;
                  temp=a[j];
                  a[j]=a[j+1];
                  a[j+1]=temp;
                  }
                  int ans=0;
         for (int i=0;i<n;i++)
          if (a[i]!=b[i]) ans++;
          fout<<"Case #"<<k+1<<": "<<ans<<".000000"<<endl;
    }
}
