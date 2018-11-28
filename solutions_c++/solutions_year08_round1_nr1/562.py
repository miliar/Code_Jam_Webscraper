#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;

int t;
int n;
long long x[1000],y[1000];
int main()
{
    ifstream FIN("input.txt");
    ofstream FOUT("output.txt");
    FIN >> t;
    for(int i=1;i<=t;i++)
    {
        FIN >> n;
        for(int j=0;j<n;j++)
            FIN >> x[j];
        for(int j=0;j<n;j++)
            FIN >> y[j];
        
        sort(x,x+n);
        sort(y,y+n);
        
        long long sum=0;
        for(int j=0;j<n;j++)
            sum += x[j]*y[n-j-1];
        FOUT << "Case #" << i << ": " << sum << endl;
    }
}
