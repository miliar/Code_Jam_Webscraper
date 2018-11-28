#include <algorithm>
#include<string>
#include<map>
#include<iostream>
#include<cstdio>
#include<vector>

using namespace std;

int main()
   {
      vector<pair<int, int> > t[2];
      
      int na,nb;
      int res[2];
      int tt;
      int m;
      
      cin>>m;
      for(int caseid=0;caseid<m;caseid++)
         {
            res[0]=0;
            res[1]=0;
            t[0].clear();
            t[1].clear();
            
            int a,b,c,d;
            cin>>tt;
            cin.get();
            cin>>na;
            cin.get();
            cin>>nb;
           
            
            for(int i = 0;i<na;i++)
               {
                  scanf("%d:%d %d:%d",&a,&b,&c,&d);
                  //cout<<a<<b<<c<<d<<endl;
                  t[0].push_back(make_pair(a*60+b,c*60+d));
                  
               }
            
            for(int i = 0;i<nb;i++)
               {
                  scanf("%d:%d %d:%d",&a,&b,&c,&d);
                  //cout<<a<<b<<c<<d<<endl;
                  t[1].push_back(make_pair(a*60+b,c*60+d));
               }
            
            sort(t[0].begin(),t[0].end());
            sort(t[1].begin(),t[1].end());
            
            while(true)
               {
                  int sa=t[0].size();
                  int sb=t[1].size();
                  
                  if(sa+sb==0)break;
                  int gyz=50000000;
                  int trb=50000000;
                  
                  if(sa>0)gyz = t[0][0].first*10000+t[0][0].second;
                  if(sb>0)trb = t[1][0].first*10000+t[1][0].second;
                  
                  int pos = 0;
                  
                  if(trb<gyz)
                     {
                        pos=1;
                        
                     }
                  
                  gyz=t[pos][0].first;
                  res[pos]++;
                  
                  while(true)
                     {
                        //    cout<<" "<<pos<<endl;
                        int j;
                        bool found=false;
                        for(j = 0;j<(int)t[pos].size();j++)
                           {
                              if(t[pos][j].first>=gyz)
                                 {
                                    found=true;break;
                                 }
                           }
                        if(!found)break;
                        
                        gyz=t[pos][j].second+tt;
                        t[pos].erase(t[pos].begin()+j,t[pos].begin()+j+1);
                        
                        pos=(pos+1)%2;
                        
                     }
               }
            
            
            cout<<"Case #"<<(caseid+1)<<": "<<res[0]<<" "<<res[1]<<endl;
         }
   }
