#include<iostream>
#include<vector>
#include<math.h>

#include<fstream>
#include<stdio.h>
#include<sstream>
using namespace std;


fstream in("input.in",ios::in);
fstream out("output.out",ios::out);
#define cin in 
#define cout out

int main()
{
    long long int n,A,B,C,D, x0, y0,M;
    int N;
    cin>>N;
    long long int X,Y;
    int flag=0;
    int ans;
    for(int i=1;i<=N;i++)
    {
            ans=0;
            cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
            vector <pair <long long int,long long int> > v;
            X=x0;
            Y=y0;
            pair <long long int,long long int> p;
            p.first=X;
            p.second=Y;
           //       cout<<X<<" "<<Y<<endl;
            v.push_back(p);
            for(int j = 1;j<= n-1;j++)
            {
                  pair <long long int,long long int> temp;
                  X = (A * X + B) %M;
                  Y = (C * Y + D)% M;
             //     cout<<X<<" "<<Y<<endl;
                    temp.first=X;
                    temp.second=Y;
                  v.push_back(temp);
                  
            }
            
            for(int j=0;j<v.size()-2;j++)
            {
                    for(int k=j+1;k<v.size()-1;k++)
                    {
                            for(int l=k+1;l<v.size();l++)
                            {
                             
                             float xx,yy;
                             xx=(float)((float)v[j].first+(float)v[k].first+(float)v[l].first)/3.0;
                             yy=(float)((float)v[j].second+(float)v[k].second+(float)v[l].second)/3.0;
                            // cout<<xx<<" "<<yy<<endl;
                             if(xx==floor(xx)&&yy==floor(yy))
                                   ans++;                         
                             }
                    }
            }
            cout<<"Case #"<<i<<": "<<ans<<endl;
            
  
    }
     system("pause");
   return 0;
}                        
                  
