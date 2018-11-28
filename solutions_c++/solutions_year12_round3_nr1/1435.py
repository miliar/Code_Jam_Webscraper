#include<iostream>
#include<fstream>
int a[1000][1000];
using namespace std;
main()
{
    int t,i,n;
     ifstream in;
    ofstream out;
    out.open("out_d.txt");
    in.open("in_d.txt");
    in>>t;
    for(i=0;i<t;i++)
    {

        int j,temp,k,n1,l;
        in>>n;
        for(j=0;j<n;j++)
        for(k=0;k<n;k++)
        a[j][k]=0;
        for(j=0;j<n;j++)
        {
            in>>temp;
            for(k=0;k<temp;k++)
            {
                in>>n1;
                a[j][n1-1]++;
            }
        }
        for(j=0;j<n;j++)
        {
            for(k=0;k<n;k++)
            {
                if(a[j][k])
                {
                    for(l=0;l<n;l++)
                    {
                        if(a[l][j])
                        a[l][k]++;
                    }
                }
            }
        }
        int flag=0;
        for(j=0;j<n;j++)
        {
            for(k=0;k<n;k++)
            {
            //   cout<<a[j][k]<<" ";
            if(a[j][k]>1)
            {
                flag=1;
                break;
            }
            }
           // cout<<endl;
            if(flag) break;
        }
      // cout<<endl;
        if(flag)
        out<<"Case #"<<i+1<<": "<<"Yes"<<endl;
        else
        out<<"Case #"<<i+1<<": "<<"No"<<endl;
    }
    in.close();
    out.close();
}
