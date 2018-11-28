#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int T;
char used[20];
int Max;
int main ()
{
    ifstream fin ("res.in");
    ofstream fout ("res.out");
    fin >> T;
    string s;
    string t;
    long long int x;
    getline(fin,s);
    
    for (int i=1;i<=T;++i)
    {
        Max=0;
        for (int j=0;j<=9;++j)
        used[j]=0;

        getline(fin,s);
        int n=s.length();
        
        for (int j=0;j<n;++j)
        {
            if (j==0)
                {
                   used[1]=s[j];

                   if (Max<1)
                   Max=1;
                   t[0]=49;
                }
                
            if (j!=0)
            {
                bool ok=false;
            for (int k=0;k<=9;++k)
            {
                
                if (used[k]==s[j])
                {
                   
                   t[j]=k+48;
                   used[k]=s[j];
                   if (Max<k)
                   {
                      Max=k;
                   }
                   ok=true;
                   break;
                }
                
            }

            if (!ok)
            for (int k=0;k<=9;++k)
            if (used[k]==0)
                {
                   t[j]=k+48;
                   used[k]=s[j];
                   if (Max<k)
                   {
                      Max=k;
                   }
                   
                   break;
                   
                }
            }
        }
        x=0;
        int p=0;
        for (int k=n-1;k>=0;--k)
        {
            x+=(t[k]-48)*pow(10.0,p);
            ++p;
        }
        cout << endl;
        int base=Max+1;

        long long int y=0;
        int last=0;
        string q="";
        
        for (int k=0;k<n;++k)
        last=last*base+(t[k]-48);
           
        y=last;
        
        fout << "Case #" << i << ": " << y << endl;
        
    }
    
    return 0;
}
