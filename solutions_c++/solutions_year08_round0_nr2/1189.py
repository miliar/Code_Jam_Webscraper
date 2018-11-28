#include<iostream>
#include<cstdio>
#include<vector>
#include<set>
using namespace std;
int main()
{
    int n;
    cin>>n;
    for(int j=1;j<=n;j++)
    {
      
        int gap;
        cin>>gap;
        int na,nb;
        cin>>na>>nb;
        vector<vector<int> > train(na+nb,3);
        
        for(int i=0;i<na;i++)
        {
            int h1,m1,h2,m2;
            scanf(" %d:%d %d:%d",&h1,&m1,&h2,&m2);
            train[i][0]=h1*60+m1;
            train[i][1]=h2*60+m2;
            train[i][2]=0;
        }
 
        
        for(int i=0;i<nb;i++)
        {
            int h1,m1,h2,m2;
            scanf(" %d:%d %d:%d",&h1,&m1,&h2,&m2);
            train[i+na][0]=h1*60+m1;
            train[i+na][1]=h2*60+m2;
            train[i+na][2]=1;
        }
        vector<multiset<int> > resources(2);

        sort(train.begin(),train.end());
        
        /*for(int i=0;i<train.size();i++)
        {
            for(int j=0;j<3;j++)
            {
                cout<<train[i][j]<<" ";
            }
            cout<<endl;
        }*/



        int ans[2]={0,0};
        
        for(int i=0;i<train.size();i++)
        {
            resources[1-train[i][2]].insert((train[i][1]+gap));
        }


        for(int i=0;i<train.size();i++)
        {
            
            if(resources[train[i][2]].size()==0)
            {ans[train[i][2]]++;continue;}

            if(*(resources[train[i][2]].begin()) > train[i][0] )
            {ans[train[i][2]]++;continue;}
            resources[train[i][2]].erase(resources[train[i][2]].begin());

        }
        cout<<"Case #"<<j<<": "<<ans[0]<<" "<<ans[1]<<endl;
       
    }
}
