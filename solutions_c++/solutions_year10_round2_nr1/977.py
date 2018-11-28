//Bismillahir Rahmanir Rahim

#include <iostream>
#include <cmath>
#include <vector>
#include <string>
using namespace std;


int main()
{
    freopen("I.txt","rt",stdin);
    freopen("Output.txt","wt",stdout);
    int i,n,j,k,l,m,kas,cas;
    vector<string>pirate;
    vector<vector<string> >vec;
    string a,b,c,d;
    cin>>kas;
    long long MIN=0;
    for(cas=1;cas<=kas;cas++){

        cin>>n>>m;

        for(i=0;i<n;i++){
        cin>>a;

        c.clear();
        for(k=0;k<a.size();k++){
                if(a[k]=='/'){
                    if(c.size()>0)
                pirate.push_back(c);
                c.clear();
                }
                c+=(a[k]);

            }
            pirate.push_back(c);
            vec.push_back(pirate);
            pirate.clear();
        }
        for(i=0;i<m;i++){
            cin>>a;
            c.clear();
            pirate.clear();
            for(k=0;k<a.size();k++){
                if(a[k]=='/'){
                    if(c.size()>0)
                pirate.push_back(c);
                c.clear();
                }
                c+=(a[k]);

            }
            if(c.size()>0)
            pirate.push_back(c);
            c.clear();

            long long tot=2147483647;

            for(j=0;j<vec.size();j++){
                int p=min(vec[j].size(),pirate.size());
                int flag=0;
                long long coun=0;
                for(k=0;k<p;k++){
                if(pirate[k]!=vec[j][k]){
                    //<<pirate[k]<<" "<<vec[j][k]<<endl;
                flag=1;
                }
                if(flag)coun++;
                }
                if(vec[j].size()<pirate.size())
                coun+=(pirate.size()-vec[j].size());
                if(tot>coun)tot=coun;

                //cout<<coun<<"  ??????????  "<<tot<<endl;
                }
                if(vec.size()==0)
                {
                    tot=pirate.size();
                }
                //cout<<tot<<"    "<<MIN<<endl;
                vec.push_back(pirate);
                MIN+=tot;
            }
            cout<<"Case #"<<cas<<": ";
            cout<<MIN<<endl;
            MIN=0;
            for(i=0;i<vec.size();i++)
            vec[i].clear();
            pirate.clear();
    }
    return 0;
}
