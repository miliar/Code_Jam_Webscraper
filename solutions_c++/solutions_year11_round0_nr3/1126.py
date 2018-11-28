#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

int main()
{
    int t,n,p,q,max,sum1,sum2,val1,val2;
    int candy[1000];
    
//    int p1,p2,t1,t2,time;
    
    fstream fin,fout;
    fin.open("a.in",ios::in);
    fout.open("a.out",ios::out);
    
    fin >> t;
    for(int i=0;i<t;i++)
    {
        fin >> n;
        max=0;
        for(int j=0;j<n;j++)
        {
            fin >> candy[j];
        }
        fout<<"Case #"<<i+1<<": ";
        //cout<<"Case #"<<i+1<<": ";
        p = (int)(pow(2.0,n));
        for(int k=1;k<p-1;k++)
        {
            sum1=sum2=val1=val2=0; 
            for(int j=n-1;j>=0;j--)
            {
                q = k >> j;
                q = q & 1;
                //cout<<q;
                if(q)
                {
                    sum1^=candy[j];
                    val1+=candy[j];
                }
                else
                {
                    sum2^=candy[j];
                    val2+=candy[j];
                }
                
            }
            //cout<<'='<<val1<<' '<<val2<<endl;
            if(sum1==sum2)
            {
                int val = val1>val2?val1:val2;
                if(val>max)
                    max=val;
            }             
        }
        if(max == 0)
           fout << "NO" << endl;
        else
           fout << max << endl;
        
    }
    //int x;
    //cin>>x;
    return 0;
}
