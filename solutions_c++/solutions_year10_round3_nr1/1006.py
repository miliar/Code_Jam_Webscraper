#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<cstdlib>
#include<cmath>
#include<stack>
#include<string>
#include<cstdio>
using namespace std;

struct hit
{
    int A,B;
};
int main()
{
    int test,i,j,n,k,kase=0;

    freopen("A.in","r",stdin);
    freopen("Aout.txt","w",stdout);
    cin>>test;
    hit temp;
    vector<hit>v;
    while(test--)
    {
        cin>>n;


            v.clear();
           int cnt=0;

          while(n--)
          {  cin>>temp.A>>temp.B;
            v.push_back(temp);
            for(i=0;i<v.size()-1;i++)
            {
                if((v[i].A > temp.A && v[i].B < temp.B)||(v[i].A <  temp.A  && v[i].B > temp.B))
                    cnt++;
            }
          }
            cout<<"Case #"<<++kase<<": "<<cnt<<endl;

    }

    return 0;
}
