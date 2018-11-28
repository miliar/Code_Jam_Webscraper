#include<iostream>
#include<conio.h>
#include<vector>
#include<fstream>
#include <iomanip>

using namespace std;

pair<double,int> tempp;

vector< pair<double,int> > V;

long double q,x,s,r,t,n,total,ans,temp1,temp2,temp3,temp4,temp5,temp6;
long double B[2000],E[2000],W[2000];

int main()
{
    ifstream fin;
    fin.open("A-large.in");
    ofstream fout;
    fout.open("out1large.out");
    fout << fixed;

    fin>>q;
    
    for(int w=1;w<=q;w++)
    {
            fin>>x>>s>>r>>t>>n;
            total=0;
            
            for(int i=1;i<=n;i++)
            {
                    fin>>B[i]>>E[i]>>W[i];
                    total+=(E[i]-B[i]);
            }
            
            V.clear();
            for(int i=1;i<=n;i++)
            {
                    tempp.first=((1/(s+W[i]))-(1/(r+W[i])));
                    tempp.second=i;
                    V.push_back(tempp);
            }
            
            tempp.first=((1/s)-(1/r));
            tempp.second=-1;
            V.push_back(tempp);
            
            sort(V.begin(),V.end());
            
            
            ans=0;
            temp1=t;
            
           for(int i=V.size()-1;i>=0;i--)
           {
                   if(V[i].second==-1)
                   {
                                      temp2=x-total;
                                      temp3=r;
                                      temp6=s;
                   
                   }
                   
                   else
                   {
                       temp2=E[((V[i]).second)]-B[(V[i]).second];
                       temp3=r+W[(V[i]).second];
                       temp6=s+W[(V[i]).second];
                   }
                   
                   if(temp1==0)
                   {
                               ans+=temp2/temp6;
                               continue;
                   }
                   
                               
                   
                   temp4=temp2/temp3;
                   
                   if(temp4<=temp1)
                   {
                                   ans+=temp4;
                                   temp1-=temp4;
                                   continue;
                   }
                   
                   
                   ans+=temp1;
           
                   
                   temp5=temp3*temp1;
                   
                   temp5=temp2-temp5;
                   ans+=temp5/temp6;
                   
                   temp1=0;
           }
           
           fout<<"Case #"<<w<<": "<<setprecision (6)<<ans<<"\n";
    }
    //getch();
}
                   
                   
                   
                   
                       
                         
            
            
                    
            
