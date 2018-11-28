#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int case_number;
#define gout case_number++, printf("Case #%d: ",case_number), cout
#define F(i,n) for((i)=0;(i)<(n);(i)++)
int N;

int getnum(vector <int> x)
{
    int i,k=0,num=0,s = x.size();
    
    while(k<s)
           k = x[k]-1;   
    if(x[s-1]==N)
    {
                 if(k==x[s-1]-1)            return 1;
                 else                       return 0;
    }
    //cout<<k;
    if(k==x[s-1]-1 && (N - x[s-1]  < x[s-1] - s))
    {
         //cout<<"Returning:"<<s<<" "<<x[s-1]<<endl;
         return 0;

    }
    for(i=x[s-1]+1;i<=N;i++)
    {
                           x.push_back(i);
                           num=(num + getnum(x))%100003;
                           x.pop_back();
    }
    //cout<<"Returning num"<<num<<endl;
    return num%100003;
}
void repeat()
{
     int i,num=0;
     cin>>N;
     F(i,N-1)
     {
           vector <int> x;
           x.push_back(i+2);
           num = (num +getnum(x))%100003;
     }
     gout<<num%100003<<endl;
}

int main(int argc, char *argv[])
{
    int i,T;
    case_number = 0;
    cin>>T;
    F(i,T)
          repeat();
}
