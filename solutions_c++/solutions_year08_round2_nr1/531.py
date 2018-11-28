#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
#define MAXI(a,b) ((a>b)?(a):(b))
#define MINI(a,b) ((a<b)?(a):(b))

bool find(vector<long long> vx,vector<long long> vy,long long xc,long long yc)
    {
    int z=vx.size();
    for(int i=0;i<z;i++)
        {
        if(vx[i]==xc && vy[i]==yc ) return true;
        }
    return false;    
    }

int main()
{
long long   cs, N, A, B, C, D, x0, y0, M ,xc,yc;
    
    cin>>cs;
    vector<long long> vx,vy;
    
    for(int i=1;i<=cs;i++)
        {
        vx.clear();
        vy.clear();
    
        cin>>N>>A>>B>>C>>D>>x0>>y0>>M;
        vx.push_back(x0);
        vy.push_back(y0);
        
        for(int j=0;j<N;j++)
            {
            vx.push_back( ( (A*vx[j]+B)%M) );
            vy.push_back( ( (C*vy[j]+D)%M));
            }
        int cnt=0;
        
        for(int j=0;j<N;j++)
           for(int k=j+1;k<N;k++)
             for(int l=k+1;l<N;l++)
                {
                xc=vx[l]+vx[j]+vx[k];
                yc=vy[l]+vy[j]+vy[k];
                
                if( ((xc%3)==0 ) && ((yc%3)==0 ) )
                        {
                        //if(find(vx,vy,xc/3,yc/3) ) 
                        cnt++;
                        //cout<<xc<<","<<yc<<endl;
                        }   
                }
        cout<<"Case #"<<i<<": "<<cnt<<endl;
        }
    
return 0;
}
