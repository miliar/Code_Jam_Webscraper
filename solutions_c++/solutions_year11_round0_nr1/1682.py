#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;
int abs(int n)
{
    return n>0 ? n : -n;
}
int minnum(int a,int b)
{
    return a<=b ? a : b;
}
int main()
{
    ifstream cin("f1.in");
    ofstream cout("f2.out");
    int t;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
            int n;
            cin>>n;
            int ans=0;
            int b=1;
            int o=1;
            int opass=0;
            int bpass=0;
            vector<int> ostation;
            vector<int> bstation;
            vector<char> command;
            for(int i=1;i<=n;i++)
            {
                    char c;
                    int station;
                    cin>>c>>station;
                    if(c=='O')ostation.push_back(station);
                    else bstation.push_back(station);
                    command.push_back(c);
            }
            for(int i=0;i<command.size();i++)
            {
                   if(command[i]=='O')
                   {
                       ans+=abs(ostation[opass]-o)+1;
                       int step=abs(ostation[opass]-o)+1;
                       o=ostation[opass];
                       opass++;
                       if(bstation.size()==bpass){continue;}
                       else{
                             if(bstation[bpass]>=b){
                                b+=minnum((bstation[bpass]-b),step);
                             }
                             else{
                                b-=minnum((b-bstation[bpass]),step);
                             }
                       }
                   }
                   else
                   {
                       ans+=abs(bstation[bpass]-b)+1;
                       int step=abs(bstation[bpass]-b)+1;
                       b=bstation[bpass];
                       bpass++;
                       if(ostation.size()==opass){continue;}
                       else{
                             if(ostation[opass]>=o){
                                o+=minnum((ostation[opass]-o),step);
                             }
                             else{
                                o-=minnum((o-ostation[opass]),step);
                             }
                       }
                   }
            }
                       
                       
            cout<<"Case #"<<j<<": "<<ans<<endl;
    } 
}
                         
