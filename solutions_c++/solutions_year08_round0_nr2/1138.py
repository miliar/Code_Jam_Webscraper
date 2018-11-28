#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <time.h>

using namespace std;

struct TT
{
       string arr;
       string dep;
       TT()
       {
           arr="";
           dep="";
       }
};

struct SortByValAsc
{
	bool operator()(const TT& p1, const TT& p2)
	{ return p1.arr < p2.arr;}
};


//sort(t.begin(),t.end(),SortByValAsc());
int turnAround;
vector<TT> A;
vector<TT> B;
vector<string> a_Status;
vector<string> b_Status;

TT t;
int TA;
int TB;
char nxt;

char findNxt()
{
     sort(A.begin(),A.end(),SortByValAsc());
     sort(B.begin(),B.end(),SortByValAsc());
     if(A.empty())
                  return 'b';
     if(B.empty())
                  return 'a';
     if(A[0].arr > B[0].arr )
                 return 'b';
     else
         return 'a';
}

void finish()
{    
     while( (!A.empty()) || (!B.empty()) )
     {
     nxt=findNxt();
     if(nxt=='a')
     {
                 string d=A[0].dep;
                 int h1, m1;
                 sscanf(d.c_str(), "%d:%d", &h1, &m1);
                 m1+=turnAround;
                 h1+=m1/60;
                 m1=m1%60;
                 if(h1 <= 23 )
                 {
                       stringstream ss;
                       string newStat="";
                       if(h1<10)
                                ss<<"0"<<h1<<":";
                       else
                           ss<<h1<<":";
                       
                       if(m1<10)
                                ss<<"0"<<m1;
                       else
                           ss<<m1;
                       
                       ss>>newStat;
                       b_Status.push_back(newStat);
                 }
                 
                 if(!a_Status.empty())
                 {
                                      sort(a_Status.begin(),a_Status.end());
                                      if( a_Status[0]<=A[0].arr )
                                          a_Status.erase(a_Status.begin(),a_Status.begin()+1);
                                      else
                                          TA++;
                 }
                 else
                     TA++;
                     
                 A.erase(A.begin(),A.begin()+1);
     }
     if(nxt=='b')
     {
                 string d=B[0].dep;
                 int h1, m1;
                 sscanf(d.c_str(), "%d:%d", &h1, &m1);
                 m1+=turnAround;
                 h1+=m1/60;
                 m1=m1%60;
                 if(h1 <= 23 )
                 {
                       stringstream ss;
                       string newStat="";
                       if(h1<10)
                                ss<<"0"<<h1<<":";
                       else
                           ss<<h1<<":";
                       
                       if(m1<10)
                                ss<<"0"<<m1;
                       else
                           ss<<m1;
                       
                       ss>>newStat;
                       a_Status.push_back(newStat);
                 }
                 
                 if(!b_Status.empty())
                 {
                                      sort(b_Status.begin(),b_Status.end());
                                      if( b_Status[0]<=B[0].arr )
                                          b_Status.erase(b_Status.begin(),b_Status.begin()+1);
                                      else
                                          TB++;
                 }
                 else
                     TB++;
                     
                 B.erase(B.begin(),B.begin()+1);
     }
     }
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("o.txt","w",stdout);
    TA=TB=0;
    
    int n;
    cin>>n;
    int a,b;
    for(int i=0;i<n;i++)
    {
            cin>>turnAround;
            cin>>a;
            cin>>b;
            for(int j=0;j<a;j++)
            {
                    cin>>t.arr;
                    cin>>t.dep;
                    A.push_back(t);
            }
            for(int j=0;j<b;j++)
            {
                    cin>>t.arr;
                    cin>>t.dep;
                    B.push_back(t);
            }
            
            finish();
            cout<<"Case #"<<i+1<<": "<<TA<<" "<<TB<<endl;
            TA=TB=0;
            A.erase(A.begin(),A.end());
            B.erase(B.begin(),B.end());
            a_Status.erase(a_Status.begin(),a_Status.end());
            b_Status.erase(b_Status.begin(),b_Status.end());
    }
           
    return 0;
}

/*
    string d="12:50";
    int h1, m1;
    sscanf(d.c_str(), "%d:%d", &h1, &m1);
    t.tm_hour=h1;
    t.tm_min=m1;
*/ 
