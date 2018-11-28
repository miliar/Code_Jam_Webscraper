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
//int SA[101] , FA[101] , SB[101] , FB[101];
int conv(string s)
{
    int res = 0;
    res += (s[3]-'0')*10 + s[4]-'0';
    res += ((s[0]-'0')*10 + s[1]-'0')*60;
    return res;
}
bool markA[101] , markB[101];
vector<pair <int , int> > SA , SB;
int PA , PB;
int T;
void solve(int next)
{
   /* for(int i= 0  ;i <SA.size() ; i++)
            {
                 cout<<SA[i].first<< " " <<SA[i].second<<endl;
                    
            }
            for(int i= 0  ;i <SB.size() ; i++)
            {
                 cout<<SB[i].first<< " " <<SB[i].second<<endl;
                    
            } 
    cout<<next<<endl;
    getchar();getchar(); 
    */
    int timer  = 0;
    while(true)
    { 
      if(next==0)
      {
           bool found = false;      
           for(int i = PA ; i<SA.size() ; i++)
           {
                   if(SA[i].first>=timer)
                   {
                         timer  = T + SA[i].second;             
                         PA = i+1;   
                         markA[i] = true;          
                         found = true;
                         break;             
                   }
           }      
           if(!found) return ;
      }
      else
      {
          bool found = false;   
          for(int i = PB ; i<SB.size() ; i++)
           {
                   if(SB[i].first>=timer)
                   {
                         timer  = T + SB[i].second;             
                         PB = i+1; 
                         markB[i] = true;           
                         found = true;
                         break;             
                   }
           }
           if(!found) return ; 
      }
      next = 1-next;
    }
}
int main()
{
    string s;;
    int kases;
    cin>>kases;
    for(int kase=1;kase<=kases;kase++)
    {
            
            int A , B;
            
            A = B = 0;
           
            cin>>T;
            int NA , NB;
            cin>>NA>>NB;
            SA.resize(NA);
            SB.resize(NB);

            REP(i,NA)
            {
                     cin>>s;
                     SA[i].first = conv(s);
                     cin>>s;
                     SA[i].second = conv(s);
            }
            REP(i,NB)
            {
                     cin>>s;
                     SB[i].first = conv(s);
                     cin>>s;
                     SB[i].second = conv(s);
            }
            //solve
            sort(SA.begin() , SA.end());
            sort(SB.begin() , SB.end());
            /*
            for(int i= 0  ;i <SA.size() ; i++)
            {
                 cout<<SA[i].first<< " " <<SA[i].second<<endl;
                    
            }
            for(int i= 0  ;i <SB.size() ; i++)
            {
                 cout<<SB[i].first<< " " <<SB[i].second<<endl;
                    
            }
            */
            while(SA.size() + SB.size())
            {
                 int next;           
                 if(SA.size()==0) next = 1;
                 else if(SB.size()==0) next = 0;
                 else
                 {
                     if(SA[0].first<=SB[0].first) next = 0;
                     else next = 1;
                 }
                 if(next) B++;
                 else A++;
                 PA = 0 , PB = 0;
                 REP(i,SA.size()) markA[i] = 0;
                 REP(i,SB.size()) markB[i] = 0;
                 solve(next);
                 for(int i = SA.size()-1;i>=0;i--) if(markA[i]) SA.erase(SA.begin() + i);
                 for(int i = SB.size()-1;i>=0;i--) if(markB[i]) SB.erase(SB.begin() + i);
            }
            
            
            cout<<"Case #"<<kase<<": ";
            cout<<A<<" "<<B<<endl;
    }
}

