#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
using namespace std;
void cropTriangles(vector <long long> x,vector <long long> y)
{
     
     long long count=0;
     vector <long long> x1;
     vector <long long> y1;
     for(long long i=0;i<x.size()-2;i++)
     {
             for(long long j=i+1;j<x.size()-1;j++)        
             {
                     for(long long k=j+1;k<x.size();k++)        
                     {
                              if((x[i]+x[j]+x[k])%3==0 && (y[i]+y[j]+y[k])%3==0) 
                              {   //x1.push_back((x[i]+x[j]+x[k])/3);
                                  //y1.push_back((y[i]+y[j]+y[k])/3);
                                  count++;
                              }
                                //cout<<y[i]+y[j]+y[k]<<"  "<<count<<endl; 
                                /*for(long long m=0;m<x1.size();m++)
                                if(((x[i]+x[j]+x[k])/3)==x[m]&&((y[i]+y[j]+y[k])/3)==y[m])
                                break;
                                if(i==x1.size())
                                     count++;*/
                     }
                     
             }
     }
     cout<<count;
     
     //do
     //{
             
    // }while(next_permutation)
}
int main()
{       
        long long k;
        cin>>k;
        
 
        
        for(long long i=0;i<k;i++)
        {
                long long  n, A, B, C, D, x0, y0,M,X,Y;
                 
                 cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
                 vector <long long> x(n,0);
                 vector <long long> y(n,0);
                 X = x0; Y = y0;
                 x[0]=X;
                   y[0]=Y;
                   //cout<<X<<"  "<<Y<<endl;
                   for (long long j = 1; j< n;j++)
                  { 
                       X = (A * X + B) %M;
                       Y = (C * Y + D) %M;
                       x[j]=X;
                       y[j]=Y;
                   //cout<<X<<"  "<<Y<<endl;
                   }
                  // for(long long j=0;j<x.size();j++)
                       //    cout<<x[j]<<"  "<<y[j]<<endl;
                   cout<<"Case #"<<(i+1)<<": ";
                   cropTriangles(x,y);
                   
                
                   
                if(i!=(k-1))
                            cout<<endl;
        }
       
        getchar();
        return 0;
}
