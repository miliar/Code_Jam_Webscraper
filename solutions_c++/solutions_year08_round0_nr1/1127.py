#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<fstream>

using namespace std;
int N,M;
vector<string> engines,queries;

int output()
{
    map<string,int> dp;
    dp.clear();
    int count=0;
    for(int i=0;i<N;i++)
    {
          dp.insert(make_pair(engines[i],i));
          //cout<<engines[i]<<"   "<<i<<"\n";
    }
    int start=0;
    while(1){
             if(start>=M-1)
               return count;
    vector<int> first(N,-1);
    for(int i=start;i<M;i++)
    {
            //cout<<queries[i]<<"   "<<dp[queries[i]]<<"\n";
            first[dp[queries[i]]]=min(i,first[dp[queries[i]]]);
            if(first[dp[queries[i]]]==-1)
              first[dp[queries[i]]]=i;
    }
    int i,change=first[0];
    for( i=0;i<N;i++)
    {
      if(first[i]==-1)
        return count;
      change=max(first[i],change);
    }
    start=change;
    count++;
}
}
    
               
    

int main()
{
    int t;
    
    ifstream fin("input.txt");
    ofstream fout("ans.txt");
    if(!fin)
    {
            cout<<"Wrong Location";
            cin>>t;
            exit(1);
    }
    fin>>t;
    
    int n=t;
    while(t--)
    {
              queries.clear();
              engines.clear();
              
              fin>>N;
              
              
              for(int i=0;i<N+1;i++)
              {
                      fin.clear();
                      char temp[110];
                      string s;      
                      getline(fin,s);
                      if(i==0)
                       continue;
                      engines.push_back(s);
                      //cout<<i<<"   "<<s<<"\n";
                      
                     
              }
              
              fin>>M;
//              fin>>s1;
              for(int i=0;i<M+1;i++)
              {
                     
                      fin.clear();
                      char temp[110];
                      string s;
                      getline(fin,s);
                      if(i==0)
                         continue;
                      queries.push_back(s);
                      //cout<<i<<"   "<<s<<"\n";
              }
              fout<<"Case #"<<n-t<<": "<<output()<<"\n";
              
    }
    cin>>t;
}              
