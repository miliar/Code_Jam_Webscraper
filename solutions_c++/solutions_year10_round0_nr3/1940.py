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

int a[1001];
long long sum[1001];
long long end[1001];

int main()
{
    clock_t start=clock();
    ifstream fin("input.in");
    ofstream fout("output.txt");
    
    //fout<<LONG_LONG_MAX<<endl;
    
    int T,R,k,N;
    fin>>T;
    
    forn(t,T)
    {
             fin>>R>>k>>N;
             forn(i,N)
                      fin>>a[i];
                      
             memset(sum,0,sizeof(sum));
             memset(end,-1,sizeof(end));
             
             long long temp;
             int counter;
             
             //bool dnc=false;
             
             forn(i,N)
             {
                      counter=i;
                      temp=a[i];
                      counter++;
                      if(counter==N)
                                    counter=0;
                                    
                      while(counter!=i)
                      {
                              if(temp+a[counter]>k)
                              {
                                                   end[i]=counter;
                                                   break;
                              }
                              temp+=a[counter];
                              counter++;
                              if(counter==N)
                                            counter=0;
                      }
                      
                      
                      sum[i]=temp;
             }
             
             long long result=0;
             
             if(end[0]==-1)
             {
                    result=R*sum[0];
                    goto done;
             }
             //int counter=0;
             int start;
             
             counter=0;
             
             while(R--)
             {
                       result+=sum[counter];                    
                       
                       counter=end[counter];
             }
             /*while(R--)
             {
                       temp=0;
                       start=counter;
                       while(temp+a[counter]<=k)
                       {
                              temp+=a[counter];
                              result+=a[counter];
                              
                              counter++;
                              if(counter==N)
                                            counter=0;
                              if(counter==start)
                                                break;
                       }
             }*/
             done:;
             fout<<"Case #"<<t+1<<": "<<result<<endl;
    }
    printf("Time : %f\n",((double)clock()-start)/CLOCKS_PER_SEC);
    system("pause");
    return 0;
}
