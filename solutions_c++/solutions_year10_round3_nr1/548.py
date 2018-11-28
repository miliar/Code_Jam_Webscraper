#include<iostream>

using namespace std;

int co(int *x,int *y,int n,int a,int b){
    int r=0;
    for(int i=0;i<n;i++){
      if( x[i]>a && y[i]>b );
      else if( x[i]<a && y[i]<b );
      else r++;
    }
    return r;
}
int main(){    freopen("input.cpp","r",stdin);  freopen("output.cpp","w",stdout);
    int _=1; int t;scanf("%d",&t);
    while( t-- ){
      int n;scanf("%d",&n);
      int x[n],y[n],ans=0;
      for(int i=0;i<n;i++){
         scanf("%d %d",&x[i],&y[i]);
         ans+=co(x,y,i,x[i],y[i]);
      }
     printf("Case #%d: %d\n",_++,ans);
    
    }
    
   // cout<<"\nTime take :: "<<clock()<<" ::ms"<<endl;while(true);
    return 0;
}
