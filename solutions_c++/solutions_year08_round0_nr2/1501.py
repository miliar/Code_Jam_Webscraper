#include <iostream>
#include <cstdlib>
#include<vector>
#include<cstdio>
#include<algorithm>
using namespace std;


int main()
{
    freopen("D:/petio's/new.txt","w",stdout);
    freopen("D:/petio's/input.txt","r",stdin);
    int n;
    cin>>n;
    for(int x=0;x<n;x++)
    {
            int turn;
            cin>>turn;
            int p,q;
            cin>>p>>q;
            vector<pair<int,int> > v;
            for(int i=0;i<p;i++)
            {
               int a,b,c,d;
               char temp[100];
               gets(temp);
               a=temp[0]-'0';
               b=temp[1]-'0';
               c=temp[3]-'0';
               d=temp[4]-'0';
               int temp1=(a*10+b)*60+c*10+d;
               v.push_back(make_pair(temp1,1));
               a=temp[6]-'0';
               b=temp[7]-'0';
               c=temp[9]-'0';
               d=temp[10]-'0';
               temp1=(a*10+b)*60+c*10+d+turn;
               v.push_back(make_pair(temp1,-1));
            }
            for(int i=0;i<q;i++)
            {
               int a,b,c,d;
               char temp[100];
               gets(temp);
               a=temp[0]-'0';
               b=temp[1]-'0';
               c=temp[3]-'0';
               d=temp[4]-'0';
               int temp1=(a*10+b)*60+c*10+d;
               v.push_back(make_pair(temp1,2));
               a=temp[6]-'0';
               b=temp[7]-'0';
               c=temp[9]-'0';
               d=temp[10]-'0';
               temp1=(a*10+b)*60+c*10+d+turn;
               v.push_back(make_pair(temp1,-2));

            }
            sort(v.begin(),v.end());
            //for(int i=0;i<2*(p+q);i++)
            //   cout<<v[i].first<<" "<<v[i].second<<"\n";
            int a1=0,b1=0,c1=0,d1=0;
            for(int i=0;i<2*(p+q);i++)
            {
                if(v[i].second==1)
                     if(!a1)
                        c1++;
                     else
                        a1--;
                else if(v[i].second==2)
                    if(!b1)
                       d1++;
                    else
                       b1--;
               else if(v[i].second==-1)
                    b1++;
               else
                    a1++;
             }
             cout << "Case #" << x+1 << ": " <<c1<<" "<<d1<<"\n";
       }
      //system("PAUSE");
      return 0;
}
