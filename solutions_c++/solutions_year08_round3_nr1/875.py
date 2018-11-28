#include<vector>

#include<iostream>
#include<cmath>
#include<fstream>
#include<stack>

#define VS vector<string>
#define VVS vector<VS>
#define VF vector<float>
#define VVF vector<VF>
#define VD vector<double>
#define VVD vector<VD>
#define VI vector<int>
#define VVI vector<VI>
#define LI long int

#define VLI vector<LI>
#define VVLI vector<VLI>
#define LLI long long int
#define VLLI vector<LLI>
#define VVLLI vector<VLLI>

#define SC stack<char>
#define SI stack<int>
#define SLI stack<LI>
#define SLLI stack<LLI>
#define SS stack<string>
#define SF stack<float>
#define SD stack<double>

#define INF 100000000


#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define itr iterator
#define all(x) x.begin(),x.end()

#define WATCH(x) {cout<<"WATCHING:"<<#x<<":";for(int i=0;i<x.size();i++){cout<<x[i]<<"..";}}
#define WATCHSTK(x,y) {cout<<"WATCHING:"<<#x<<":";stack<typeof(x.top())> y;y=x;for(int i=0;i<x.size();i++){cout<<y.top()<<"..";y.pop()}}
#define PEEK(x) {cout<<#x<<"="<<x;}

#define GI ({int t;scanf("%d",&t);t;})
#define GS ({char buff[1000];scanf("%s",buff);string a=buff;a;})
using namespace std;
int xfind(vector<int> a,int b)
{
    for(int i=0;i<a.size();i++)
     if(a[i]==b)
      return i;
    return -1;
}
int getMinPress(int maxlet,int nokey,int noalp,VI freq)
{
    VI indx,orig;
    orig=freq;
    sort(all(freq));
    reverse(all(freq));
    for(int i=0;i<freq.sz;i++)
            indx.pb(xfind(orig,freq[i]));
    int press=0,i=0;
 int flag=0;
            for(int j=0;j<maxlet;j++)
            {
             PEEK(j);
             for(int k=0;k<nokey;k++)
             {
                   PEEK(k);
                   PEEK(freq[i]);
                   press+=freq[i]*(j+1);
                   PEEK(press);
                   ++i;
                   if(i==freq.sz)
                   {
                    ++flag;
                    break;
                   }
                  // getch();
             }  
             if(flag)
              break;
            }
   return press;
                     
            
}
int main()
{
    fstream inp("a.in");
    if(!inp.is_open())
     cout<<"Error!";
    string tmpss;
    int nt;
    getline(inp,tmpss);
    nt=atoi(tmpss.c_str());
 
    int tmpa,tmpb,tmpc;
    VI maxlet,nokeys,noalpha;
    VVI freq;
    for(int i=0;i<nt;i++)
    {
            int tmpi;
            string tmps;
            getline(inp,tmps);
            sscanf(tmps.c_str(),"%d %d %d",&tmpa,&tmpb,&tmpc);
            PEEK(tmpa);
            PEEK(tmpb);
            PEEK(tmpc);
            maxlet.pb(tmpa);
            nokeys.pb(tmpb);
            noalpha.pb(tmpc);
            VI tmpv;
            for(int j=0;j<noalpha.back();j++)
            {

             inp>>tmpi;
             tmpv.pb(tmpi);
 
            }
            getline(inp,tmps);
            freq.pb(tmpv);
            WATCH(tmpv);
    }
    WATCH(maxlet);
    WATCH(nokeys);
    WATCH(noalpha);
    inp.close();
    ofstream outp("answer.out");
    for(int i=0;i<nt;i++)
     outp<<"Case #"<<i+1<<": "<<getMinPress(maxlet[i],nokeys[i],noalpha[i],freq[i])<<"\n"; 
    outp.close();
   
    return 0;
}
            
    
    
    
    
    
    
 
