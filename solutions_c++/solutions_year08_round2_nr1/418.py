#include<iostream>
#include<vector>
#include<list>
#include<string>
#include<algorithm>
#include <sstream>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
//getline(std::cin,temp);

using namespace std;
vector<long long>x,y;
int main()
{
    int N,i,j,k,l,m,count;
    long long n,A,B,C,D,x0,y0,M,X,Y;
    cin>>N;
    for(i=0;i<N;i++)
    {
        cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
        X = x0; Y = y0;
        count=0;
        x.clear();
        y.clear();
        x.push_back(X);
        y.push_back(Y);
        for (j = 1; j<=n-1;j++)
        {  
            X = (A * X + B) % M;
            Y = (C * Y + D) % M;
          x.push_back(X);
          y.push_back(Y);
          //cout<<x[j]<<y[j];
        }
        //cout<<x.size()<<y.size();
        for(j=0;j<=n-1;j++)
        {
         for(k=j+1;k<=n-1;k++)
         {
                           for(l=k+1;l<=n-1;l++)
                           {
                                  x0=(x[j]+x[k]+x[l])/3;
                                  y0=(y[j]+y[k]+y[l])/3;
                                  if((x[j]+x[k]+x[l])%3==0&&(y[j]+y[k]+y[l])%3==0)
                                  {
                                              count++;
                                  }
                           }
         }
        }
        cout<<"Case #"<<i+1<<": "<<count<<"\n";
    }
    //system("PAUSE");
    return 0;
}
