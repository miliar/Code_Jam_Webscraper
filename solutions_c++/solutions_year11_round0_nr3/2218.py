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
    int t,n;
    in>>t;
    for(int ii=0;ii<t;ii++)
    {
        in>>n;
        vector<int> a(n);
        for(int i=0;i<n;i++)
        {
            in>>a[i];
        }
        sort(a.begin(),a.end());
        int t1,t2,t3,t4,i;
        for(i=0;i<n-1;i++)
        {
            t3=a[i];
            t4=a[i+1];
            t1=a[i];
            t2=a[i+1];
            for(int j=i-1;j>=0;j--)
            {
                t3+=a[j];
                t1^=a[j];
            }

            for(int j=i+2;j<n;j++)
            {
                t4+=a[j];
                t2^=a[j];
            }

            if(t1==t2)
            break;
        }
        if(i==n-1)
        out<<"Case #"<<ii+1<<": NO"<<endl;
        else if(t3>t4)
        out<<"Case #"<<ii+1<<": "<<t3<<endl;
        else
        out<<"Case #"<<ii+1<<": "<<t4<<endl;

    }
    return 0;
}
