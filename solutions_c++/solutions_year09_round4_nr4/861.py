#include<iostream>
#include<string>
#include<vector>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<numeric>
#include<map>
#include<set>
#include<queue>
using namespace std ;
vector<int>X(4),Y(4),R(4);
double radio(int a,int b )
{
    double dev= R[a]+R[b]+hypot(X[a]-X[b],Y[a]-Y[b]);    
    dev=dev/2.0;
    return dev;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    int n=0;
    cin>>n;
    for(int caso=0;caso<n;caso++)
    {
        int t;cin>>t;
        
        for(int i=0;i<t;i++)
            cin>>X[i]>>Y[i]>>R[i];
        
        /*
        for(int i=0;i<t;i++)
            cout<<X[i]<<" "<<Y[i]<<" "<<R[i]<<endl;
            cout<<endl;
        */
        if(t==1){cout<<"Case #"<<caso+1<<": "<<R[0]<<endl;}
        if(t==2)
        {
           double dev=max(R[0],R[1]);    
            cout<<"Case #"<<caso+1<<": "<<dev<<endl;
        }
        if(t==3)
        {
            double dev=min(max(radio(0,1),(double)R[2]/2.0),max(radio(0,2),(double)R[1]/2.0));
            dev=min(dev,max(radio(1,2),(double)R[0]/2.0) );
            //cout<<" -- "<<max(radio(0,1),(double)R[2]/2.0)<<"  "<<max(radio(0,2),(double)R[1]/2.0)<<" "<<max(radio(1,2),(double)R[0]/2.0 )<<endl;
            cout<<"Case #"<<caso+1<<": "<<dev<<endl;
        }
    }
    //system("pause");
    return 0;
}


