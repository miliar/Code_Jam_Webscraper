#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;
queue<long>q;
queue<long>a;
int main()
{
    long test,i,j,r,k,n,x,c,sum,s,t=1;
    freopen("c.txt","r",stdin);
    freopen("d.txt","w",stdout);
    scanf("%ld",&test);
    while(test--)
    {
        scanf("%ld %ld %ld",&r,&k,&n);
        for(i=0;i<n;i++)
        {
            cin>>x;
            q.push(x);
        }
      //  for(j=q.front();j<q.end();j++)
        // printf("%ld ",q[i]);
         sum=0;
        for(i=1;i<=r;i++)
        {
            c=0;
            while((q.front()+c)<=k && (!q.empty()))
            {
                 if((q.front()+c)<=k)
                 {
                  c=q.front()+c;
                  sum+=q.front();
                  a.push(q.front());
                //cout<<"a"<<endl;
                  q.pop();
                 }
            }
            while(!a.empty())
            {
                q.push(a.front());
                //cout<<"b"<<endl;
                a.pop();
            }
        }
        printf("Case #%d: ",t++);
         cout<<sum<<endl;
         s=q.size();
         for(i=0;i<s;i++)
         q.pop();
         s=a.size();
         for(i=0;i<s;i++)
         a.pop();

    }
    return 0;
}
