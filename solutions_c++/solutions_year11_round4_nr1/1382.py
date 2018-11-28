#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int X,N,ttt,RR,SS;
double t;
int W[100001];
int B[100001];
int E[100001];
int main()
{
    int T;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    
    for(int caso=1;caso<=T;caso++)
    {
        cin>>X>>SS>>RR>>ttt>>N;
        t=ttt;
        int tt=0;
        for(int i=0;i<N;i++)
        {
                cin>>B[i]>>E[i]>>W[i];      
              //  cout<<E[i]-B[i]<<endl;  
                tt+=E[i]-B[i];
        }
        vector<pair<int,int> >V;
        V.push_back(make_pair(0,X-tt));
        for(int i=0;i<N;i++)V.push_back(make_pair(W[i],E[i]-B[i]));
        sort(V.begin(),V.end());
        double res=0;
        for(int i=0;i<V.size();i++)
        {
              double d=V[i].second;
              double R=RR+V[i].first;
              double S=SS+V[i].first;
             // cout<<d<<" "<<V[i].first<<" "<<V[i].second<<endl;
              if(d<=t*R)
              {
                   res+=(d/(double)R);
                   t-=(d/(double)R);
                //   cout<<d/(double)R<<"s"<<endl;
                   continue;
                                      
              }
              double b=(d-t*R)/(double)S;
              
              res+=b+t;        
              t=0;
              
        }
        cout<<"Case #"<<caso<<": ";
        printf("%.7lf\n",res);       
    }
    //system("pause");
    return 0;    
}
