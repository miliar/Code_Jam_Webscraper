#include<iostream>
#include<fstream>
#include <iomanip>
using namespace std;
main()
{
    int t,n,i,j;
    double v[201],s[201],sum;
    ifstream in;
    ofstream out;
    out.open("out_s.txt");
    in.open("in_s.txt");
    in>>t;
    for(j=1;j<=t;j++)
    {
        sum=0.0;
        in>>n;
        for(i=0;i<n;i++)
        {
            in>>s[i];
            sum+=s[i];
        }
        //sum*=2;
        double is=2*sum/n;
        double new_sum=0.0;
        out<<"Case #"<<j<<": ";
        int count=0;
        for(i=0;i<n;i++)
        {
            //v[i]=((is-s[i])*2)/sum;
            if(s[i]<is)
            {
                count++;
                new_sum+=s[i];
            }
            //out<<setprecision(8)<<v[i]*100<<" ";
        }
        cout<<sum<<" "<<new_sum<<endl;
        if(count<n)
        is=(sum+new_sum)/count;
        for(i=0;i<n;i++)
        {
            //v[i]=((is-s[i])*2)/sum;
            if(is<=s[i])
            {
                v[i]=0;
                continue;
            }
            else
            {
                v[i]=(is-s[i])/(sum);
            }
            //out<<setprecision(8)<<v[i]*100<<" ";
        }
        for(i=0;i<n;i++)
        out<<setprecision(8)<<v[i]*100<<" ";
        out<<endl;


    }
    in.close();
    out.close();

}
