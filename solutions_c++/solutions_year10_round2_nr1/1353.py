// Google Code Jam Round 1B 2010
// Problem A: File Fix-it
// soimort

#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream in("A-small-attempt0.in");
    ofstream out("A.out");
    
    int t, n, m;
    string a[100], b[100];
    in>>t;
    for(int i=1; i<=t; i++)
    {
        in>>n>>m;
        for(int j=0; j<n; j++)
        {
            in>>a[j];
            a[j]=a[j]+"/";
        }
        for(int j=0; j<m; j++)
        {
            in>>b[j];
            b[j]=b[j]+"/";
        }
        
        int sum=0;
        if(n==0) n++;
        if(i==1) sum--;
        for(int j=0; j<m; j++)
        {
            int min=100000;
            for(int k=0; k<n; k++)
            {
                int p=0, last, temp=0;
                while(a[k][p]==b[j][p] && p<a[k].length())
                {
                    if(a[k][p]=='/') last=p;
                    p++;
                }
                for(int l=p; l<b[j].length(); l++)
                    if(b[j][l]=='/') temp++;
                if(temp<min) min=temp;
            }
            for(int k=0; k<j; k++)
            {
                int p=0, last, temp=0;
                while(b[k][p]==b[j][p] && p<b[k].length())
                {
                    if(b[k][p]=='/') last=p;
                    p++;
                }
                for(int l=p; l<b[j].length(); l++)
                    if(b[j][l]=='/') temp++;
                if(temp<min) min=temp;
            }
            sum+=min;
        }
        
        out<<"Case #"<<i<<": "<<sum<<endl;
    }
    
    return 0;
}
