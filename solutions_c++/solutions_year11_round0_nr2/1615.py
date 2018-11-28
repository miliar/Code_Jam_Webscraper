#include <iostream>
#include <vector>

using namespace std;

struct node
{
    node(){}
    node(int a,int b):next(a),trans(b){}
    int next;
    int trans;
};

vector<node> comb[26];
vector<int> ops[26],ans;
int T,C,D,N;
int emt[200];

void solv()
{
    ans.push_back(emt[0]);
    for(int i=1;i<N;i++)
    {
        bool ck=true;
        int now=emt[i];
        if(comb[now].size())
        {
            for(int j=0;j<comb[now].size();j++)
            {
                if(ans.back()==comb[now][j].next)
                {
                    ans.pop_back();
                    ans.push_back(comb[now][j].trans);
                    ck=false;
                    break;
                }
            }
        }
        if(ck && ops[now].size())
        {
            for(int j=0;j<ops[now].size() && ck;j++)
            {
                for(int k=ans.size()-1;k>=0;k--)
                {
                    if(ans[k]==ops[now][j])
                    {
                        ans.clear();
                        ck=false;
                        break;
                    }
                }
            }
        }
        if(ck)ans.push_back(now);
    }
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    char tmp[3];
    cin>>T;
    for(int cnt=1;cnt<=T;cnt++)
    {
        for(int i=0;i<26;i++)
        {
            comb[i].clear();
            ops[i].clear();
        }
        ans.clear();
        cin>>C;
        for(int i=0;i<C;i++)
        {
            cin>>tmp[0]>>tmp[1]>>tmp[2];
            int a=tmp[0]-'A',b=tmp[1]-'A',c=tmp[2]-'A';
            comb[a].push_back(node(b,c));
            comb[b].push_back(node(a,c));
        }
        cin>>D;
        for(int i=0;i<D;i++)
        {
            cin>>tmp[0]>>tmp[1];
            int a=tmp[0]-'A',b=tmp[1]-'A';
            ops[a].push_back(b);
            ops[b].push_back(a);
        }
        cin>>N;
        for(int i=0;i<N;i++)
        {
            char tt;
            cin>>tt;
            emt[i]=tt-'A';
        }
        solv();
        cout<<"Case #"<<cnt<<": [";
        for(int i=0;i<ans.size();i++)
        {
            if(i)cout<<", ";
            cout<<(char)(ans[i]+'A');
        }
        cout<<"]"<<endl;
    }
    return 0;
}
