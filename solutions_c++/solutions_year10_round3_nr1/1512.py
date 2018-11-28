#include<fstream>
#include<string>
#include<algorithm>
#include<vector>
#include<stdio.h>
#include<iostream>
#include<cmath>
using namespace std;
#define INF (1<<20);




int T,N;

vector<pair<int,int> > data;


int main()
{
freopen("A-small.in","r",stdin);
freopen("sub.out","w",stdout);
cin>>T;
int a,b,tmp;
for(int caseid=1;caseid<=T;caseid++)
{
        cin>>N;
        data.clear();
        int i,j,k;
        for(i=1;i<=N;i++)
        {
                cin>>a>>b;
                data.push_back(make_pair(a,b));
                
        }
        sort(data.begin(),data.end());
        int sor[N];
        
        for(i=0;i<N;i++)
        sor[i]=data[i].second;
        int res=0;
        
        for(i=0;i!=N-1;i++)
        {j=i+1;
        
              
                                      
                                 while(sor[i]>sor[j]&& j!=N)
                                 {j++;
                                 
                                 res++;
                                 }
                                if(j==N-1)
                                 j=N;
                                 
                                 
              
                                 tmp=sor[i];
                                 for(k=i;k!=j-1;k++)
                                 
                                 sor[k]=sor[k+1];
                                 
                                 
                                 sor[j-1]=tmp;
               
        
        }








cout<<"Case #"<<caseid<<": "<<res<<endl;
}



return 0;


}     
