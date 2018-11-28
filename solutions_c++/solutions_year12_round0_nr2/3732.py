#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>

bool cmp(const int cmp1,const int cmp2){
     return cmp1>cmp2;
}

int main()
{
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
    int t;
    std::cin>>t;
    for(int i=0;i<t;i++)
    {
        int n,s,p;
        std::vector<int> v;
        std::cin>>n>>s>>p;
        for(int j=0;j<n;j++)
        {
            int tmp;
            std::cin>>tmp;
            v.push_back(tmp);
        }
        int cnt=0;
        std::sort(v.begin(),v.end(),cmp);
        for(int j=0;j<v.size();j++)
        {
            int tmp=v[j];
            if (v[j]==0) 
            {
                if (p==0)
                {
                    cnt++;
                }
                continue;
            }
            if (3*p<=v[j]+2) cnt++;
            else if(3*p>v[j]+2 && (v[j]+4)/3==p)
            {
                if (s==0) break;
                cnt++;
                s--;
            }
            else break;
        }
        std::cout<<"Case #"<<i+1<<": "<<cnt<<std::endl;
    }
}