#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    int i,t,n,j,c=0,a[2],b[2],cnt=0;
    ifstream in("input_a.txt");
    ofstream out("output_a.txt");
    in>>t;
    for(i=0;i<t;i++)
    {
        in>>n;
        cnt=0;
        for(j=0;j<n;j++)
        {
            in>>a[j]>>b[j];
        }

        if(n==1)
            cnt=0;
        else if(n==2)
        {
            if((a[0]>a[1] && b[0]<b[1]) || (a[0]<a[1] && b[0]>b[1]))
                cnt=1;
            else
                cnt==0;
        }
        c++;
        out<<"Case #"<<c<<": "<<cnt<<"\n";
    }
    return 0;
    }
