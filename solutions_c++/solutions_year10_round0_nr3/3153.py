#include <iostream>
#include <cmath>
#include <vector>
#include <functional>
#include <algorithm>
#include <queue>
using namespace std;

int main()
{
freopen("C-small.in","r",stdin);
freopen("c-small.out","w",stdout);
long t,r,k,n,c=0;
cin>>t;
while(t--)
    {
    c++;
    long resp=0,aux;
    cin>>r>>k>>n;
    vector<long> v1;
    deque<long> q1;
    deque<long> q2;
    for(long i=0;i<n;i++)
        {cin>>aux;
        v1.push_back(aux);}
    while(r--)
        {
        long sum=0;
        bool flag=false;
        for(long i=0;i<v1.size();i++)
            {
            if(sum+v1[i]<=k && flag==false)
                {sum=sum+v1[i];
                q1.push_back(v1[i]);}
            else
                {
                q2.push_back(v1[i]);
                flag=true;
                continue;
                }
            }
        resp=resp+sum;
        long aux2=q2.size();
        for(int i=0;i<aux2;i++)
            {
            v1[i]=q2.front();
            q2.pop_front();
            }
        for(int j=aux2;j<v1.size();j++)
            {
            v1[j]=q1.front();
            q1.pop_front();
            }
        }
    v1.clear();
    q1.clear();
    q2.clear();
    printf("Case #%d: %d\n",c,resp);
    }
return 0;
}
