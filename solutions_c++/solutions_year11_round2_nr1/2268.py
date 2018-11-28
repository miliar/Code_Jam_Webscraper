#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <cstring>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define FOR( i,a,b ) for(int i=a;i<b;i++)
#define NS string::npos
#define VI vector <int>
#define sz size
#define PI <int ,int >
#define CLEAR(cab) memset(cab,0,sizeof cab)
using namespace std;

int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
   int test;
   string s;
   int n;
   int tot,count;
   int avg1;
   int q=0;
   vector<double> wp1,owp1,oowp1;
    double rpi,owp;
   cin>>test;
    int i,j,k,avg;
   vector<string > v;
   while(test--)
   {
q++;
       v.clear();
       cin>>n;
       wp1.clear();
       owp1.clear();
       oowp1.clear();
       wp1.resize(n);
       owp1.resize(n);
       oowp1.resize(n);
       cin.ignore();
       for(i=0;i<n;i++)
       {
        getline(cin,s,'\n');
        v.push_back(s);
       }
       for( i=0;i<n;i++)
       {
           s=v[i];
           tot=0;
           count=0;
           for( j=0;j<n;j++)
           {
               if(v[i][j]!='.')
               {
                   tot++;
                   if(v[i][j]=='1')
                   count++;
               }
           }
           wp1[i]=(double)count/tot;

           owp=0;
           avg=0;
        }

        for( i=0;i<n;i++)
        {
            owp=0;
            avg=0;
        for(j=0;j<n;j++)
        {
            if(v[i][j]=='.')
            continue;
               tot=0;
               count=0;
               avg++;
               for(k=0;k<n;k++)
               {

                   if(k==i)
                   continue;
                   if(v[j][k]!='.')
                   {
                       tot++;
                       if(v[j][k]=='1')
                       count++;
                   }
               }

            owp=owp+(double)count/tot;
        }
           owp=owp/(double)(avg);
           owp1[i]=owp;


        }

        for(i=0;i<n;i++)
        {
            oowp1[i]=0;
            avg=0;
            for(j=0;j<n;j++)
           {

                if(v[i][j]=='.')
                {
                    continue;
                }
                oowp1[i]+=owp1[j];
                avg++;

           }
           oowp1[i]/=(double)avg;

        }
printf("Case #%d:\n",q);
for(int i=0;i<n;i++)
{
    double x;
    x=0.25*wp1[i]+0.5*owp1[i]+0.25*oowp1[i];
    printf("%.12lf\n",x);
}

   }




return 0;
}


