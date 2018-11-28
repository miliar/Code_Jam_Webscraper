#include<ctime>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include<cstring>
#include<locale>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define sz(a) (int((a).size()))
typedef istringstream iss; typedef ostringstream oss; typedef long long lli;
const double TOLL=1e-9;
const int size=513;
struct node
{
    int r,c,s;
    node(int rr,int cc,int ss)
    {
        r=rr; c=cc; s=ss;
    }

};
bool operator<(const node& a,const node& b)
{
    if(a.s!=b.s) return a.s>b.s;
    if(a.r!=b.r) return a.r<b.r;
    return a.c<b.c;
}
char grid[size][size];
int M,N;
int dr[]={0,0,1,-1};
int dc[]={1,-1,0,0};
bool possible(int r,int c,int s)
{
    for(int i=r;i<r+s;i++)
    {
        for(int j=c;j<c+s;j++)
        {
            char should='W';
            if(grid[i][j]=='W') should='B';
            if(grid[i][j]=='X') return false;
            for(int d=0;d<4;d++)
            {
                int nr=i+dr[d], nc=j+dc[d];
                if(nr>=i && nr<r+s && nc>=j && nc<c+s)
                {
                    if(grid[nr][nc]!=should) return false;
                }
            }

        }
    }
    return true;
}
map<int,int> mp;

bool getNew()
{
    vector<node> v;
    for(int i=0;i<M;i++)
        for(int j=0;j<N;j++) //optimize
        {
            for(int k=1;k<=min(N-j,M-i);k++) if(possible(i,j,k)) v.push_back(node(i,j,k));

        }
    //cerr<<"size of V:"<<sz(v)<<endl;
    if(sz(v)==0) return false;
    sort(all(v));
    int r=v[0].r, c=v[0].c, s=v[0].s;
    mp[s]++;
    for(int i=r;i<r+s;i++) for(int j=c;j<c+s;j++) grid[i][j]='X';
    return true;
}
string decode(char x)
{
    int n;
    if(isalpha(x)) n=(x-'A')+10;
    else n=x-'0';
    string rv="";
    while(n)
    {
        int t=n%2;
        char add='0';
        add=add+t;
        rv=rv+add;
        n/=2;
    }
    while(sz(rv)<4) rv=rv+"0";
    reverse(all(rv));
    return rv;
}

int main()
{

    int t; cin>>t;
    int cn=0;
    while(t--)
    {
        cn++;
        mp.clear();
        cin>>M>>N;
        string line;
        for(int i=0;i<M;i++)
        {
            cin>>line;
            string now="";
            for(int k=0;k<sz(line);k++)
            {
                string TEMP=decode(line[k]);
                now=now+TEMP;
                //cout<<"DEBUG ::"<<line<<' '<<TEMP<<' '<<now<<endl;
            }
            for(int k=0;k<sz(now);k++)
            {
                char a='W';
                if(now[k]=='0') a='B';
                grid[i][k]=a;
            }
            //cout<<"DEBUG "<<line<<' '<<now<<endl;

        } //input done;
        // Debug
        //cout<<"GRID"<<endl;
        /*for(int i=0;i<M;i++)
        {
            for(int j=0;j<N;j++) cout<<grid[i][j]<<' '; cout<<endl;
        }*/
        while(getNew());
        vector<pair<int,int> > rv;
        for(map<int,int>::iterator it=mp.begin();it!=mp.end();it++)
        {
            int a=it->first, b=it->second;
            rv.push_back(make_pair(a,b));
        }
        reverse(all(rv));
        printf("Case #%d: %d\n",cn,sz(rv));
        for(int i=0;i<sz(rv);i++) cout<<rv[i].first<<' '<<rv[i].second<<endl;

    }

    return 0;
}
