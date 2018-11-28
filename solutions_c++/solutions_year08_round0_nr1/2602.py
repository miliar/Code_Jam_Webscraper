#include<vector>
#include<conio.h>
#include<iostream>
#include<cmath>
#include<stack>
#include<fstream>

#define VS vector<string>
#define VVS vector<VS>

#define VI vector<int>
#define VVI vector<VI>


#define pb push_back
#define sz size()
#define itr iterator
#define all(x) x.begin(),x.end()

using namespace std;
VI chkStats(VI occ,int indx,bool& flag)
{
    VI tn;
    for(int i=0;i<occ.sz;i++)
     if(occ[i]==0)
      tn.pb(i);     
    if(tn.sz==1&&indx==tn[0])
    {
                flag=true;
                return occ;
    }
    ++occ[indx];
    return occ;
}   
int getMinSwitches(VS search,VS query)
{
    if(search.sz>query.sz)
     return 0;
    int count=0;
    VI occur;
    for(int i=0;i<search.sz;i++)
     occur.pb(0);
    for(int i=0;i<query.sz;i++)
    {
            int ind=find(all(search),query[i])-search.begin();
            bool stats=false;
            occur=chkStats(occur,ind,stats);
            if(stats==true)
            {
                           --i;
                           ++count;
                           for(int i=0;i<search.sz;i++)
                                   occur[i]=0;
                           continue;
            }
    }
    return count;
}
            
            
int main()
{
    fstream inp("A.in");
    if(!inp.is_open())
     cout<<"Error!";
    string tmpss;
    int nt;
    getline(inp,tmpss);
    nt=atoi(tmpss.c_str());
    VI nose,noq;
    VVS se,q;
    for(int i=0;i<nt;i++)
    {
            int tmpi;
            string tmps;
            getline(inp,tmps);
            tmpi=atoi(tmps.c_str());
            nose.pb(tmpi);
            VS t1,t2;
            for(int j=0;j<nose.back();j++)
            {
             getline(inp,tmps); 
             t1.pb(tmps);
            }
            se.pb(t1); 
            getline(inp,tmps);
            tmpi=atoi(tmps.c_str());
            noq.pb(tmpi);        
            for(int j=0;j<noq.back();j++)
            {
             getline(inp,tmps);
             t2.pb(tmps);
            }
            q.pb(t2);
    }
    inp.close();
    ofstream outp("A.out");
    for(int i=0;i<nt;i++)
     outp<<"Case #"<<i+1<<": "<<getMinSwitches(se[i],q[i])<<"\n"; 
    outp.close();
    getch();
    return 0;
}
