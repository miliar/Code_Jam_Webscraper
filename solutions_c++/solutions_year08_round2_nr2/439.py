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
#include<queue>
using namespace std;
int PP;
int prime(int a)
{
    for(int i=2;i*i<=a;i++)
      if(a%i==0)
        return 0;
    return true;
}
int get(int a,int b)
{
    int gcde=__gcd(a,b);
    int n1=gcde;
    while(n1>=0&&gcde%n1==0)
    {
               if(prime(n1)&&gcde%n1==0)
                  return n1;
               
               n1++;
               
                 
    }
    return -100;
                  
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
           int A,B,P;
           fin>>A>>B>>P;
           PP=P;
           vector<bool> used(B-A+1,false);
           queue<int> total;
           for(int i=A;i<=B;i++)
              total.push(i);
           int count=0;
           while(!total.empty())
           {
                int now=total.front();
                total.pop();
                if(used[now-A]!=false)
                  continue;
                //used[now-A]=true;
                queue<int> thisp;
                thisp.push(now);
                while(!thisp.empty()){
                                      int now1=thisp.front();
                                      thisp.pop();
                                      if(used[now1-A])
                                        continue;
                                      used[now1-A]=true;
                for(int i=A;i<=B;i++)
                {
                        if(!used[i-A])
                        {
                                      int n1=now1;
                                      int n2=i;
                                      int pr=get(now1,i);
                                      if(pr>=P)
                                        thisp.push(i);
                        }
                }
                }
                count++;
           }
           fout<<"Case #"<<n-t<<": "<<count<<"\n";
           }
           cin>>t;                             
           
                   
}
