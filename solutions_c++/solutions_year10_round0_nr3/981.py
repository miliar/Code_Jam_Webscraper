#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cstdio>
using namespace std;


long long l_value[1000]={0};
long long l_next[1000]={0};

int circle[1000]={0};
long long l_res_cir[1000]={0};

long long my_deal(vector<long long>& vec_value,long long r,long long k,long long n)
{
    memset(l_value,0,sizeof(l_value));
    memset(l_next,0,sizeof(l_next));
    memset(circle,0,sizeof(circle));
    memset(l_res_cir,0,sizeof(l_res_cir));
    for(int i=0;i<n;i++)
    {
        int j=i;
        long long value=0;
        int time=0;
        while((value+vec_value[j]) <=k&&time < n)
        {
            value+=vec_value[j];
            j=(j+1)%n;
            time++;
        }
        l_value[i]=value;
        l_next[i]=j;
    }
    int n_circle=0;
    long long l_circle_value=0;
    long long l_result=0;
    int n_start=0;
    int i=1;
    for(;i<=r;i++)
    {
        if(circle[n_start]!=0)
        break;
        l_result+=l_value[n_start];
        circle[n_start]=i;
        n_start=l_next[n_start];
    }
    if(i>r)
       return l_result;
    else
       {
           int temp=1;
           n_circle=i-circle[n_start];
           int start_temp=n_start;
           for(;temp<=n_circle;temp++)
           {
                l_res_cir[temp]=l_res_cir[temp-1]+l_value[start_temp];
                start_temp=l_next[start_temp];
            }
            temp=r-i+1;
            l_result+=(temp/n_circle)*l_res_cir[n_circle];
            l_result+=l_res_cir[temp%n_circle];
          //  cout<<"i: "<<i<<"n_circle: "<<n_circle<<endl;
            return l_result;
        }

    return 0;
}
int main()
{
  ifstream in("a.in");
  ofstream out("a.out");

  long long t=0,r=0,k=0,n=0;
  in>>t;
  for(long long i=1;i<=t;i++)
  {
    in>>r>>k>>n;
    vector<long long> vec_value(n);
    for(long long j=0;j<n;j++)
       in>>vec_value[j];
    long long result=my_deal(vec_value,r,k,n);
    out<<"Case #"<<i<<": "<<result<<endl;
  }
    return 0;
}
