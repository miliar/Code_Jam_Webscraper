#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <queue>
#include <cmath>
#include <cstdlib>
using namespace std;

        //My Macro's
#define FOR(i,n) for(int i=0;i<(int)n;i++)
#define FORN(i,st,end) for(int i=st;i<end;++i)
#define FORD(i,n) for(int i=(int)n;i>=0;i--)
#define SZ(n) ((int)n.size())
#define RET return
#define BTOE(a) a.begin(),a.end()
#define foreach(it,a) for(__typeof(a.begin()) it=a.begin();it!=a.end();++it)
#define BTOER(a) a.rbegin(),a.rend()
#define SORT(a) (sort(BTOE(a)))
#define PB push_back
#define SET(a,i) (memset(a,i,sizeof(a)))
       //End of Macro's
typedef vector<string> VS;
typedef vector<int> VI;
typedef stringstream SS;
typedef long long LL;
typedef map<string ,int > MPSI;
typedef map<int ,string > MPIS;
typedef pair<int ,int > PII;

//Helper Functions
string itos(int i)
{SS ss;ss<<i;return ss.str();}
int stoi(string s)
{SS ss;ss<<s;int i;ss>>i;return i;}
//End of helper function
char input[101];

struct NODE
{
    int dtime,atime;
    bool station;
    NODE(int d,int a,bool s)
    {
        dtime=d,atime=a,station=s;
    }    
};   


struct AVAIL
{
    int timing;
    bool station;
    AVAIL(int t,bool s)
    {
        timing=t,station=s;
    }    
};     

bool cmp(NODE a,NODE b)
{
    if(a.dtime!=b.dtime)
        RET a.dtime<b.dtime;
    RET a.atime<b.atime;
}    

bool cmp1(AVAIL a,AVAIL b)
{
    RET a.timing<b.timing;
}
    

int main()
{
    int test;
    cin>>test;
    gets(input);
    for(int tc=1;tc<=test;tc++)
    {
        int turn_time,NA,NB;
        VI ans(2,0);
        cin>>turn_time;
        vector<NODE> schedule;
        vector<AVAIL> available;
        gets(input);
        cin>>NA>>NB;
        gets(input);
        FOR(i,NA)
        {
            gets(input);
            SS ss(input);
            string first,second;
            ss>>first>>second;
            SS ss1(first),ss2(second);
            int ahr,amin,dhr,dmin;
            char colon;
            ss1>>dhr>>colon>>dmin;
            ss2>>ahr>>colon>>amin;
            NODE add((dhr*60)+dmin,(ahr*60)+amin+turn_time,0);
            schedule.PB(add);
        }    
        FOR(i,NB)
        {
            gets(input);
            SS ss(input);
            string first,second;
            ss>>first>>second;
            SS ss1(first),ss2(second);
            int ahr,amin,dhr,dmin;
            char colon;
            ss1>>dhr>>colon>>dmin;
            ss2>>ahr>>colon>>amin;
            NODE add((dhr*60)+dmin,(ahr*60)+amin+turn_time,1);
            schedule.PB(add);
        } 
        sort(schedule.begin(),schedule.end(),cmp);
        
        int schedule_ln=SZ(schedule);
        
        if(schedule_ln)
        {
            ans[schedule[0].station]++;
            AVAIL add(schedule[0].atime,(!(schedule[0].station)));
            available.PB(add);
            FORN(i,1,schedule_ln)
            {
                int avail_ln=SZ(available);
                sort(available.begin(),available.end(),cmp1);   
                bool flag=0;
                FOR(j,avail_ln)
                {
                    if((schedule[i].dtime>=available[j].timing)&&(schedule[i].station==available[j].station))
                    {
                        available.erase(available.begin()+j);
                        AVAIL add(schedule[i].atime,(!(schedule[i].station)));
                        flag=1;
                        available.PB(add);
                        break;
                    }    
                }
                if(!flag)
                {
                       ans[schedule[i].station]++;
                       AVAIL add(schedule[i].atime,(!(schedule[i].station)));
                       available.PB(add); 
                }             
            }    
        }    
        
        
        cout<<"Case #"<<tc<<": "<<ans[0]<<" "<<ans[1]<<endl;
    }    
    //system("PAUSE");
}
//Presto



