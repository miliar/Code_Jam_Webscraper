#include <cstdio>
#include <cstring>
#include <stack>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <queue>
#include <map>
using namespace std;
struct Node
{
    char  s[3];
    int num;
}node[1000];

int main()
{
    int t,n;
    freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
    scanf("%d",&t);
    int cas=0;
    while(t--)
    {
        scanf("%d",&n);
        queue <int> q1,q2;
        for(int i=0;i<n;i++)
          {
              scanf("%s%d",node[i].s,&node[i].num);
              if(node[i].s[0]=='O')
                  q1.push(node[i].num);
               else
                  q2.push(node[i].num);
          }
        int cur1=1;
        int cur2=1;
        int ans=0;
        for(int i=0;i<n;i++)
        {
            //cout<<cur1<<" "<<cur2<<endl;
            if(node[i].s[0]=='O')
            {
                 int tmp1=q1.front();
                 q1.pop();
                 int t=abs(tmp1-cur1)+1;
                 ans+=t;
                 cur1=tmp1;
                 int tmp2=q2.front();
                 if(t>abs(tmp2-cur2))
                 {
                     cur2=tmp2;
                 }
                 else if(cur2>tmp2)
                   cur2-=t;
                 else
                   cur2+=t;

            }
            else
            {
                 int tmp2=q2.front();
                 q2.pop();
                 int t=abs(tmp2-cur2)+1;
                 ans+=t;
                 cur2=tmp2;
                 int tmp1=q1.front();
                 if(t>abs(tmp1-cur1))
                 {
                     cur1=tmp1;
                 }
                 else  if(cur1>tmp1)
                   cur1-=t;
                 else
                   cur1+=t;

            }

        }

        printf("Case #%d: %d\n",++cas,ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
