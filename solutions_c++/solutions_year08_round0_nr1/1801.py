#include<iostream>
#include<cstdio>
#include<fstream>
#include<string>
#include<vector>
#include<istream>
#include<map>
#define M 10000
using namespace std;
int main()
{
    freopen("A-small-attempt4(1).in","r",stdin);freopen("out.txt","w",stdout);
    //i fin("google.in");
    //ofstream fout("A-small-attempt0.out");
    int n;
    cin>>n;
    //cout<<n<<endl;
    vector<string>query;
    vector<string>engine;
    map<string,int>p;
    map<string,int>::iterator iter;
    int num[M];
    int v[M];
    int x=0;
    for(int i=0;i<n;i++)
    {
        int m;
        cin>>m;
        getchar();
        //cout<<m<<endl;
        query.clear();
        engine.clear();
        memset(num,0,sizeof(num));
        p.clear();
        char b[M];
        string a;
        for(int j=0;j<m;j++)
        {
            gets(b);
            a=b;
            //cout<<a<<endl;
            engine.push_back(a);
            p[a]=j;
        }
        sort(engine.begin(),engine.end());
        int mm;
        cin>>mm;
        //cout<<mm<<endl;
        getchar();
        for(int j=0;j<mm;j++)
        {
            gets(b);
            a=b;
            //cout<<a<<endl;
            query.push_back(a);
            iter=p.find(a);
            if(iter!=p.end())
            {
                num[j]=iter->second;
            }
        }
        memset(v,0,sizeof(v));
        int time=0;
        x=0;
        for(int j=0;j<mm;j++)
        {
            if(!v[num[j]])
            {
                x++;
                if(x==m)
                {
                   // cout<<x<<" "<<j<<endl;
                    time++;
                    x=1;
                    memset(v,0,sizeof(v));
                }
                v[num[j]]=1;
            }
        }
        cout<<"Case #"<<i+1<<": "<<time<<endl; 
    }
}
