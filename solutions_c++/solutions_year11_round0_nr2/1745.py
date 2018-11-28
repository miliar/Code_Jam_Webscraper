#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>
using namespace std;
int T,n,c,d;
vector<string> comb;
vector<string> del;
const int INF=0x3f3f3f3f;
vector<char> ans;
int myabs(int x)
{
    return x>0?x:(-x);
}
int main()
{
    freopen("BL.in","r",stdin);
    freopen("bout.txt","w",stdout);
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cout<<"Case #"<<t<<": ";
        cin>>c;
        string tmp;
        comb.clear();
        del.clear();
        ans.clear();
        for(int i=1;i<=c;i++)
        {
            cin>>tmp;comb.push_back(tmp);
        }
        cin>>d;
        for(int i=1;i<=d;i++)
        {
            cin>>tmp;
            del.push_back(tmp);
        }
        cin>>n;
        cin>>tmp;
        for(int i=0;i<n;i++)
        {
            ans.push_back(tmp[i]);
            int size=ans.size();
            if(size>=2)
            {
                char c1=ans[size-1];
                char c2=ans[size-2];
                bool finded=false;
                for(int j=0;j<comb.size();j++)
                {
                    if((c1==comb[j][0] && c2==comb[j][1]) || (c2==comb[j][0] && c1==comb[j][1]))
                    {
                        ans.erase(ans.end()-1);
                        ans[size-2]=comb[j][2];
                        break;
                    }
                }
            }
            size=ans.size();
            if(size>=2)
            {
            bool flag=false;
            for(int j=0;j<size-1;j++)
            {
                for(int k=0;k<del.size();k++)
                {
                    if((ans[size-1]==del[k][0] && ans[j]==del[k][1]) || (ans[size-1]==del[k][1] && ans[j]==del[k][0]))
                    {
                        ans.clear();
                        flag=true;
                        break;
                    }
                }
                if(flag) break;
            }
            }
        }
        cout<<"[";
        for(int i=0;i<ans.size();i++)
        {
            if(i!=0) cout<<", ";
            cout<<ans[i];
        }
        cout<<"]"<<endl;
    }
    return 0;
}
