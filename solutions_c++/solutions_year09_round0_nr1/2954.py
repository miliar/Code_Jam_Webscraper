#include<iostream>
#include<vector>
#include<string>
#include<fstream>
using namespace std;
vector<string> dict,patt;
int main()
{
    ofstream fp;
    fp.open("output.in");
    int l,d,n,i,j,k,count,siter,flag,z,pcount;
    cin>>l>>d>>n;
    dict.resize(d);
    patt.resize(n);
    for(i=0;i<d;i++)
        cin>>dict[i];
    for(i=0;i<n;i++)
        cin>>patt[i];
    for(i=0;i<n;i++)
    {
        count=0;

        for(j=0;j<d;j++)
        {
            flag=siter=0,z=1;
            for(k=0;k<patt[i].length();k++)
            {

                if(patt[i].at(k)=='(')
                {
                    flag=1;
                    pcount=0;
                    continue;
                }
                else if(patt[i].at(k)==')')
                {
                    flag=0;
                    siter++;
                    if(pcount==0)
                    {
                    z=0;
                    break;
                    }
                    continue;
                }

                if(patt[i].at(k)==dict[j].at(siter))
                {
                    //cout<<"\n\n\n1="<<patt[i].at(k)<<"\n2="<<dict[j].at(siter)<<"\n\n\n";
                    if(flag==0)
                    siter++;
                    else
                    pcount++;
                    }
                else if(flag==0)
                {
                    //cout<<"\n\n\n1="<<patt[i].at(k)<<"\n2="<<dict[j].at(siter)<<"\n\n\n";
                    z=0;
                    siter++;
                    break;
                    }
            }

            if(z==1)
            count++;
        }
        fp<<"Case #"<<i+1<<": "<<count<<endl;
    }

    return 0;
}
