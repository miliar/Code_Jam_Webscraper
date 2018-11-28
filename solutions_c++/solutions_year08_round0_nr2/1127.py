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

vector<int> A,B;
vector<int> leaveA,reachedB,leaveB,reachedA;

bool availA(int time)
{
    int sum=0;
    for(int i=0;i<leaveA.size();i++)
     {
            if(leaveA[i]<=time)
               sum--;
     }
     for(int i=0;i<reachedA.size();i++)
       if(reachedA[i]<=time)
          sum++;
     for(int i=0;i<A.size();i++)
      if(A[i]<=time)
        sum++;
     if(sum>=0)
       return true;
     return false;
}

bool availB(int time)
{
    int sum=0;
    for(int i=0;i<leaveB.size();i++)
     {
            if(leaveB[i]<=time)
               sum--;
     }
     for(int i=0;i<reachedB.size();i++)
       if(reachedB[i]<=time)
          sum++;
     for(int i=0;i<B.size();i++)
      if(B[i]<=time)
        sum++;
     if(sum>=0)
       return true;
     return false;
}

int solve()
{
    int i,j;
    for( i=0,j=0;i<leaveA.size()&&j<leaveB.size();)
    {
            if(leaveA[i]<leaveB[j])
            {
              if(!availA(leaveA[i]))
              {
                 A.push_back(leaveA[i]);
               //  i++;
              }
              else
              i++;
            }
            else
            {
                if(!availB(leaveB[j]))
                {
                   B.push_back(leaveB[j]);
             //      j++;
                }
                else j++;
            }
    }
    if(i==leaveA.size())
    {
       for(int k=j;k<leaveB.size();)
          if(!availB(leaveB[k]))
           {
              B.push_back(leaveB[k]);
              //k++;     
           }
           else k++;
    }
    else
    {
      for(int k=i;k<leaveA.size();)
       if(!availA(leaveA[k]))
       {
           A.push_back(leaveA[k]);
           //k++;      
       }
       else
       k++;
       
    }
}
int main()
{
    int t;
    int n;
    ifstream fin("input.txt");
    ofstream fout("ans.txt");
    if(!fin)
    {
            cout<<"Wrong file";
            cin>>t;
            exit(0);
    }
    fin>>t;
    n=t;
    while(t--)
    {
              A.clear();
              B.clear();
              leaveA.clear();
              reachedB.clear();
              leaveB.clear();
              reachedA.clear();
              int turn;
              fin>>turn;
              int N,M;
              fin>>N>>M;
              for(int i=0;i<N;i++)
              {
                      int data;
                      string s;
                      
                      fin>>s;
                      data=((s[0]-'0')*10+(s[1]-'0'))*60+(s[3]-'0')*10+s[4]-'0';
                      //cout<<s<<"   ";
                      //cout<<s[1]-'0'<<"\n";
                      leaveA.push_back(data);
                      fin>>s;
                      data=((s[0]-'0')*10+(s[1]-'0'))*60+(s[3]-'0')*10+s[4]-'0';
                      //cout<<s<<"\n";
                      reachedB.push_back(data+turn);
              }
              for(int i=0;i<M;i++)
              {
                      int data;
                      string s;
                      fin>>s;
                      data=((s[0]-'0')*10+(s[1]-'0'))*60+(s[3]-'0')*10+s[4]-'0';
                      //cout<<s<<"  ";
                      leaveB.push_back(data);
                      fin>>s;
                      data=((s[0]-'0')*10+(s[1]-'0'))*60+(s[3]-'0')*10+s[4]-'0';
                      //cout<<s<<"\n";
                      reachedA.push_back(data+turn);
              }
              for(int i=0;i<N;i++)
              {
                      int leastindex=i;
                      for(int j=i+1;j<N;j++)
                      if(leaveA[leastindex]>leaveA[j])
                        leastindex=j;
                      swap(leaveA[leastindex],leaveA[i]);
                      swap(reachedB[leastindex],reachedB[i]);
              }
              for(int i=0;i<M;i++)
              {
                      int leastindex=i;
                      for(int j=i+1;j<M;j++)
                      if(leaveB[leastindex]>leaveB[j])
                        leastindex=j;
                      swap(leaveB[leastindex],leaveB[i]);
                      swap(reachedA[leastindex],reachedA[i]);
              }
              solve(); 
              fout<<"Case #"<<n-t<<": "<<A.size()<<" "<<B.size()<<"\n";
              
    }
    cin>>t;
}
