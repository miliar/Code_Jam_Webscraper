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

using namespace std;

int check(vector<int>total,vector<bool>arr)
{
    int seam=0,patrick=0,sum=0;
    for(int i=0;i<arr.size();i++)
    {
        if(arr[i])
        {
            patrick^=total[i];
            sum+=total[i];
        }
        else seam^=total[i];
    }
    if(seam==patrick) return sum;
    return 0;
}

int solve(vector<int>total,vector<bool>arr,int m,int n)
{
    if(m<arr.size())
    {
      int val=check(total,arr);
      if(val>0) return val;
      if(n<arr.size())
      {
          bool tmp;
          tmp=arr[n];arr[n]=arr[m];arr[m]=tmp;
          val=solve(total,arr,m,n+1);
          if(val>0) return val;
          tmp=arr[n];arr[n]=arr[m];arr[m]=tmp;
      }
      else
      {
          arr[m]=false;
          val=solve(total,arr,m+1,0);
          if(val>0) return val;
      }
    }
    return 0;
}
int main()
{
    freopen("Prob_C_Small.in","r",stdin);
    freopen("Prob_C_Small.out","w",stdout);
    //freopen("Prob_C_Large.in","r",stdin);
    //freopen("Prob_C_Large.out","w",stdout);
    int times,count=0;
    cin>>times;getchar();
    while(times--)
    {
        int candies,val;
        vector<int> total;vector<bool> arr;
        cin>>candies;
        for(int i=0;i<candies;i++){cin>>val;total.push_back(val);}
        sort(total.begin(),total.end());
        arr.push_back(false);
        for(int i=1;i<candies;i++) arr.push_back(true);
        val=solve(total,arr,0,1);
        cout<<"Case #"<<++count<<": ";
        if(val==0) cout<<"NO";
        else cout<<val;
        cout<<endl;
    }
    return 0;
}
