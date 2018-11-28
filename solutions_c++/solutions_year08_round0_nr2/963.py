#include<iostream>
#include<string>
#include<vector>
#include<sstream>
#include<algorithm>
using namespace std;
int main()
{
    int tc;
    cin>>tc;
    vector<vector<int> > ans;
    vector<int> ad,aa,bd,ba;
    for(int i=0;i<tc;i++)
    {
            ad.erase(ad.begin(),ad.end());
            aa.erase(aa.begin(),aa.end());
            bd.erase(bd.begin(),bd.end());
            ba.erase(ba.begin(),ba.end());
            int na,nb,t,a,b,c,d;
            char e,f;
            cin>>t>>na>>nb;
            string s;
            getline(cin,s);
            for(int j=0;j<na;j++)
            {
                    getline(cin,s);
                    istringstream z(s);
                    z>>a>>e>>b>>c>>f>>d;
                    ad.push_back(60*a+b);
                    ba.push_back(60*c+d+t);
            }
            for(int j=0;j<nb;j++)
            {
                    getline(cin,s);
                    istringstream z(s);
                    z>>a>>e>>b>>c>>f>>d;
                    bd.push_back(60*a+b);
                    aa.push_back(60*c+d+t);
            }
            sort(ad.begin(),ad.end());
            sort(aa.begin(),aa.end());
            sort(bd.begin(),bd.end());
            sort(ba.begin(),ba.end());
            int ana=0,anb=0;
            for(int j=0;j<ad.size();j++)
            {
                   if(aa.size()==0)
                   {
                      ana+=ad.size()-j;
                      break;
                   }                    
                if(ad[j]>=aa[0])
                {
                   aa.erase(aa.begin());                
                }
                else
                   ana++;
            }
            for(int j=0;j<bd.size();j++)
            {
                   if(ba.size()==0)
                   {
                      anb+=bd.size()-j;
                      break;
                   }
                if(bd[j]>=ba[0])
                {
                   ba.erase(ba.begin());             
                }
                else
                   anb++;
            }          
            vector<int> q;
            q.push_back(ana);
            q.push_back(anb);
            ans.push_back(q);
    } 
    for(int i=0;i<ans.size();i++)
            cout<<"Case #"<<i+1<<": "<<ans[i][0]<<" "<<ans[i][1]<<endl;
    return 0;
}          
                
                           
