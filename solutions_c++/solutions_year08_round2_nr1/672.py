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
    long long int n,a,b,c,d,x0, y0,m;
    int N;
    cin>>N;
    long long int x,y;
    int flag=0;
    int ans;
    int count=1;
    while(N--)
    {        
            ans=0;
            cin>>n>>a>>b>>c>>d>>x0>>y0>>m;
            vector <pair <long long int,long long int> > nik;
            x=x0;
            y=y0;
            pair <long long int,long long int> pi;
            pi.first=x;
            pi.second=y;
            nik.push_back(pi);
            for(int j = 1;j<= n-1;j++)
            {
                  pair <long long int,long long int> temp;
                  x = (a * x + b) %m;
                  y = (c * y + d)% m;
                    temp.first=x;
                    temp.second=y;
                  nik.push_back(temp);
                  
            }
            
            for(int j=0;j<nik.size()-2;j++)
            {
                    for(int k=j+1;k<nik.size()-1;k++)
                    {
                            for(int l=k+1;l<nik.size();l++)
                            {
                             
                             float xx,yy;
                             xx=(float)((float)nik[j].first+(float)nik[k].first+(float)nik[l].first)/3.0;
                             yy=(float)((float)nik[j].second+(float)nik[k].second+(float)nik[l].second)/3.0;
                             if(xx==floor(xx)&&yy==floor(yy))
                                   ans++;                         
                             }
                    }
            }
            cout<<"Case #"<<count<<": "<<ans<<endl;
            count++;
  
    }
     system("pause");
   return 0;
}                        
                  
