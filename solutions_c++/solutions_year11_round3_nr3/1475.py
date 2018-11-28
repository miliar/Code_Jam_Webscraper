#include <iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;
#define pb push_back

int abs(int n)
{
    if(n<0)
    return n*-1;
    else
    return n;
}

int main()
{
    ifstream in("D:\\inp.txt");
    ofstream out("D:\\out.txt");
    int t,n,min,max;
    in>>t;
    for(int ii=1;ii<=t;ii++)
    {
        in>>n>>min>>max;
        vector<int> inp(n);
        for(int i=0;i<n;i++)
        {
            in>>inp[i];
        }
        int flag=1;
        int i;
        for(i=min;i<=max;i++)
        {
            int j;
            for(j=0;j<n;j++)
            {
                if(!(inp[j]%i==0 || i%inp[j]==0))
                break;
            }
            if(j==n)
            {
                flag=0;
                break;
            }

        }
        out<<"Case #"<<ii<<": ";
        if(flag==1)
        {
            out<<"NO"<<endl;
        }
        else
        out<<i<<endl;
    }
    return 0;
}
