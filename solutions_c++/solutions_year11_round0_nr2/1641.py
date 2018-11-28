#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
    int t;
    cin>>t;
    map<char,int> els;
    els['Q']=0;
    els['W']=1;
    els['E']=2;
    els['R']=3;
    els['A']=4;
    els['S']=5;
    els['D']=6;
    els['F']=7;
    for(int test_case=0;test_case<t;test_case++)
    {
        int c;
        vector<string> comb;
        cin>>c;
        for(int i=0;i<c;i++)
        {
            string s;
            cin>>s;
            comb.push_back(s);
        }

        int d;

        vector<string> op;
        cin>>d;
        for(int i=0;i<d;i++)
        {
            string s;
            cin>>s;
            op.push_back(s);
        }
        int n;
        string s;
        cin>>n>>s;
        char ans[101];
        int k=0;
        for(int i=0;i<n;i++)
        {
            if(k==0)
                ans[k++]=s[i];
            else
            {
                bool co=false;
                for(int j=0;j<comb.size();j++)
                {
                    if(ans[k-1]==comb[j][0]&&s[i]==comb[j][1]||ans[k-1]==comb[j][1]&&s[i]==comb[j][0])
                    {
                        ans[k-1]=comb[j][2];
                        co=true;
                        break;
                    }
                }

                if(!co)
                {
                    for(int j=0;j<op.size();j++)
                    {
                        for(int h=0;h<k;h++)
                        if(ans[h]==op[j][0]&&s[i]==op[j][1]||ans[h]==op[j][1]&&s[i]==op[j][0])
                        {
                            k=0;
                            co=true;
                            break;
                        }
                    }
                    if(!co)ans[k++]=s[i];
                }
            }
        }
        cout<<"Case #"<<test_case+1<<": [";
        for(int i=0;i<k;i++)
        {
            cout<<ans[i];
            if(i<k-1)cout<<", ";
        }
        cout<<']'<<endl;
    }
    return 0;
}
