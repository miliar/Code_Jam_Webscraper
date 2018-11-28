#include <iostream>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <boost/algorithm/string.hpp>
#include <boost/lexical_cast.hpp>
#include <map>
#include <algorithm>
#include <stdint.h>

#define foreach(variable,list) for(uint64_t variable=0;variable<list.size();variable++)

using namespace std;

inline uint64_t power(uint64_t x,uint64_t n)
{
uint64_t result=1;
for(int i=0;i<n;i++) result*=x;
return result;
}

bool solve(vector<uint64_t>& set,vector<uint64_t>& r1,vector<uint64_t>& r2)
{

int N=20;
uint64_t firstNUM=power(2,N);
vector<uint64_t> r; 
uint64_t total=0;
for(int i=0;i<N;i++) total+=set[i];

for(uint64_t i=0;i<firstNUM;i++)
{
//cout<<i<<endl;
r1.resize(0);
r.resize(0);
r2.resize(0);
uint64_t sum1=0;

for(int j=0;j<N;j++)
    if ((i>>j)%2==1)
        {
        r1.push_back(set[j]);
        sum1+=set[j];
        }
     else
     {
        r.push_back(set[j]);      
     }
if (sum1*2>total) continue;

uint64_t secNUM=power(2,r.size());
uint64_t sum2=0;

for(uint64_t k=0;k<secNUM;k++)
{
r2.resize(0);
sum2=0;
for(int j=0;j<r.size();j++)
    if ((k>>j)%2==1)
        {
        sum2+=r[j];
        r2.push_back(r[j]);
        if (sum2==sum1 && r1.size()>0) return true;
        }
}

}


return false;
}


int main()
{
    uint64_t end;string tmp;
    cin>>end;
    for(uint64_t problem=0; problem<end; problem++)
    {
        uint64_t N,t;
        vector<uint64_t> set,result1,result2;
        cin>>N;
        for(uint64_t i=0;i<N;i++)
        {
        cin>>t;
        set.push_back(t);

        }
        if (solve(set,result1,result2))
            {
            cout<<"Case #"<<(problem+1)<<":"<<endl;
            for(uint64_t i=0;i<result1.size();i++)
                {
                cout<<result1[i]<<" ";
                if (i!=result2.size()-1) cout<<" ";
                }
            cout<<endl;
            for(uint64_t i=0;i<result2.size();i++)
                            {
                cout<<result2[i];
                if (i!=result2.size()-1) cout<<" ";
                }
            cout<<endl;            
            }
            else
            {
            cout<<"Case #"<<(problem+1)<<": Impossible"<<endl;
            }
            
    }

    return 0;
}

