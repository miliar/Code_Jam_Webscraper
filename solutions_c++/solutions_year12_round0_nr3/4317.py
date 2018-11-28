// CJ.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int base[7] = {1,10,100,1000,10000,100000,1000000};
int a,b;
vector < pair<int,int> > T;

bool cmp(pair<int,int> x,pair<int,int> y)
{
     return ((x.first<y.first)||(x.first==y.first&&x.second<y.second));
}
int calc(int x)
{
     int num = x, c = 0, res = 0;
     while (num!=0)
           num/=10,c++;
     num = x;
     for (int i=0;i<c-1;++i)
     {
         int k = num%10;
		 num /= 10;
         num = k*base[c-1]+num;
         if (num>x&&num<=b)
         {
            res++;     
            T.push_back(make_pair(x,num));         
         }
     }
     return res;
}

int main ()
{
//    freopen("input.in","r",stdin);
//    freopen("output.out","w",stdout);
    int t,ans,p;
    cin >> t;
    for (int test=0;test<t;++test)
    {
          T.clear();
          cin >> a >> b;
          p = 0;
          for (int i=a;i<=b;++i)          
              p += calc(i);
          sort(T.begin(),T.end(),cmp);
          ans = p;
          for (int i=0;i<p;++i)
          {
              if (T[i].first == T[i+1].first && T[i].second == T[i+1].second)
                 ans--;
          }
          cout << "Case #" << test+1 << ": " << ans << endl;
    }
    return 0;
}

