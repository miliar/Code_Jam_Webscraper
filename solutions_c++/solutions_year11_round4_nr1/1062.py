#include <stdio.h>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
using namespace std;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout); 
    
    int N;
    scanf("%d",&N);
    int s,m,R,t,n,A,B,C;
    for(int _h=0;_h<N;_h++)
    {
       vector< pair<int,double> > v;
       scanf("%d%d%d%d%d",&m,&s,&R,&t,&n);
       double sum=0;
       for(int r=0;r<n;r++)
       {
         scanf("%d%d%d",&A,&B,&C);
         sum+=(B-A);
         v.push_back(  make_pair(C,B-A) );
       }
       v.push_back(make_pair(0,m-sum));
       
       sort(  v.begin(),v.end() );
       double T=t; 
       double res=0;
       for(int r=0;r<v.size();r++)
       {
          if(  T>0 )        
          {
            double T2=min(T,v[r].second/(double)(R+v[r].first)); 
            res+=T2;
            v[r].second-=T2*(double)((R+v[r].first));
            T-=T2;
          }
          
          res+=v[r].second/(s+v[r].first);
       }
       printf("Case #%d: %lf\n",_h+1,res);
    }
    
    return 0;   
}
