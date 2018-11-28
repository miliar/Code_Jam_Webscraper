#include<iostream>   
#include<cmath>   
#include<vector>   
#include<algorithm>   
#include<cstdio>   
#include<cstdlib>   
#include<string>   
#include<sstream>   
#include<map>   
#include<queue>   
#include<set>   
    
#define vi vector<int>   
#define vs vector<string>   
#define br break   
#define re return   
    
#define REP(i,n) for(int i=0;i<(int) n;i++)   
#define SZ size()   
#define INF (2<<29)   
#define DEBUG(x) cout<<#x<<": "<<x<<endl   
#define LL long long   
#define pb push_back   
    
using namespace std; 
string Search[101] , Query[1001];
int last[101];
map<string , int> Index;
int main()
{
    int kases;
    cin>>kases;
    int res ;
    for(int kase = 1 ; kase <= kases ; kase++)
    {
            Index.clear();
            int S;
            cin>>S;
            getline(cin , Search[0]);
            for(int i=0;i<S;i++)
            {
                    //cin>>Search[i]; 
                    getline(cin , Search[i]);
            }
            int Q;
            cin>>Q;
            getline(cin , Query[0]);
            for(int i = 0  ;i <Q ; i++)
            {
                    //cin>>Query[i];
                    getline(cin , Query[i]);
                    Index[Query[i]] = i;
            }
            res = 0;
            //for(int i=0;i<S;i++)
            //cout<<(Index.count(Search[i]))<<endl;
           // cout<<"here\n";
            int pos = 0;
            while(pos<Q)
            {
                   memset(last , -1 , sizeof(last));                       
                   for(int i = Q-1 ; i>=pos ; i--)
                   {
                           last[Index[Query[i]]] = i;
                   }
                   int best = -1;
                   for(int i = 0 ; i<S;i++)
                   {
                           if(!Index.count(Search[i])) { res++; goto Done;}
                           if(last[Index[Search[i]]]==-1){ res++; goto Done;}
                           best>?=last[Index[Search[i]]];
                   }
                   //cout<<"best : " <<best<<endl;
                   pos = best;
                   res++;
                   
            }
            Done:
                 if(Q!=0) res--;
            cout<<"Case #"<<kase<<": ";
            cout<<res<<endl; 
    }
}
