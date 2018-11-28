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
        int s,q;
        cin>>s;
        vector<string> eng(s);
        string temp;

        getline(cin,temp,'\n');
        for(int i=0;i<s;i++)
        {
            getline(cin,eng[i],'\n');
        }
        cin>>q;
        getline(cin,temp,'\n');
        vector<string> query(q);
        set<string> ss;
        int ans=0;           
        for(int i=0;i<q;i++)
        {
               getline(cin,temp,'\n');
               if(ss.find(temp)==ss.end() && find(eng.begin(),eng.end(),temp)!=eng.end() ) 
                   ss.insert(temp);
               if(ss.size()==s)
               {
                   ss.clear();
                   ss.insert(temp);
                   ans++;
               }

        }
        cout<<"Case #"<<j<<": "<<ans<<endl;

        

        /*
        for(int i=0;i<s;i++)
        {
            cout<<eng[i]<<endl;
        }
        for(int i=0;i<q;i++)
        {
            cout<<query[i]<<endl;
        }
        */

    }
}
