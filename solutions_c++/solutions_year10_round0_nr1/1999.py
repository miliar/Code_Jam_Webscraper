/* Author: Piyush Sachdeva */

#include<iostream>
#include<vector>
#include<cmath>
#include<time.h>
#include<fstream>
#include<queue>
#include<stack>
#include<utility>
#include<stdlib.h>
#include<string.h>
#include<set>
#include<list>
#include<map>
#include<algorithm>
#include <sstream>
#include <unistd.h>

#define GI ({int t;scanf("%d",&t);t;})
#define forn(i,n) for(int i=0;i<n;i++)
#define forab(i,a,b) for(int i=a;i<b;i++)
#define pb(t) push_back(t)
#define pq priority_queue
#define mp(t1,t2) make_pair(t1,t2)
#define vi vector<int>
#define pii pair<int,int>
#define vpii vector<pair<int,int> >

#define INF INT_MAX
#define ep 0.00000001

#define dbg(x) cout << #x << " -> " << (x) << "\t";
#define dbge(x) cout << #x << " -> " << (x) << "\n";

using namespace std;

bool power[30];
bool state[30];

int main()
{
    clock_t start=clock();
    ifstream fin("Alarge.in");
    ofstream fout("Aloutput.txt");
    
    int T;
    
    fin>>T;
    int n,k;
    
    int temp;
    bool fl;
    
    forn(t,T)
    {
             fin>>n>>k;
             
             temp=(int)pow((float)2,(float)n);
             temp--;
             
             float ans=(((float)(k-temp))/(float)(temp+1));
             
             if(ans<floor(ans)+ep&&ans>floor(ans)-ep)
                                                     fl=true;
             else
                 fl=false;
             
             fout<<"Case #"<<t+1<<": ";
             if(fl)
                   fout<<"ON"<<endl;
             else
                 fout<<"OFF"<<endl;
    }
    /*forn(t,T)
    {
            fin>>n>>k; 
            
            memset(power,0,sizeof(power));
            memset(state,0,sizeof(state));
            power[0]=1;
            
            while(k--)
            {
                      forn(i,n)
                      {
                               if(power[i]==0)
                               {
                                            break;
                               }
                               else
                               {
                                   if(state[i]==0)
                                                  state[i]=1;
                                   else
                                                  state[i]=0;
                               }
                      }
                      
                      power[0]=1;
                      forab(i,1,n)
                      {
                                  if(power[i-1]==1&&state[i-1]==1)
                                                                  power[i]=1;
                                  else
                                                                  power[i]=0;
                      }
            }
            
            
            cout<<"Case #"<<t+1<<": ";
            
            if(power[n-1]==1&&state[n-1]==1)
                                            cout<<"ON"<<endl;
            else
                                            cout<<"OFF"<<endl;
    }*/
    printf("Time : %f\n",((double)clock()-start)/CLOCKS_PER_SEC);
    system("pause");
    return 0;
}
