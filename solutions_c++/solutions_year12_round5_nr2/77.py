#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <cstring>
using namespace std;
typedef long long int lli;

ifstream cin("in.txt");
ofstream cout("out.txt");
int dx[]={0,0,-1,-1,1,1};
int dy[]={-1,1,-1,0,1,0};
int S,M;
bool m[1000][1000];
string getstr;
bool v[1000][1000];
int cc,ec;
set<int> ecs;
void dfs(int x,int y,bool flag)
{
    int by=max(x-S+1,1),ey=min(S+x,S*2)-1;
    if (x<1||x>S*2-1||y<by||y>ey||v[x][y]||((!m[x][y]&&flag)||(m[x][y]&&!flag))) return;
    v[x][y]=true;
    if (x==1||x==S*2-1||y==by||y==ey)
    {
        if ((x==1&&(y==by||y==ey))
            ||(x==S*2-1&&(y==by||y==ey))
            ||(x==S&&(y==by||y==ey)))
            cc++;
        else
        {
            if (x==1) ecs.insert(1);
            else if (x==S*2-1) ecs.insert(2);
            else if (x>S)
            {
                if (y==by) ecs.insert(3);
                else ecs.insert(4);
            }
            else if (x<S)
            {
                if (y==by) ecs.insert(5);
                else ecs.insert(6);
            }
        }
    }
    for (int i=0;i<6;i++)
        dfs(x+dx[i],y+dy[i],flag);
}
bool get(int x)
{
    memset(v,0,sizeof v);
    bool flag=false;
    bool r=false,b=false,f=false;
    string gs;
    for (int i=1;i<S*2;i++)
    {
        int bj=max(i-S+1,1),ej=min(S+i,S*2);
        for (int j=bj;j<ej;j++)
            if (!m[i][j])
            {
                if (!v[i][j])
                {
                    cc=0;
                    ec=0;
                    ecs.clear();
                    dfs(i,j,false);
                    ec=ecs.size();
                    if (cc==0&&ec==0)
                    {
                        r=true;
                        flag=true;
                    }
                }
            }
            else
            {
                if (!v[i][j])
                {
                    cc=0;
                    ec=0;
                    ecs.clear();
                    dfs(i,j,true);
                    ec=ecs.size();
                    if (cc>=2)
                    {
                        b=true;
                        flag=true;
                    }
                    if (ec>=3)
                    {
                        f=true;
                        flag=true;
                    }
                }
            }
    }
    if (b)
    {
        if (gs.length()!=0) gs+="-bridge";
        else gs+="bridge";
    }
    if (f)
    {
        if (gs.length()!=0) gs+="-fork";
        else gs+="fork";
    }
    if (r)
    {
        if (gs.length()!=0) gs+="-ring";
        else gs+="ring";
    }
    if (flag)
    {
        stringstream sout;
        sout<<gs<<" in move "<<x;
        getstr=sout.str();
        return true;
    }
    else return false;
}

int main()
{
    int T;
    cin>>T;
    for (int t=1;t<=T;t++)
    {
        cin>>S>>M;
        memset(m,0,sizeof m);
        getstr="none";
        bool flag=false;
        for (int i=1;i<=M;i++)
        {
            int x,y;
            cin>>x>>y;
            m[x][y]=true;
            if (!flag&&get(i)) flag=true;
        }
        cout<<"Case #"<<t<<": ";
        cout<<getstr;
        cout<<endl;
    }
}

