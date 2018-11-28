#include<iostream>
using namespace std;
int main()
{
    int t,result[100];
    cin>>t;
    for(int i=0;i<t;i++)
    {       result[i]=0;
            int c[30],s=0,p;
            int n,si;
            cin>>n>>si>>p;
            for(int k=0;k<n;k++)
            cin>>c[k];
           
            for(int j=0;j<n;j++)
            { int q=c[j]/3;
                    if(float(c[j]/3)>=p)
                                result[i]++;
                    else if(q==(p-1)&& c[j]%3!=0)
                    result[i]++;
                    else if(s<si)
                    {
                         
                         if(q==(p-1)&& c[j]%3==0&&q>0)
                         {
                                     result[i]++;
                                     s++;
                                     }                         
                         else if((p-2)==q&& (q*3+2)==c[j])
                         {     result[i]++; s++; }
                    }
            }
            }
            
                for(int i=0;i<t;i++)
                cout<<"Case #"<<i+1<<": "<<result[i]<<endl;
                
}
